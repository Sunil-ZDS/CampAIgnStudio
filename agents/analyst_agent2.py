# agents/analyst_agent.py
# from typing import Dict, List
# from pydantic_ai import Agent
# # import json

# from database.db_manager import DatabaseManager
# from models.response_models import AnalysisOutput

# class AnalystAgent:
#     def __init__(self, model, db_manager: DatabaseManager):
#         self.db_manager = db_manager
#         self.agent = Agent(
#             model=model,
#             output_type=AnalysisOutput,
#             system_prompt="""You are a Senior Marketing Data Analyst with expertise in campaign performance analysis,
#              pattern recognition, and data-driven marketing insights. You excel at identifying success patterns from
#              historical campaign data and translating them into actionable recommendations.

#              **Crucially, your output MUST strictly adhere to the provided JSON schema. Ensure 'channel_performance'
#             and 'budget_recommendations' are objects (dictionaries), not lists or prose.**

#             Focus on:
#             - Identifying patterns in successful campaigns
#             - Channel performance analysis
#             - Audience behavior insights
#             - Budget optimization recommendations
#             - Creative performance trends
#             - ROI and conversion optimization

#             Provide data-driven, actionable insights that can directly improve campaign performance."""
#         )

#     async def analyze_campaign_patterns(self, campaign_objective: str, target_industry: str = None) -> AnalysisOutput:
#         """Analyze historical campaign data to identify success patterns"""

#         # Gather data from database
#         successful_campaigns = await self.db_manager.get_successful_campaigns(20)
#         channel_performance = await self.db_manager.get_channel_performance()
#         industry_insights = await self.db_manager.get_industry_insights(target_industry)

#         print("DEBUG channel_performance:", channel_performance)

#         # Prepare analysis prompt
#         analysis_prompt = f"""
#         Develop a comprehensive marketing strategy using historical performance insights:

#         CAMPAIGN OBJECTIVE: {campaign_objective}
#         TARGET INDUSTRY: {target_industry or "General"}

#         HISTORICAL SUCCESS DATA:

#         TOP PERFORMING CAMPAIGNS:
#         {self._format_campaign_data(successful_campaigns)}

#         CHANNEL PERFORMANCE ANALYSIS:
#         {self._format_channel_data(channel_performance)}

#         INDUSTRY INSIGHTS:
#         {self._format_industry_data(industry_insights)}

#         Based on this data, provide insights adhering strictly to the AnalysisOutput schema:
#         1.  `successful_patterns`: List of key success patterns.
#         2.  `channel_performance`: A JSON object (dictionary) where keys are channel names (e.g., "Social Media") and values are their average performance metrics (e.g., {{"avg_success_score": 8.5, "avg_roas": 7.2}}). Do NOT provide a list of descriptive strings.
#         3.  `audience_insights`: List of audience-related insights.
#         4.  `budget_recommendations`: A JSON object (dictionary) where keys are budget categories (e.g., "Low Budget", "High Budget") or specific channel names, and values are budget recommendations for them (e.g., {{"Social Media": "Invest more in video ads", "Content Marketing": "Allocate 20% of budget"}}). Do NOT provide a list of descriptive strings.
#         5.  `creative_trends`: List of effective creative trends.
#         6.  `key_success_factors`: List of critical factors.
#         7.  `recommendations`: List of actionable recommendations.

#         Focus on actionable insights that can be directly applied to strategy and creative development.
#         """
#         result = await self.agent.run(analysis_prompt)
#         return result.output

#     def _format_campaign_data(self, campaigns: List[Dict]) -> str:
#         """Format campaign data for analysis"""
#         if not campaigns:
#             return "No successful campaigns found"
#         formatted = []
#         for camp in campaigns[:10]:  # Top 10 for brevity
#             formatted.append(
#                 f"• {camp['campaign_name']} | Industry: {camp['industry']} | "
#                 f"Success Score: {camp['success_score']} | ROAS: {camp['roas']} | "
#                 f"Channels: {', '.join(camp['channels'])} | "
#                 f"Creative: {camp['creative_type']} | Tone: {camp['messaging_tone']}"
#             )
#         return "\n".join(formatted)

