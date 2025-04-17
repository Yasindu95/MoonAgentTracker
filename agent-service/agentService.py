from flask import Flask, jsonify

app = Flask(__name__)

# Hardcoded patient data
agents = [
    {
        "agent_code": 1,
        "name": "John 5566 Doe",
        "age": 30,
        "gender": "Male",
        "products":["Life Insurance", "Health Insurance"],
     },
    {
        "agent_code": 2,
        "name": "Jane e55444 Smith",
        "age": 25,
        "gender": "Female",       
        "products":["Life Insurance", "Health Insurance", "Car Insurance"],
    },
        {
        "agent_code": 3,
        "name": "Kim 5r55 Kate",
        "age": 23,
        "gender": "Female",       
        "products":["Life Insurance", "Health Insurance", "Car Insurance", "Travel Insurance"],
    }
]

@app.route("/agents/", methods=["GET"])
def get_agents():
    return jsonify(agents)

@app.route("/agents/<int:agent_code>", methods=["GET"])
def get_agent(agent_code: int):
    agent = next((a for a in agents if a["agent_code"] == agent_code), None)
    if agent:
        return jsonify(agent)
    return jsonify({"error": "Agent not found"}), 404

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8000)