from flask import Flask, jsonify, request
import logging

# Configure basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

@app.route("/sales", methods=["POST"])
def handle_sales_post():
    """
    A simple placeholder endpoint that acknowledges POST requests.
    """
    # You could optionally log the received data:
    # if request.is_json:
    #     data = request.get_json()
    #     logging.info(f"Received POST data: {data}")
    # else:
    #     logging.info(f"Received non-JSON POST request")

    logging.info("Received POST request on /sales")
    return jsonify({"message": "Integration Service received POST request"}), 200 # Respond with 200 OK

@app.route("/health-status", methods=["GET"])
def health_check():
    """Basic health check endpoint."""
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    # Port 8080 matches the containerPort often used in the CDK/K8s definitions
    app.run(host="0.0.0.0", port=8001)