# Import libraries
from flask import Flask
import request, url_for, redirect, render_template

# Instantiate Flask functionality
app = Flask(__name__)

# Sample data
# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

# Read operation
@app.route('/')
def get_transactions():
    return render_template('transactions.html', transactions = transactions)

# Create operation
@app.route('/add', methods=['GET','POST'])
def add_transaction():
    if request.method == 'POST':
        transaction = {
              'id': len(transactions)+1,
              'date': request.form['date'],
              'amount': float(request.form['amount'])
        }

        transactions.append(transaction)
        return redirect(url_for('get_transactions'))
    return render_template('form.html')

# Update operation
@app.route('/edit/<int:transaction_id>', methods=['GET','POST'])
def edit_transaction(transaction_id):
    if request.method == 'POST':
        date = request.form['date']
        amount = float(request.form['amount'])

        for transaction in transactions:
            if transaction['id'] == transaction_id:
                transaction['date'] == date
                transaction['amount'] == amount
                break
        return redirect(url_for('get_transactions'))
    
    for transaction in transactions:
            if transaction['id'] == transaction_id:
                return render_template('edit.html', transaction=transaction)

    return {'message': 'Transaction not found'}

# Delete operation
# Delete operation: Delete a transaction
# Route to handle the deletion of an existing transaction
@app.route("/delete/<int:transaction_id>")
def delete_transaction(transaction_id):
    # Find the transaction with the matching ID and remove it from the list
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            transactions.remove(transaction)  # Remove the transaction from the transactions list
            break  # Exit the loop once the transaction is found and removed

    # Redirect to the transactions list page after deleting the transaction
    return redirect(url_for("get_transactions"))
# Run the Flask app
# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)