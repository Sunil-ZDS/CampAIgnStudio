import streamlit as st
import asyncio
import os
from services.openai_config import create_azure_openai_model
from pydantic_ai import Agent
from pydantic import BaseModel
from typing import List
import requests

class CreativeVariation(BaseModel):
    name: str
    text: str

def generate_dalle3_image(prompt: str) -> str:
    # Load Azure OpenAI config from env
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    api_key = os.getenv("AZURE_OPENAI_API_KEY")
    api_version = os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-01")
    deployment = os.getenv("AZURE_OPENAI_DALLE_DEPLOYMENT")  # e.g. "dall-e-3"

    if not all([endpoint, api_key, deployment]):
        st.error("Azure OpenAI DALLE-3 configuration missing. Check your .env file.")
        return None

    url = f"{endpoint}/openai/deployments/{deployment}/images/generations?api-version={api_version}"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    payload = {
        "model": deployment,
        "prompt": prompt,
        "size": "1024x1024",
        "style": "natural", #natural,vivid
        "quality": "hd", #HD,standard
        "n": 1
    }
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=60)
        response.raise_for_status()
        data = response.json()
        images = data.get("data", [])
        if images and "url" in images[0]:
            return images[0]["url"]
        else:
            st.error("No image URL found in DALLE-3 response.")
            return None
    except Exception as e:
        st.error(f"DALLE-3 error: {e}")
        return None

async def generate_creative_variations(prompt, tone, format_type, num_variations):
    azure_model = create_azure_openai_model()
    agent = Agent(
        model=azure_model,
        output_type=List[CreativeVariation],
        system_prompt=(
            "You are a creative marketing copywriter. "
            "Given a campaign brief, tone, and format, generate a list of natural real looking creative ad copy variations. "
            "For each, provide a meaningful, catchy name and the ad copy text. "
            "Return a list of dicts: [{'name': ..., 'text': ...}]"
        )
    )
    user_prompt = (
        f"CAMPAIGN BRIEF: {prompt}\n"
        f"TONE: {tone or 'Any'}\n"
        f"FORMAT: {format_type or 'Any'}\n"
        f"Generate {num_variations} creative ad copy variations. "
        "Each should have a unique, catchy name and the ad copy text. "
        "Return as a list of dicts: [{'name': ..., 'text': ...}]"
    )
    result = await agent.run(user_prompt)
    return result.output

def show_creative_asset_generator2():
    st.markdown("## 📝 Creative Asset Generator")
    st.markdown("Generate ad copy, headlines, CTAs, and visual ideas for your campaign.")

    with st.form("creative_asset_form2"):
        campaign_brief = st.text_area(
            "Campaign Brief or Prompt",
            placeholder="Describe your campaign or product...",
            key="creative_campaign_brief2"
        )
        tone_preference = st.text_input(
            "Tone Preference",
            placeholder="e.g., playful, professional",
            key="creative_tone_preference2"
        )
        format_type = st.text_input(
            "Desired Format",
            placeholder="e.g., banner, poster",
            key="creative_format_type2"
        )
        num_variations = st.number_input(
            "Number of Text Variations",
            min_value=1, max_value=10, value=3,
            key="creative_num_variations2"
        )
        submitted = st.form_submit_button("Generate Creative Assets")

    if submitted:
        if not campaign_brief:
            st.error("Please enter a campaign brief or prompt.")
            return

        with st.spinner("Generating creative assets..."):
            variations = asyncio.run(
                generate_creative_variations(
                    campaign_brief, tone_preference, format_type, num_variations
                )
            )

            st.markdown("### ✅ Generated Creative Variations:")
            for i, v in enumerate(variations, start=1):
                st.markdown(f"**{i}. {v.name}**")
                st.markdown(f"`{v.text}`")

            st.markdown("### 🖼️ Generated Images for Each Variation:")
            for i, v in enumerate(variations, start=1):
                image_url = generate_dalle3_image(v.text)
                if image_url:
                    st.image(image_url, caption=f"{v.name} - {v.text}")
                    st.markdown(f"[Open Image in New Tab]({image_url})")
                else:
                    st.warning(f"Image for '{v.name}' could not be generated.")

            st.markdown("### 💡 A/B Testing Tips:")
            st.markdown("""
            1. Use different text and image variations for A/B testing.
            2. Test each combination to see what resonates best with your audience.
            3. Monitor engagement metrics to determine the most effective creative assets.
            """)