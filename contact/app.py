from flask import Flask, request, jsonify
from flask_cors import CORS
import csv, os

app = Flask(__name__)

# ✅ Allow requests from your frontend (5500)
CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1:5500"}})

CSV_FILE = "contact_messages.csv"

if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Email", "Message"])

@app.route('/api/contact/submit', methods=['POST'])
def contact_submit():
    try:
        data = request.get_json()
        name = data.get("name", "").strip()
        email = data.get("email", "").strip()
        message = data.get("message", "").strip()

        if not name or not email or not message:
            return jsonify({"error": "All fields required"}), 400

        with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([name, email, message])

        print(f"✅ Message received from {name} ({email})")
        return jsonify({"status": "success", "message": "Saved successfully!"}), 200

    except Exception as e:
        print("❌ Error:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
