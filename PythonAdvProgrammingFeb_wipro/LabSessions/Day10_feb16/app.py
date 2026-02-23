from flask import Flask,request,jsonify

app = Flask(__name__)

customers = {}
next_id = 1


@app.route("/customers", methods = ["POST"])
def create_customer():
    global  next_id

    data = request.json

    customer = {
        "id" : next_id,
        "name": data.get("name"),
        "email": data.get("email"),
        "balance": data.get("balance",0)
    }

    customers[next_id] = customer
    next_id += 1

    return jsonify(customer),201

@app.route("/customers/<int:customer_id>",methods= ["GET"])
def get_customer(customer_id):
    customer= customers.get(customer_id)

    if not customer:
        return jsonify({"error": "Customer not found,"}),404

    return jsonify(customer),200

@app.route("/customers/<int:customer_id>",methods=["PUT"])
def update_customer(customer_id):
    customer = customers.get(customer_id)

    if not customer:
        return jsonify({"error": "Customer not  found."}),404

    data = request.json

    customer["email"]= data.get("email",customer["email"])

    return jsonify(customer),200

@app.route("/customers/<int:customer_id>",methods = ["DELETE"])
def delete_customer(customer_id):
    if customer_id not in customers:
        return jsonify({"error": "Customer not found"}),404

    del customers[customer_id]

    return "",204

if __name__ == "__main__":
    app.run(debug=True)