#     def _format_channel_data(self, channels: Dict) -> str:
#         """Format channel performance data"""
#         if not channels:
#             return "No channel data available"
#         formatted = []
#         for channel, data in channels.items():
#             formatted.append(
#                 f"• {channel}: Success Score {data['avg_success_score']:.2f} | "
#                 f"ROAS {data['avg_roas']:.2f} | CTR {data['avg_ctr']:.4f} | "
#                 f"Campaigns: {data['campaign_count']}"
#             )
#         return "\n".join(formatted)

#     def _format_industry_data(self, industries: List[Dict]) -> str:
#         """Format industry insights data"""
#         if not industries:
#             return "No industry data available"
#         formatted = []
#         for industry in industries[:5]:  # Top 5 industries
#             formatted.append(
#                 f"• {industry['industry']}: Avg Success {industry['avg_success_score']:.2f} | "
#                 f"Avg Budget ${industry['avg_budget']:,.0f} | "
#                 f"Campaigns: {industry.get('campaign_count', 'N/A')}"
#             )
#         return "\n".join(formatted)
    
#     def _format_channel_data_for_prompt(self, channels: Dict) -> str:
#         """Format channel performance data specifically for the prompt as key-value pairs."""
#         if not channels:
#             return "No channel data available."
#         formatted = []
#         for channel, data in channels.items():
#             formatted.append(
#                 f'"{channel}": {{"avg_success_score": {data["avg_success_score"]:.2f}, '
#                 f'"avg_roas": {data["avg_roas"]:.2f}, '
#                 f'"avg_ctr": {data["avg_ctr"]:.4f}, '
#                 f'"avg_conversion_rate": {data["avg_conversion_rate"]:.4f}, '
#                 f'"campaign_count": {data["campaign_count"]}}}'
#             )
#         # Wrap it in curly braces to suggest it's part of a JSON object
#         return "{\n" + ",\n".join(formatted) + "\n}"

# from typing import Dict, List
# from pydantic_ai import Agent
# from database.db_manager import DatabaseManager
# from models.response_models import AnalysisOutput
# import random

# class AnalystAgent:
#     def __init__(self, model, db_manager: DatabaseManager):
#         self.db_manager = db_manager
#         self.agent = Agent(
#             model=model,
#             output_type=AnalysisOutput,
#             system_prompt="""You are a Senior Marketing Data Analyst with expertise in campaign performance analysis,
#              pattern recognition, and data-driven marketing insights. You excel at identifying success patterns from
#              historical campaign data and translating them into actionable recommendations.

#              **Crucially, your output MUST strictly adhere to the provided JSON schema. Ensure 'channel_performance'
#             and 'budget_recommendations' are objects (dictionaries), not lists or prose.**

#             Focus on:
#             - Identifying patterns in successful campaigns
#             - Channel performance analysis
#             - Audience behavior insights
#             - Budget optimization recommendations
#             - Creative performance trends
#             - ROI and conversion optimization

#             Provide data-driven, actionable insights that can directly improve campaign performance."""
#         )

    # async def analyze_campaign_patterns(self, campaign_objective: str, target_industry: str = None) -> AnalysisOutput:
    #     """Bypass analysis and return default AnalysisOutput structure."""
    #     # Return a default AnalysisOutput with generic/sample data
    #     return AnalysisOutput(
    #         executive_summary="This analysis identifies key success patterns, top-performing channels, and actionable recommendations for your campaign.",
    #         successful_patterns=[
    #             "Strong brand messaging",
    #             "Consistent multi-channel presence",
    #             "Personalized audience targeting"
    #         ],
    #         channel_performance={
    #             "Social Media": {
    #                 "avg_success_score": 8.2,
    #                 "avg_roas": 6.5,
    #                 "avg_ctr": 3.1,
    #                 "avg_conversion_rate": 4.8,
    #                 "campaign_count": 25
    #             },
    #             "Search": {
    #                 "avg_success_score": 7.9,
    #                 "avg_roas": 5.8,
    #                 "avg_ctr": 2.7,
    #                 "avg_conversion_rate": 4.2,
    #                 "campaign_count": 18
    #             }
    #         },
    #         audience_insights=[
    #             "Millennials engage most with video content",
    #             "Parents respond well to value-driven messaging"
    #         ],
    #         budget_recommendations={
    #             "Social Media": "Allocate 40% of budget",
    #             "Search": "Allocate 30% of budget",
    #             "Content Marketing": "Allocate 20% of budget",
    #             "Other": "Allocate 10% of budget"
    #         },
    #         creative_trends=[
    #             "Short-form video",
    #             "User-generated content",
    #             "Interactive polls"
    #         ],
    #         key_success_factors=[
    #             "Clear CTA",
    #             "Mobile-first design",
    #             "A/B testing"
    #         ],
    #         recommendations=[
    #             "Increase investment in social video ads",
    #             "Test new creative formats monthly",
    #             "Leverage influencer partnerships"
    #         ]
    #     )

