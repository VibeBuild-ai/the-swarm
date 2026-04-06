from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app) # Allows your Dashboard from GitHub Pages to access the hub

@app.route('/nexus_gateway', methods=['POST'])
def nexus_gateway():
    """The Diplomat: Routes requests securely from GitHub to Google Vertex AI"""
    target_url = request.args.get('url')
    if not target_url:
        return jsonify({"error": "Missing target URL"}), 400
    
    headers = {
        "Authorization": request.headers.get("Authorization"),
        "Content-Type": request.headers.get("Content-Type")
    }
    
    try:
        response = requests.post(
            target_url, 
            data=request.data, 
            headers=headers,
            timeout=30
        )
        return (response.text, response.status_code, response.headers.items())
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Start on port 5005 (or your desired port)
    app.run(host='0.0.0.0', port=5005)
