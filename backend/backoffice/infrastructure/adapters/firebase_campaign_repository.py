import firebase_admin
from firebase_admin import credentials, firestore
from application.ports.campaign_repository import CampaignRepository
from domain.campaign import Campaign
from typing import List
from dataclasses import asdict

cred = credentials.Certificate("firebase-credentials.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

class FirebaseCampaignRepository(CampaignRepository):

    def get_next_campaign_id(self) -> int:
        last_campaign = db.collection('campañas').order_by('id', direction=firestore.Query.DESCENDING).limit(1).get()
        last_id = last_campaign[0].to_dict()['id'] if last_campaign else 0
        return last_id + 1
    def create_campaign(self, campaign_data: dict) -> None:
        next_id = self.get_next_campaign_id()

        if isinstance(campaign_data, Campaign):
            campaign_data = asdict(campaign_data)
        
        campaign_data['id'] = next_id

        campaign = Campaign(**campaign_data)
        campaign_dict = asdict(campaign)
        db.collection('campañas').document(str(campaign.id)).set(campaign_dict)
        return campaign_data['id']

    def update_product_campaign_id(self, brand_ids: List[int], campaign_id: int) -> None:
        products_ref = db.collection('productos')
        for brand_id in brand_ids:
            products_query = products_ref.where('marcaID', '==', brand_id).stream()
            for product_doc in products_query:
                print("APLICANDO CAMPANIA A PRODUCTO: ",product_doc)
                products_ref.document(product_doc.id).update({'campana_id': campaign_id})

