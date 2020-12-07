import sqlite3


class Settings:
    def __init__(self):
        self.db_name = 'warehouse.db'

        self.category_table = """
            CREATE TABLE IF NOT EXISTS category(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            )
        """

        self.product_table = """
            CREATE TABLE IF NOT EXISTS product(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                in_store BOOL NOT NULL,
                category_id INTEGER NOT NULL,
                price INTEGER NOT NULL,
                FOREIGN KEY(category_id) REFERENCES category(id)
            )
        """

        self.categories = {
            'general': [
                ['apple', True, 150],
                ['banana', True, 200],
                ['raspberry', False, 220]
            ],
            'voter': [
                ['bonaqua', True, 10],
                ['pepsi', True, 20],
                ['Cocacola', False, 30]
            ],
            'other': [
                ['chocolat', True, 200],
                ['spice', True, 300]
            ]
        }

    def install_db(self):
        con = sqlite3.connect(self.db_name)
        cur = con.cursor()

        cur.execute(self.category_table)
        cur.execute(self.product_table)

        for category in self.categories.keys():
            query = 'SELECT * FROM category WHERE name=?'
            is_category_exists = cur.execute(query, (category,)).fetchall()
            if len(is_category_exists) == 0:
                query = 'INSERT INTO category(name) VALUES(?)'
                cur.execute(query, (category,))
                query = 'SELECT id FROM category WHERE name=?'
            # print(f'category:{category} len({len(is_category_exists)})')

            category_id = cur.execute(query, (category,)).fetchall()[0][0]
            # print(f'category:{category}; category_id:{category_id}')
            for products in self.categories[category]:
                product_name, product_in_store, product_price = products

                query = 'SELECT * FROM product WHERE name=?'
                is_product_exists = cur.execute(query, (product_name,)).fetchall()
                if len(is_product_exists) == 0:
                    query = 'INSERT INTO product(name, in_store, category_id, price) '\
                        'VALUES(?, ?, ?, ?)'
                    cur.execute(query, (product_name, product_in_store, category_id, product_price))

        con.commit()
        cur.close()
        con.close()


Settings().install_db()