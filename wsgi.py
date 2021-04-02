from flask import request
from app.factory import create_app
from app.domain.use_cases import GetPovertyPrediction


app = create_app()
prediction = GetPovertyPrediction(app.config)

@app.route('/predict', methods=['POST'])
def run():
    info = request.get_json()
    response = prediction.execute(info)
    return response

@app.route('/status', methods=['GET'])
def status():
    return {'response': 'Hello world!'}, 200