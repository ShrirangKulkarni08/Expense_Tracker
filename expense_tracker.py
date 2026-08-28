from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Your original expense list
expense = []


# Open frontend
@app.route("/")
def home():
    return send_from_directory(".", "expense_console.html")


# VIEW EXPENSE
@app.route("/api/expenses", methods=["GET"])
def view_expenses():
    expenses = []

    for item in expense:
        expenses.append({
            "name": item[0],
            "amount": item[1]
        })

    return jsonify(expenses)


# ADD EXPENSE
@app.route("/api/expenses", methods=["POST"])
def add_expense():

    data = request.get_json()

    name = data.get("name")
    amount = data.get("amount")

    if not name or amount is None:
        return jsonify({
            "error": "Name and amount are required"
        }), 400

    # Same as your original:
    # expense.append([name, amount])
    expense.append([name, float(amount)])

    return jsonify({
        "message": "EXPENSE ADDED SUCCESSFULLY"
    }), 201


# TOTAL EXPENSE
@app.route("/api/total", methods=["GET"])
def total_expense():

    total = 0

    # Same logic as your original code
    for item in expense:
        total += item[1]

    return jsonify({
        "total": total
    })


# DELETE EXPENSE
@app.route("/api/expenses/<int:index>", methods=["DELETE"])
def delete_expense(index):

    if index < 0 or index >= len(expense):
        return jsonify({
            "error": "Expense not found"
        }), 404

    removed = expense.pop(index)

    return jsonify({
        "message": "Expense deleted successfully",
        "expense": {
            "name": removed[0],
            "amount": removed[1]
        }
    })


if __name__ == "__main__":
    app.run(debug=True)