import pytest
from modules.common.database import Database

@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_connection()

@pytest.mark.database
def test_check_all_users():
    db = Database()
    users = db.get_all_users()

    print(users)

@pytest.mark.database
def test_check_user_sergii():
    db = Database()
    users = db.get_user_address_by_name('Sergii')

    assert users[0][0] == 'Maydan Nezalezhnosti 1'
    assert users[0][1] == 'Kyiv'
    assert users[0][2] == '3127'
    assert users[0][3] == 'Ukraine'

@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    db.update_product_qnt_by_id(1, 25)
    water_qnt = db.select_product_qnt_by_id(1)

    assert water_qnt[0][0] == 25

@pytest.mark.database
def test_product_insert():
    db = Database()
    db.insert_product(4, 'печиво', 'солодке', 30)
    water_qnt = db.select_product_qnt_by_id(4)

    assert water_qnt[0][0] == 30

@pytest.mark.database
def test_product_delete():
    db = Database()
    db.insert_product(99, 'тестові', 'дані', 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)

    assert len(qnt) == 0

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

@pytest.mark.database
def test_update_product_qnt_by_id_qnt_less_than_zero():
    with pytest.raises(Exception):
        db = Database()
        db.update_product_qnt_by_id(-1)

@pytest.mark.database
def test_delete_product_by_id_delete_not_existing_product():
    with pytest.raises(Exception):
        db = Database()
        db.delete_product_by_id(5)

@pytest.mark.database
def test_get_product_by_id_not_existing_id():
    db = Database()
    db.get_product_by_id(5)
    qnt = db.get_product_by_id(5)

    assert len(qnt) == 0

@pytest.mark.database
def test_order_insert_product_not_exists():
    with pytest.raises(Exception):
        db = Database()
        db.insert_order(2, 1, -5, '10-10-23')

#DELETE from orders where id <> 1

@pytest.mark.database
def test_check_user_name_not_exists():
        db = Database()
        qnt = db.get_user_address_by_name('Mark')

        assert len(qnt) == 0