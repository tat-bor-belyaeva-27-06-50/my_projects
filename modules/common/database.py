import sqlite3


class Database():

# в конструкторі класу ініціалізовані 2 атрибути об'єкта:
# 1-self.connection-об'єкт, який реалізує з'єднання з базою даних
# 2-self.cursor-курсор об'єкта self.connection
    def __init__(self):
        self.connection = sqlite3.connect(r'D:\\Repository\\my_projects\\become_qa_auto.db')
        self.cursor = self.connection.cursor()

# метод об'єкта test_connection виконує SQL-запит SELECT sqlite_version(),
# результатом виконання методу є виведена в термінал версія бази даних
    def test_connection(self):
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        print(f"Connected successfully. SQLite Database Version is: {record}")

# метод об'єкта get_all_users має повернути із таблиці customers значення полів name, address, city
# для всіх користувачів
    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

# метод об'єкта get_user_address_by_name має обов'язковий параметр name,
# метод має повернути із таблиці customers значення полів address, city, postalCode, country для
# користувача з іменем  name 
    def get_user_address_by_name(self, name):
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

# метод об'єкта update_product_qnt_by_id має обов'язкові параметри product_id, qnt,
# метод має змінити кількість товару за вказаним в параметрі product_id унікальним значенням в
# таблиці  products на значення вказаного в параметрі qnt
    def update_product_qnt_by_id(self, product_id, qnt):
        if qnt < 0:
            raise Exception("Quantity should be more than 0.")
        query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

# метод об'єкта select_product_qnt_by_id має обов'язковий параметр product_id,
# метод має повернути кількість товару за вказаним в параметрі product_id унікальним значенням із
# таблиці  products
    def select_product_qnt_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

# метод об'єкта insert_product має обов'язкові параметри product_id, name, description, qnt
# метод має вставити або замінити дані в таблиці products для колонок id, name, description, quantity
# дані взяти з параметрів  product_id, name, description, qnt
    def insert_product(self, product_id, name, description, qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
            VALUES ({product_id}, '{name}', '{description}', {qnt})"
        self.cursor.execute(query)
        self.connection.commit()

# метод об'єкта delete_product_by_id має обов'язковий параметр product_id, 
# метод має видалити товар за вказаним в параметрі product_id унікальним значенням із таблиці products 
    def delete_product_by_id(self, product_id):
        query = f"SELECT * FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        existingProduct = self.cursor.fetchall()
        if len(existingProduct) == 0:
            raise Exception(f"Can't find the product with id {product_id}")
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

# метод об'єкта get_detailed_orders, використовуючи оператор JOIN та таблиці orders, customers, 
# products, має повернути наступну інформацію у відповідному порядку: унікальний
# номер замовлення, ім'я покупця, ім'я замовленого продукту, опис замовленого продукту, дату замовлення 
    def get_detailed_orders(self):
        query = "SELECT orders.id, customers.name, products.name, \
                products.description, orders.order_date \
                FROM orders \
                JOIN customers ON orders.customer_id = customers.id \
                JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
# метод об'єкта get_product_by_id намагається отримати продукт
# з ідентифікаторм, який дорівнює product_id
# метод об'єкта get_product_by_id повертає отриманий продукт
    def get_product_by_id(self, product_id):
        query = f"SELECT * FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        
        return record

# метод об'єкта insert_order додає замовлення в таблицю orders
    def insert_order(self, orders_id, customer_id, product_id, order_date):
        query = f"INSERT INTO orders (id, customer_id, product_id, order_date) \
            VALUES ({orders_id}, '{customer_id}', '{product_id}', {order_date})"
        self.cursor.execute(query)
        self.connection.commit()
    
    