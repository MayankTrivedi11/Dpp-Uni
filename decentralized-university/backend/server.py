from flask import Flask, jsonify, request
from flask_cors import CORS
from web3 import Web3
import json

app = Flask(__name__)
CORS(app)

# Connect to Ethereum Node (Local Hardhat or Infura)
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))

# Load Smart Contract ABI & Address
with open("CourseManagementABI.json") as f:
    contract_abi = json.load(f)

contract_address = "0xYourSmartContractAddress"  # Replace after deployment
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

@app.route("/api/courses", methods=["GET"])
def get_courses():
    try:
        courses = contract.functions.getCourses().call()
        return jsonify([
            {"id": course[0], "title": course[1], "description": course[2], "instructor": course[3]}
            for course in courses
        ])
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/courses", methods=["POST"])
def add_course():
    data = request.json
    title = data.get("title")
    description = data.get("description")
    instructor = data.get("instructor")

    if not title or not instructor:
        return jsonify({"error": "Title and Instructor are required"}), 400

    try:
        tx_hash = contract.functions.addCourse(title, description, instructor).transact({"from": w3.eth.accounts[0]})
        w3.eth.wait_for_transaction_receipt(tx_hash)
        return jsonify({"message": "Course added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=8000, debug=True)
