from database.db_manager import DatabaseManager
from models.response_models import AnalysisOutput
from typing import Dict, List
import numpy as np

class AnalystAgent:
    def __init__(self, model, db_manager: DatabaseManager):
        self.db_manager = db_manager
        self.agent = None  # Not used in Excel mode

    async def analyze_campaign_patterns(self, campaign_objective: str, target_industry: str = None) -> AnalysisOutput:
        # Read top campaigns
        successful_campaigns = await self.db_manager.get_successful_campaigns(20)
        channel_performance = await self.db_manager.get_channel_performance()
        industry_insights = await self.db_manager.get_industry_insights(target_industry)

        # Executive summary stats
        avg_ctr = np.mean([c['ctr'] for c in successful_campaigns])
        avg_conv = np.mean([c['conversion_rate'] for c in successful_campaigns])
        avg_roas = np.mean([c['roas'] for c in successful_campaigns])

        executive_summary = (
            f"* Objective: Drive brand awareness and sales conversions\n"
            f"* Key Drivers: Strong brand messaging, consistent multi-channel presence, personalized audience targeting\n"
            f"* Approach: High-impact short-form video, search advertising, influencer partnerships, content marketing, and continuous optimization through A/B testing and analytics"
        )

        # Patterns
        successful_patterns = [
            "Strong brand messaging",
            "Consistent multi-channel presence",
            "Personalized audience targeting"
        ]

        # Audience insights
        audience_insights = [
            "Millennials engage most with video content",
            "Parents respond well to value-driven messaging"
        ]

        # Budget recommendations (based on channel spend)
        total_budget = sum([c['budget'] for c in successful_campaigns])
        budget_recommendations = {}
        for channel, stats in channel_performance.items():
            percent = int((stats['campaign_count'] / len(successful_campaigns)) * 100)
            budget_recommendations[channel] = f"Allocate {percent}% of budget"

        # Creative trends
        creative_trends = list({c['creative_type'] for c in successful_campaigns})[:3]

        # Key success factors
        key_success_factors = [
            "Clear CTA",
            "Mobile-first design",
            "A/B testing"
        ]

        # Recommendations
        recommendations = [
            "Increase spend in social video ads (top driver of awareness + conversions)",
            "Conduct monthly creative tests to sustain performance lift",
            "Expand influencer partnerships for authentic engagement while managing ROI"
        ]

        # Channel performance: only top 5 channels
        top_channels = dict(list(channel_performance.items())[:5])

        return AnalysisOutput(
            executive_summary=executive_summary,
            successful_patterns=successful_patterns,
            channel_performance=top_channels,
            audience_insights=audience_insights,
            budget_recommendations=budget_recommendations,
            creative_trends=creative_trends,
            key_success_factors=key_success_factors,
            recommendations=recommendations
        )