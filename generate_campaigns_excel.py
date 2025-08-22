import pandas as pd
from datetime import datetime, timedelta
import random

industries = ["Retail", "Finance", "Healthcare", "Education", "Technology", "Travel", "Automotive", "Food & Beverage"]
channels_list = ["Facebook", "Instagram", "Google", "YouTube", "LinkedIn", "Twitter", "TikTok"]
creative_types = ["Image", "Video", "Carousel", "Story", "Banner"]
messaging_tones = ["Playful", "Professional", "Friendly", "Inspirational", "Urgent", "Confident"]

data = []
for i in range(1, 101):
    industry = random.choice(industries)
    channels = ", ".join(random.sample(channels_list, k=random.randint(1, 3)))
    creative_type = random.choice(creative_types)
    messaging_tone = random.choice(messaging_tones)
    budget = round(random.uniform(1000, 50000), 2)
    duration_days = random.randint(7, 90)
    ctr = round(random.uniform(0.5, 5.0), 2)
    conversion_rate = round(random.uniform(0.5, 10.0), 2)
    roas = round(random.uniform(1.0, 10.0), 2)
    engagement_rate = round(random.uniform(0.5, 10.0), 2)
    brand_lift = round(random.uniform(0.1, 5.0), 2)
    success_score = round(random.uniform(5.0, 10.0), 2)
    launch_date = datetime.now() - timedelta(days=random.randint(0, 365))
    created_at = launch_date

    data.append({
        "campaign_id": f"CMP{i:03d}",
        "campaign_name": f"Campaign {i}",
        "industry": industry,
        "target_audience": f"Audience {random.randint(1, 10)}",
        "channels": channels,
        "budget": budget,
        "duration_days": duration_days,
        "ctr": ctr,
        "conversion_rate": conversion_rate,
        "roas": roas,
        "engagement_rate": engagement_rate,
        "brand_lift": brand_lift,
        "success_score": success_score,
        "creative_type": creative_type,
        "messaging_tone": messaging_tone,
        "launch_date": launch_date.date(),
        "created_at": created_at.date()
    })

df = pd.DataFrame(data)
df.to_excel("campaigns.xlsx", index=False)
print("campaigns.xlsx generated with 100 sample campaigns.")