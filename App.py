from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
device_locations = {}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/location', methods=['POST'])
def update_location():
    data = request.get_json()
    device = data.get("device")
    if not device:
        return jsonify({"error": "Device name required"}), 400
    device_locations[device] = {
        "latitude": data.get("latitude"),
        "longitude": data.get("longitude"),
        "timestamp": data.get("timestamp")
    }
    return jsonify({"status": "Location updated"}), 200

@app.route('/get-location/<device>', methods=['GET'])
def get_location(device):
    location = device_locations.get(device)
    if location:
        return jsonify(location), 200
    else:
        return jsonify({"error": "Device not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
