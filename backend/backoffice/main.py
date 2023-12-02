# main.py
from flask import Flask, request, jsonify
from application.campaign_service import CampaignService
from infrastructure.adapters.firebase_campaign_repository import FirebaseCampaignRepository

app = Flask(__name__)
campaign_repository = FirebaseCampaignRepository()
campaign_service = CampaignService(campaign_repository)

@app.route('/backoffice/campaigns/newCampaign', methods=['POST'])
def create_campaign():
    try:
        campaign_data = request.get_json()
        print("DATA :", campaign_data)
        campaign_service.create_campaign(campaign_data)
        return jsonify({'status': 'success', 'data': campaign_data}), 201
    except Exception as e:
        print(f"Error creating campaign: {e}")
        return jsonify({'status': 'error', 'message': 'Internal Server Error'}), 500

@app.route('/backoffice/campaigns/update/<int:campaign_id>', methods=['PATCH'])
def update_campaign(campaign_id):
    try:
        campaign_data = request.get_json()
        campaign_service.update_campaign(campaign_id, campaign_data)
        return jsonify({'status': 'success', 'message': 'Campaign updated successfully.'}), 200
    except Exception as e:
        print(f"Error updating campaign: {e}")
        return jsonify({'status': 'error', 'message': 'Internal Server Error'}), 500
    
@app.route('/backoffice/campaign/<int:campaign_id>', methods=['GET'])
def get_campaign(campaign_id):
    try:
        campaign = campaign_service.get_campaign(campaign_id)
        if campaign:
            return jsonify({'status': 'success', 'data': campaign}), 200
        else:
            return jsonify({'status': 'not found', 'message': 'Campaign not found'}), 404
    except Exception as e:
        print(f"Error retrieving campaign: {e}")
        return jsonify({'status': 'error', 'message': 'Internal Server Error'}), 500    
    
@app.route('/backoffice/campaign/', methods=['GET'])
def get_all_campaigns():
    try:
        campaigns = campaign_service.get_all_campaigns()
        return jsonify({'status': 'success', 'data': campaigns}), 200
    except Exception as e:
        print(f"Error retrieving campaigns: {e}")
        return jsonify({'status': 'error', 'message': 'Internal Server Error'}), 500    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
