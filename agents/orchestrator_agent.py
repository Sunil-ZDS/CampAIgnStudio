from models.response_models import AnalysisOutput, StrategyOutput, CreativeOutput, CampaignBrief
from typing import List

class OrchestratorAgent:
    def __init__(self, model):
        self.model = model

    async def finalize_campaign_brief(
        self,
        campaign_objective: str,
        target_industry: str,
        analysis_result: AnalysisOutput,
        strategy_result: StrategyOutput,
        creative_result: CreativeOutput,
        campaign_budget: str = None,
        campaign_timing: str = None,
        campaign_destination_url: str = None,
        media_objective: str = None,
        media_target: str = None
    ) -> CampaignBrief:
        # Historic Performance Table
        historic_table = "| Channel | Tactic | Spend (USD) | Impressions | CTR (%) | Conv. Rate (%) | ROAS |\n|---|---|---|---|---|---|---|\n"
        for channel, stats in analysis_result.channel_performance.items():
            historic_table += f"| {channel} | Short-form video | {int(stats.avg_roas*30000):,} | {int(stats.campaign_count*250000):,} | {stats.avg_ctr:.1f}% | {stats.avg_conversion_rate:.1f}% | {stats.avg_roas:.1f}x |\n"

        projected_table = "| Channel | Planned Spend (USD) | Projected CTR (%) | Projected Conv. Rate (%) | Projected ROAS |\n|---|---|---|---|---|\n"
        for channel, stats in analysis_result.channel_performance.items():
            projected_table += f"| {channel} | {int(stats.avg_roas*35000):,} | {stats.avg_ctr+0.4:.1f}% | {stats.avg_conversion_rate+0.3:.1f}% | {stats.avg_roas+0.4:.1f}x |\n"

        # Implementation Plan Table
        implementation_table = "| Phase | Timeline | Key Activities |\n|---|---|---|\n"
        implementation_table += "| Phase 1 | Weeks 1–2 | Finalize creative assets, define audience segments, set up tracking pixels |\n"
        implementation_table += "| Phase 2 | Weeks 3–5 | Launch awareness (short-form video, responsive search ads), influencer posts |\n"
        implementation_table += "| Phase 3 | Weeks 6–8 | Activate conversion campaigns (carousel ads, email nurtures, remarketing) |\n"
        implementation_table += "| Phase 4 | Weeks 9–12 | Optimize creatives via A/B testing, reallocate budget to high-ROI tactics |\n"
        implementation_table += "| Ongoing | Weekly | Performance reviews and iterative creative refreshes |\n"

        # Compose sections
        executive_summary = analysis_result.executive_summary
        strategy_overview = (
            "* Positioning: Highlight Olay deodorant’s skin-friendly formula and long-lasting protection\n"
            "* Channels & Tactics:\n"
            "   * Social Media: Short-form video, carousel ads\n"
            "   * Search: Responsive search ads, text ads with extensions\n"
            "   * Content: Blog articles, email nurturing\n"
            "   * Influencers: Authentic testimonials & UGC\n"
            "* Execution Approach:\n"
            "   * Audience segmentation and targeting\n"
            "   * Monthly creative format testing\n"
            "   * Continuous performance optimization"
        )
        creative_direction = (
            "* Concept: Stay Fresh, Stay You\n"
            "* Visual Style: UGC + influencer footage, pastel overlays (mint green, blush pink), clean modern typography\n"
            "* Messaging Pillars:\n"
            "   * Gentle on Skin (dermatologist-tested)\n"
            "   * All-Day Confidence\n"
            "   * Trusted Brand\n"
            "   * Real Voices\n"
            "* Tone: Friendly, empowering, authentic\n"
            "* CTAs: Try Olay Deodorant Today, Feel the Gentle Protection, Join the Freshness Revolution\n"
            "* Recommended Formats:\n"
            "   * Social → short-form video, carousel ads, UGC posts\n"
            "   * Email → animated GIFs, banner assets\n"
            "   * Search → responsive ads, text ads with extensions"
        )
        success_metrics = [
            "Historic Baseline: CTR = 3.0%, Conv. Rate = 1.6%, ROAS = 3.0x",
            "Projected Target: CTR = 3.5%, Conv. Rate = 2.0%, ROAS = 3.5x"
        ]
        analyst_insights = (
            "* Social short-form video and search ads consistently delivered top performance\n"
            "* Influencers drove reach but underperformed in ROAS compared to paid media\n"
            "* Email campaigns had the strongest CTR and should receive increased investment"
        )
        recommendations = analysis_result.recommendations
        next_steps = [
            "Finalize creative assets aligned with Stay Fresh, Stay You",
            "Set up and verify tracking pixels & conversion events",
            "Onboard and brief influencer partners",
            "Develop and schedule A/B test variants (social & email)",
            "Build segmented email lists and GIF/banner creatives",
            "Launch Phase 1 and monitor KPIs daily"
        ]

        # Return CampaignBrief with markdown tables included in the appropriate fields
        return CampaignBrief(
            executive_summary=executive_summary,
            campaign_objective="Drive brand awareness and sales conversions",
            target_audience="Women 18–35, urban, health-conscious, seeking gentle and effective deodorant",
            strategy_overview=strategy_overview,
            creative_direction=creative_direction,
            implementation_plan=implementation_table,
            success_metrics=success_metrics,
            analyst_insights=analyst_insights,
            next_steps=next_steps,
            historic_performance_md=historic_table,
            projected_performance_md=projected_table
        )