# main.py
from flask import Flask, request, jsonify
from application.campaign_service import CampaignService
from infrastructure.adapters.firebase_campaign_repository import FirebaseCampaignRepository

app = Flask(__name__)
campaign_repository = FirebaseCampaignRepository()
campaign_service = CampaignService(campaign_repository)

@app.route('/backoffice/campaigns/newCampaign', methods=['POST'])
def create_campaign():
    campaign_data = request.get_json()
    print("DATA :",campaign_data)
    campaign_service.create_campaign(campaign_data)
    return jsonify({'status': 'success', 'data': campaign_data}), 201

if __name__ == '__main__':
    app.run(debug=True)
