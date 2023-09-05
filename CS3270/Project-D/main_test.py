


"""Tests for the Customer Object"""
def customer_test(Customer):
    cust_id = "12345678"
    name = "John Jones"
    street = "1100S 15000W"
    city = "Orem" 
    state = "Utah"
    postal_code = "84569"
    phone = "435-568-5413"
    email = "JohnJones@gmail.com"

    try:
        Customer(cust_id, name, street, city, state, postal_code, phone, email)
        print("Customer_test: Passed")
    except TypeError as e:
        print("Cutomer_test: Failed")
        print(f" - {e}")


"""Tests for the Order Object"""
class Payment():
    pass
def order_test(order):
    order_id = "123456789"
    order_date = "11-12-2020"
    cust_id = "1111111"
    line_items = ["stuff", "stuff"]
    payment = Payment()

    try:
        order(order_id, order_date, cust_id, line_items, payment)
        print("order_test: Passed")
    except TypeError as e:
        print("order_test: Failed")
        print(f" - {e}")

"""Tests for the Payment Object"""
# def payment_test(payment):
    # amount = 1000.59
    # try:
    #     payment(amount)
    #     print("payment_test: Failed")
    # except:
    #     print("payment_test: Passed")

def paypal_test(paypal):
    paypal_id = "123456789"
    try:
        paypal(paypal_id)
        print("paypal_test: Passed")
    except TypeError as e:
        print("paypal_test: Failed")
        print(f" - {e}")

def wire_test(wire):
    bank_id = "123456789"
    account_id = "53248696"
    try:
        wire(bank_id, account_id)
        print("wire_test: Passed")
    except TypeError as e:
        print("wire_test: Failed")
        print(f" - {e}")

def credit_test(credit):
    card_number = "123456789"
    exp_date = "01/52"
    try:
        credit(card_number, exp_date)
        print("credit_test: Passed")
    except TypeError as e:
        print("credi_test: Failed")
        print("f - {e}")

def line_item_test(line_item):
    item_id = "456"
    qty = 5
    try:
        line_item(item_id, qty)
        print("line_item_test: Passed")
    except TypeError as e:
        print("line_item_test: Failed")
        print(f" - {e}")

def item_test(item):
    item_id = "123"
    description = "testing testing"
    price = 100.56
    try:
        item(item_id, description, price)
        print("item_test: Passed")
    except TypeError as e:
        print("item_test: Failed")
        print(f" - {e}")


def file_test(customer, item, order):
    try:
        customer.read_customer("customers.txt")
        print("customer_file_test: Passed")
    except OSError as e:
        print("customer_file_test: Failed")
        print(f" - {e}\ntry checking the Customer.read_customer method")

    try:
        item.read_items("items.txt")
        print("item_file_test: Passed")
    except OSError as e:
        print("item_file_test: Failed")
        print(f" - {e}\ntry checking the Item.read_item method")

    try:
        order.read_orders("orders.txt")
        print("order_file_test: Passed")
    except OSError as e:
        print("order_file_test: Failed")
        print(f" - {e}\ntry checking the Order.read_order method")

# def database_test(customer, orders, items):
#     customer_database = "810003,Kai Antonikov,31 Prairie Rose Street,Philadelphia,PA,19196,215-975-7421,kantonikov0@4shared.com"
#     orders_database = "762212,1,2020-03-15,10951-3,64612-2,57544-1,80145-1,27515-2,16736-1,79758-2,29286-2,51822-3,39096-1,32641-3,63725-3,64007-2,23022-1,16974-3,26860-2,75536-2,26461-1,373975319551257,12-2023" 
#     items_database = "57464,Almonds Ground Blanched,2.99"
#     try:
#         if str(customer["810003"]) == customer_database:
#             print("database_customer_test: Passed")
#         else:
#             print("database_customer_test: Failed")
#             print(f" - result should be: {customer_database} ")
#             print("   result was: ", end="")
#             print(customer["810003"])

#         if orders["1"] == orders_database:
#             print("database_orders_test: Passed")
#         else:
#             print("database_orders_test: Failed")
#             print(f" - result should be: {orders_database} ")
#             print("   result was: ", end="")
#             print(orders["1"])

#         if str(items["57464"]) == items_database:
#             print("database_items_test: Passed")
#         else:
#             print("database_items_test: Failed")
#             print(f" - result should be: {items_database} ")
#             print("   result was: ", end="")
#             print(items["57464"])
#     except TypeError as e:
#         print(e)
