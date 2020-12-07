from flask import Flask, render_template, request
import sqlite3

from settings.settings import Settings

settings = Settings()

app = Flask(__name__)


@app.route('/')
def list_categories():
    con = sqlite3.connect(settings.db_name)
    cur = con.cursor()

    query = f'SELECT name FROM category'
    category_query = cur.execute(query)

    category_list = []
    while True:
        result = category_query.fetchone()
        if not result:
            break
        category_list.append(result[0])
    print(category_list)

    return render_template('default.html', category_list=category_list)

    cur.close()
    con.close()


@app.route('/category/<string:category_name>')
def category(category_name):
    con = sqlite3.connect(settings.db_name)
    cur = con.cursor()
    category_id = cur.execute('SELECT id FROM category WHERE name=?', (category_name,)).fetchall()[0][0]
    products_query = cur.execute('SELECT * FROM product WHERE category_id=?', (category_id,)).fetchall()
    cur.close()
    return render_template('products_list.html', products=products_query)


@app.route('/product/<string:product_id>')
def product(product_id):
    con = sqlite3.connect(settings.db_name)
    cur = con.cursor()
    query = 'SELECT product.name, product.in_store, category.name, product.price FROM product ' \
        'LEFT JOIN category ON category.id=product.category_id WHERE product.id=?'
    product_query = cur.execute(query, (product_id,)).fetchall()[0]
    cur.close()
    return render_template('product.html', product=product_query)


@app.route('/admin/add_category', methods=['GET', 'POST'])
def add_category():
    if request.method == 'GET':
        return render_template('add_category.html')
    else:
        category = request.form['category']
        message = 'category already exists'

        con = sqlite3.connect(settings.db_name)
        cur = con.cursor()
        # return f'Category "{category}" added'
        cat_query = cur.execute('SELECT name FROM category WHERE name=?', (category,)).fetchall()
        if len(cat_query) == 0 and len(category) != 0:
            cur.execute('INSERT INTO category(name) VALUES(?)', (category,))
            con.commit()
            message = 'category added'

        cur.close()

        if len(category) == 0:
            message = 'category has a zero length'
        return render_template('category_added.html', category=category, message=message)


@app.route('/admin/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'GET':
        con = sqlite3.connect(settings.db_name)
        cur = con.cursor()
        query = 'SELECT name FROM category'
        categories_list_query = cur.execute(query).fetchall()
        cur.close()
        return render_template('add_product.html', categories=categories_list_query)
    else:
        con = sqlite3.connect(settings.db_name)
        cur = con.cursor()
        message = 'product already exists'
        product_name = request.form['product_name']
        category_name = request.form['category_name']
        in_store = request.form['in_store']
        product_price = request.form['product_price']

        query = 'SELECT * FROM product WHERE name=?'
        is_product_exists = cur.execute(query, (product_name,)).fetchall()

        if len(is_product_exists) == 0:
            if len(product_name) == 0:
                message = 'product has a zero length'
            elif len(product_price) == 0:
                message = 'price has a zero length'
            else:
                if in_store == 1:
                    in_store = True
                else:
                    in_store = False

                query = 'SELECT id FROM category WHERE name=?'
                category_id = cur.execute(query, (category_name,)).fetchall()[0][0]

                query = 'INSERT INTO product(name, in_store, category_id, price) ' \
                        'VALUES(?, ?, ?, ?)'
                cur.execute(query, (product_name, in_store, category_id, product_price))
                con.commit()
                message = f'product {product_name} added in category {category_name} with price {product_price}'

        cur.close()
        return render_template('product_added.html', message=message)


@app.route('/admin')
def admin_page():
    return render_template('admin.html')


app.run(debug=True)
