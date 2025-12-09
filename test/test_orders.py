from orders import process_orders

def test_product_not_in_inventory():
    orders = [{"product": "apple", "quantity": 2}]
    inventory = {"banana": 10}

    try:
        process_orders(orders, inventory)
        assert False 
    except ValueError as e:
        assert str(e) == "Product 'apple' not found in inventory"
def test_not_enough_quantity():
    orders = [{"product": "apple", "quantity": 10}]
    inventory = {"apple": 5}

    try:
        process_orders(orders, inventory)
        assert False
    except ValueError as e:
        assert str(e) == "Not enough stock for 'apple'"
        
def test_successful_order_reduces_inventory():
    orders = [{"product": "apple", "quantity": 3}]
    inventory = {"apple": 10}
    result = process_orders(orders, inventory)
    assert result == [{"product": "apple", "quantity": 3}]
    assert inventory["apple"] == 7
