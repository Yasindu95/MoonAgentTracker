from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/send_notification/", methods=["POST"])
def send_notification():
    # Hardcoded notification data
    member_email = "member001@example.com"
    subject = "Sales Target Notification"
    message = "Dear Patient, this is to inform you that your sales target has been achieved. Congratulations!"

    # Simulating sending email (no actual sending here)
    return jsonify({
        "status": "Notification sent",
        "to": member_email,
        "subject": subject,
        "message": message
    }), 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8002)