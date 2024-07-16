from flask import Flask, render_template
from flask import request
import sqlite3
import json
import csv

app = Flask(__name__)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open('items.json') as f:
        data = json.load(f)
    items = data.get("items", [])

    return render_template('items.html', items=items)

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    if source == 'json':
        with open('items.json', 'r') as file:
            products = json.load(file)

    elif source == 'csv':
        products = []
        with open('products.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
        
    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id:
        filtered_products = []
        for product in products:
            if product['id'] == product_id:
                filtered_products.append(product)
       
        if not filtered_products:
            return render_template('product_display.html', error="Product not found")
        else:
            products = filtered_products

    return render_template('product_display.html', products=products)
@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    if source == 'json':
        with open('products.json', 'r') as file:
            products = json.load(file)

    elif source == 'csv':
        products = []
        with open('products.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
        
    elif source == 'sql':
        connection = sqlite3.connect('products.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM products')
        products = cursor.fetchall()
        cursor.close()
        connection.close()
        products = [{'id': row[0], 'name': row[1], 'price': row[2]} for row in products]

    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id:
        filtered_products = []
        for product in products:
            if product['id'] == product_id:
                filtered_products.append(product)
       
        if not filtered_products:
            return render_template('product_display.html', error="Product not found")
        else:
            products = filtered_products

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)