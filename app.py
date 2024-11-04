from flask import Flask, render_template, request, redirect, url_for
import csv

app = Flask(__name__)

# Load items from items.csv
def load_items():
    items = []
    with open('items.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            items.append({
                'name': row['name'],
                'image_path': row['image_path'],
                'price': float(row['price'])
            })
    return items

# Load customers from customers.csv
def load_customers():
    customers = []
    with open('customers.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            customers.append({
                'name': row['name'],
                'email': row['email'],
                'phone': row['phone']
            })
    return customers

# Load orders from orders.csv
def load_orders():
    orders = []
    with open('orders.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            orders.append({
                'order_id': int(row['order_id']),
                'customer_name': row['customer_name'],
                'item_name': row['item_name']
            })
    return orders

# Save an order to orders.csv
def save_order(order_id, customer_name, item_name):
    with open('orders.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([order_id, customer_name, item_name])

# Route for home page (Items)
@app.route('/')
@app.route('/items')
def items():
    items = load_items()
    return render_template('items.html', items=items)

# Route for customers page
@app.route('/customers')
def customers():
    customers = load_customers()
    return render_template('customers.html', customers=customers)

@app.route('/orders')
def orders():
    orders = load_orders()  
    return render_template('orders.html', orders=orders)


# Route to place an order
@app.route('/order', methods=['POST'])
def order():
    order_id = len(load_orders()) + 1
    customer_name = request.form.get('customer_name')
    item_name = request.form.get('item_name')
    save_order(order_id, customer_name, item_name)
    return redirect(url_for('orders'))

if __name__ == '__main__':
    app.run(debug=True)
