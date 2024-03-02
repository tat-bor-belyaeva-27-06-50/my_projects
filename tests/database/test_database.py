import pytest
from modules.common.database import Database

# test_database_connection має мітку database
# в тілі тесту створюється екземпляр класу Database,
# в тілі тесту виконується метод об'єкта test_connection
@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()

# test_check_all_users має мітку database
# в тілі тесту створюється екземпляр класу Database,
# в тілі тесту виконується метод об'єкта get_all_users
# виводиться в термінал результат виконання методу об'єкта get_all_users
@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()

    print(users)

# test_check_user_sergii має мітку database
# в тілі тесту створюється екземпляр класу Database,
# в тілі тесту виконується метод об'єкта get_user_address_by_name зі значенням параметру name=Sergii
# перевіряється, що дані, які повернув метод get_user_address_by_name, відповідають даним:
# Maydan Nezalezhnosti 1, Kyiv, 3127, Ukraine
@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    users = db.get_user_address_by_name('Sergii')

    assert users[0][0] == 'Maydan Nezalezhnosti 1'
    assert users[0][1] == 'Kyiv'
    assert users[0][2] == '3127'
    assert users[0][3] == 'Ukraine'

# test_product_qnt_update має мітку database
# в тілі тесту створюється екземпляр класу Database,
# в тілі тесту виконується метод об'єкта update_product_qnt_by_id зі значенням параметрів product_id=1 
# та qnt=25
# перевіряється, що після оновлення даних кількість товару з унікальним номером 1 дорівнює 25
@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25

# test_product_insert має мітку database
# в тілі тесту створюється екземпляр класу Database,
# в тілі тесту виконується метод об'єкта insert_product зі значенням параметрів product_id=4, 
# name=печиво, description=солодке, qnt=30
# перевіряється, що після оновлення даних кількість товару з унікальним номером 4 дорівнює 30
@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, 'печиво', 'солодке', 30)
    water_qnt = db.select_product_qnt_by_id(4)

    assert water_qnt[0][0] == 30

# test_product_delete має мітку database
# в тілі тесту створюється екземпляр класу Database,
# в тілі тесту створюються тестові дані, створивши продукт в таблиці products зі значеннями параметрів
# product_id=99, name=тестові, description=дані, qnt=999
# в тілі тесту видаляється дані з таблички  products зі значеннями параметра product_id=99
# перевіряється, що кількість рядків, що було знайдено, дорівнює 0
@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, 'тестові', 'дані', 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0

# test_detailed_orders має мітку database
# в тілі тесту створюється екземпляр класу Database,
# в тілі тесту виводиться в термінал результат виконання методу get_detailed_orders об'єкта класу Database
# перевіряється, що кількість знайдених результатів дорівнює 1
# перевіряється, що дані, які повернув метод get_detailed_orders, відповідають даним: 
# 1, Sergii, солодка вода, з цукром
@pytest.mark.database
def test_detailed_orders():
    db = Database()
    orders = db.get_detailed_orders()
    print("Замовлення", orders)
    # Check quantity of orders equal to 1
    assert len(orders) == 1

    # Check struture of data
    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'
    assert orders[0][3] == 'з цукром'

#test_update_product_qnt_by_id_qnt_less_than_zero має мітку database
# в тілі тесту створюється екземпляр класу Database,
# в тілі тесту передається параметр -1 методу об'єкту update_product_qnt_by_id
# перевіряється, що метод update_product_qnt_by_id згенерує помилку
@pytest.mark.database
def test_update_product_qnt_by_id_qnt_less_than_zero():
    with pytest.raises(Exception):
        db = Database()
        db.update_product_qnt_by_id(-1)

# test_delete_product_by_id_delete_not_existing_product має мітку database
# в тілі тесту створюється екземпляр класу Database,
# в тілі тесту передається ідентифікатор неіснуючого продукту id=5 в метод delete_product_by_id
# перевіряється, що метод delete_product_by_id згенерує помилку
@pytest.mark.database
def test_delete_product_by_id_delete_not_existing_product():
    with pytest.raises(Exception):
        db = Database()
        db.delete_product_by_id(5)

# test_get_product_by_id_not_existing_id має мітку database
# в тілі тесту створюється екземпляр класу Database,
# в тілі тесту передається ідентифікатор неіснуючого продукту id=5 в метод get_product_by_id
# перевіряється, що кількість рядків, що було знайдено, дорівнює 0
@pytest.mark.database
def test_get_product_by_id_not_existing_id():
    db = Database()
    db.get_product_by_id(5)
    qnt = db.get_product_by_id(5)

    assert len(qnt) == 0

# test_order_insert_product_not_exists має мітку database
# в тілі тесту створюється екземпляр класу Database,
# в тілі тесту створюється замовлення на продукт, якого не існує в базі с id=-5
# перевіряється, що метод insert_order генерує помилку
@pytest.mark.database
def test_order_insert_product_not_exists():
    with pytest.raises(Exception):
        db = Database()
        db.insert_order(2, 1, -5, '10-10-23')

#DELETE from orders where id <> 1

# test_check_user_name_not_exists має мітку database
# в тілі тесту створюється екземпляр класу Database,
# в тілі тесту методу get_user_address_by_name передається ім'я неіснуючого користувача Mark
# перевіряється, що кількість рядків, що було знайдено, дорівнює 0
@pytest.mark.database
def test_check_user_name_not_exists():
        db = Database()
        qnt = db.get_user_address_by_name('Mark')

        assert len(qnt) == 0