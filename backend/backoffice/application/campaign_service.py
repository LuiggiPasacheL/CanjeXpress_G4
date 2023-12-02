from application.ports.campaign_repository import CampaignRepository
from domain.campaign import Campaign

class CampaignService:
    def __init__(self, campaign_repository: CampaignRepository):
        self.campaign_repository = campaign_repository

    def create_campaign(self, campaign_data: dict) -> None:
        campaign = Campaign(**campaign_data)
        campaing_id = self.campaign_repository.create_campaign(campaign)
        self.campaign_repository.update_product_campaign_id(campaign.brands, campaing_id)
    def update_campaign(self, campaign_id: int, campaign_data: dict) -> None:
        self.campaign_repository.update_campaign(campaign_id, campaign_data)

    def get_campaign(self, campaign_id: int):
        return self.campaign_repository.get_campaign_by_id(campaign_id)        
    
    def get_all_campaigns(self):
            return self.campaign_repository.get_all_campaigns()    