import random
from models.response_models import AnalysisOutput

class AnalystAgent:
    def __init__(self, model, db_manager):
        self.db_manager = db_manager
        self.agent = None  # Not used in bypass mode

    async def analyze_campaign_patterns(self, campaign_objective: str, target_industry: str = None) -> AnalysisOutput:
        """Bypass analysis and return randomized AnalysisOutput structure."""

        patterns_pool = [
            "Strong brand messaging", "Consistent multi-channel presence", "Personalized audience targeting",
            "Seasonal promotions", "Influencer partnerships", "Localized content", "Interactive campaigns",
            "Data-driven optimization", "Cross-channel retargeting", "Customer testimonials", "Limited-time offers",
            "Gamified experiences", "Mobile-first design", "Storytelling approach", "Sustainability messaging",
            "Community engagement", "User-generated content", "Dynamic creative rotation", "Geo-targeted ads",
            "Behavioral segmentation", "Responsive design", "Social proof integration", "Referral programs",
            "Loyalty incentives", "Real-time engagement", "Conversational marketing", "AI-powered recommendations",
            "Personalized email flows", "Video-first strategy", "Shoppable posts", "Micro-influencer campaigns"
        ]
        channels_pool = [
            "Social Media", "Search", "Email", "Display", "Video", "Influencer", "Content Marketing",
            "Podcast", "SMS", "Mobile App", "Affiliate", "Native Ads", "Connected TV", "Out-of-home",
            "Direct Mail", "Events", "Webinars", "Pinterest", "Snapchat", "Reddit", "Quora", "WhatsApp",
            "Messenger", "Telegram", "Discord", "YouTube Shorts", "Instagram Reels", "LinkedIn", "Twitter",
            "TikTok", "Google Shopping"
        ]
        audience_pool = [
            "Millennials engage most with video content", "Parents respond well to value-driven messaging",
            "Gen Z prefers interactive polls", "Seniors respond to trusted testimonials",
            "Urban professionals like concise messaging", "Students react to meme-based ads",
            "Remote workers prefer flexible offers", "Fitness enthusiasts engage with challenges",
            "Gamers respond to exclusive drops", "Pet owners love relatable stories",
            "Eco-conscious buyers seek sustainability", "Travelers engage with destination imagery",
            "Foodies react to recipe content", "Fashionistas love trend alerts",
            "Techies respond to product demos", "Entrepreneurs prefer actionable tips",
            "Artists engage with creative showcases", "Parents value educational content",
            "Sports fans react to live updates", "Homeowners prefer DIY guides",
            "Luxury buyers seek exclusivity", "Budget shoppers respond to deals",
            "Health-conscious audiences engage with wellness tips", "Music lovers react to playlists",
            "Bookworms prefer recommendations", "Collectors engage with limited editions",
            "Students value scholarships", "Retirees respond to financial advice",
            "Young professionals prefer networking events", "Freelancers engage with productivity hacks",
            "Teachers value classroom resources"
        ]
        budget_pool = [
            {"Social Media": "Allocate 40% of budget", "Search": "Allocate 30% of budget", "Content Marketing": "Allocate 20% of budget", "Other": "Allocate 10% of budget"},
            {"Video": "Allocate 50% of budget", "Influencer": "Allocate 20% of budget", "Search": "Allocate 20% of budget", "Other": "Allocate 10% of budget"},
            {"Email": "Allocate 25% of budget", "Social Media": "Allocate 35% of budget", "Display": "Allocate 30% of budget", "Other": "Allocate 10% of budget"},
            {"Podcast": "Allocate 15% of budget", "Mobile App": "Allocate 25% of budget", "Affiliate": "Allocate 30% of budget", "Other": "Allocate 30% of budget"},
            {"Native Ads": "Allocate 20% of budget", "Connected TV": "Allocate 30% of budget", "Out-of-home": "Allocate 25% of budget", "Other": "Allocate 25% of budget"},
            {"Direct Mail": "Allocate 10% of budget", "Events": "Allocate 40% of budget", "Webinars": "Allocate 30% of budget", "Other": "Allocate 20% of budget"},
            {"Pinterest": "Allocate 20% of budget", "Snapchat": "Allocate 20% of budget", "Reddit": "Allocate 20% of budget", "Other": "Allocate 40% of budget"},
            {"Quora": "Allocate 15% of budget", "WhatsApp": "Allocate 25% of budget", "Messenger": "Allocate 30% of budget", "Other": "Allocate 30% of budget"},
            {"Telegram": "Allocate 10% of budget", "Discord": "Allocate 20% of budget", "YouTube Shorts": "Allocate 40% of budget", "Other": "Allocate 30% of budget"},
            {"Instagram Reels": "Allocate 35% of budget", "LinkedIn": "Allocate 25% of budget", "Twitter": "Allocate 20% of budget", "Other": "Allocate 20% of budget"},
            {"TikTok": "Allocate 40% of budget", "Google Shopping": "Allocate 30% of budget", "Email": "Allocate 20% of budget", "Other": "Allocate 10% of budget"},
            {"Display": "Allocate 30% of budget", "Content Marketing": "Allocate 30% of budget", "Video": "Allocate 30% of budget", "Other": "Allocate 10% of budget"},
            {"Influencer": "Allocate 35% of budget", "Social Media": "Allocate 35% of budget", "Search": "Allocate 20% of budget", "Other": "Allocate 10% of budget"},
            {"Affiliate": "Allocate 25% of budget", "Native Ads": "Allocate 25% of budget", "Connected TV": "Allocate 25% of budget", "Other": "Allocate 25% of budget"},
            {"Out-of-home": "Allocate 20% of budget", "Direct Mail": "Allocate 20% of budget", "Events": "Allocate 30% of budget", "Other": "Allocate 30% of budget"},
            {"Webinars": "Allocate 30% of budget", "Pinterest": "Allocate 20% of budget", "Snapchat": "Allocate 20% of budget", "Other": "Allocate 30% of budget"},
            {"Reddit": "Allocate 15% of budget", "Quora": "Allocate 25% of budget", "WhatsApp": "Allocate 30% of budget", "Other": "Allocate 30% of budget"},
            {"Messenger": "Allocate 10% of budget", "Telegram": "Allocate 20% of budget", "Discord": "Allocate 40% of budget", "Other": "Allocate 30% of budget"},
            {"YouTube Shorts": "Allocate 35% of budget", "Instagram Reels": "Allocate 25% of budget", "LinkedIn": "Allocate 20% of budget", "Other": "Allocate 20% of budget"},
            {"Twitter": "Allocate 40% of budget", "TikTok": "Allocate 30% of budget", "Google Shopping": "Allocate 20% of budget", "Other": "Allocate 10% of budget"},
            {"Email": "Allocate 30% of budget", "Display": "Allocate 30% of budget", "Content Marketing": "Allocate 30% of budget", "Other": "Allocate 10% of budget"},
            {"Video": "Allocate 35% of budget", "Influencer": "Allocate 35% of budget", "Social Media": "Allocate 20% of budget", "Other": "Allocate 10% of budget"},
            {"Search": "Allocate 25% of budget", "Affiliate": "Allocate 25% of budget", "Native Ads": "Allocate 25% of budget", "Other": "Allocate 25% of budget"},
            {"Connected TV": "Allocate 20% of budget", "Out-of-home": "Allocate 20% of budget", "Direct Mail": "Allocate 30% of budget", "Other": "Allocate 30% of budget"},
            {"Events": "Allocate 30% of budget", "Webinars": "Allocate 20% of budget", "Pinterest": "Allocate 20% of budget", "Other": "Allocate 30% of budget"},
            {"Snapchat": "Allocate 15% of budget", "Reddit": "Allocate 25% of budget", "Quora": "Allocate 30% of budget", "Other": "Allocate 30% of budget"},
            {"WhatsApp": "Allocate 10% of budget", "Messenger": "Allocate 20% of budget", "Telegram": "Allocate 40% of budget", "Other": "Allocate 30% of budget"},
            {"Discord": "Allocate 35% of budget", "YouTube Shorts": "Allocate 25% of budget", "Instagram Reels": "Allocate 20% of budget", "Other": "Allocate 20% of budget"},
            {"LinkedIn": "Allocate 40% of budget", "Twitter": "Allocate 30% of budget", "TikTok": "Allocate 20% of budget", "Other": "Allocate 10% of budget"}
        ]
        creative_trends_pool = [
            "Short-form video", "User-generated content", "Interactive polls", "Animated explainers", "Live streams",
            "360-degree product views", "AR experiences", "Shoppable posts", "Influencer takeovers", "Behind-the-scenes content",
            "Podcast sponsorships", "Gamified ads", "Personalized recommendations", "Dynamic email banners", "Interactive infographics",
            "Virtual events", "Social challenges", "Memes", "Voice search optimization", "Mobile-first layouts",
            "Ephemeral content", "Micro-videos", "Interactive quizzes", "Swipeable carousels", "AI-generated art",
            "Sustainability stories", "Customer testimonials", "Product demos", "Countdown timers", "Interactive maps"
        ]
        key_success_pool = [
            "Clear CTA", "Mobile-first design", "A/B testing", "Personalized offers", "Strong visual hierarchy",
            "Consistent branding", "Fast load times", "Trust signals", "Social proof", "Easy navigation",
            "Relevant targeting", "Compelling headlines", "Optimized landing pages", "Responsive design", "Engaging visuals",
            "Value proposition clarity", "Multi-step funnels", "Retargeting", "Segmentation", "Real-time analytics",
            "Cross-device compatibility", "Accessibility", "Localized messaging", "Seasonal relevance", "Urgency cues",
            "Interactive elements", "Customer support integration", "Feedback loops", "Storytelling", "Emotional appeal"
        ]
        recommendations_pool = [
            "Increase investment in social video ads", "Test new creative formats monthly", "Leverage influencer partnerships",
            "Expand retargeting efforts", "Optimize landing pages for conversions", "Run seasonal campaigns",
            "Use dynamic creative rotation", "Launch interactive polls", "Try AR experiences", "Sponsor podcasts",
            "Host virtual events", "Utilize shoppable posts", "Engage micro-influencers", "Create behind-the-scenes content",
            "Implement gamified ads", "Personalize recommendations", "Add countdown timers", "Use interactive infographics",
            "Promote sustainability stories", "Feature customer testimonials", "Demo products live", "Optimize for voice search",
            "Use ephemeral content", "Launch swipeable carousels", "Integrate AI-generated art", "Highlight value proposition",
            "Improve accessibility", "Segment audiences", "Increase urgency cues", "Collect feedback regularly", "Tell brand stories"
        ]

        successful_patterns = random.sample(patterns_pool, k=3)
        selected_channels = random.sample(channels_pool, k=2)
        channel_performance = {}
        for channel in selected_channels:
            channel_performance[channel] = {
                "avg_success_score": round(random.uniform(7.0, 9.0), 2),
                "avg_roas": round(random.uniform(4.0, 7.0), 2),
                "avg_ctr": round(random.uniform(2.0, 4.0), 2),
                "avg_conversion_rate": round(random.uniform(3.5, 6.0), 2),
                "campaign_count": random.randint(15, 35)
            }
        
        audience_insights = random.sample(audience_pool, k=2)
        budget_recommendations = random.choice(budget_pool)
        creative_trends = random.sample(creative_trends_pool, k=3)
        key_success_factors = random.sample(key_success_pool, k=3)
        recommendations = random.sample(recommendations_pool, k=3)

        executive_summary = (
            f"This analysis highlights {', '.join(successful_patterns)} as key success patterns. "
            f"Top channels: {', '.join(selected_channels)}. "
            f"Recommendations: {', '.join(recommendations)}."
        )

        return AnalysisOutput(
            executive_summary=executive_summary,
            successful_patterns=successful_patterns,
            channel_performance=channel_performance,
            audience_insights=audience_insights,
            budget_recommendations=budget_recommendations,
            creative_trends=creative_trends,
            key_success_factors=key_success_factors,
            recommendations=recommendations
        )

    # def _format_campaign_data(self, campaigns: List[Dict]) -> str:
    #     return "Bypassed: No campaign data formatting."

    # def _format_channel_data(self, channels: Dict) -> str:
    #     return "Bypassed: No channel data formatting."

    # def _format_industry_data(self, industries: List[Dict]) -> str:
    #     return "Bypassed: No industry data formatting."

    # def _format_channel_data_for_prompt(self, channels: Dict) -> str:
    #     return "Bypassed: No channel data formatting for prompt."