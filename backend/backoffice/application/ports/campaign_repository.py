# application/ports/campaign_repository.py
from abc import ABC, abstractmethod
from domain.campaign import Campaign
from typing import List

class CampaignRepository(ABC):
    @abstractmethod
    def create_campaign(self, campaign: Campaign) -> None:
        pass

    @abstractmethod
    def update_product_campaign_id(self, brand_ids: List[int], campaign_id: int) -> None:
        pass
