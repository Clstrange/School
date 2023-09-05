"""
    Cody Strange
    11/10/2022
    CS3270-001
    Programming project D

    Summary:
            This program will print a report of online orders
            from a fictional grocery chain using data from customers.txt, orders.txt, and items.txt

            Report:
                - <Order #>, <date>
                - <Amount>, <method of >
                - <Customer ID>
                - <Name>, <phone-number>, <email>
                - <Address>
                - <City>, <State> <zip-code>
                - Order Detail:
                    <Item #>: <"item">, <quantity> @ <price>

    Bugs:
        - none found

    Required features:
        - none remaining

    Recomended features
        - create more test cases for remaining code
        - create multiple files to hold the code
"""

class Customer():
    """Customer Object
            fields
                cust_id:string
                name:string
                street:string
                city:string
                state:string
                postal_code:string
                phone:string
                email:string
            Methods:
                __init__(...)
                __str__():string
                read_customers(fname:string) 
    """
    def __init__(self, cust_id, name, street, city, state, postal_code, phone, email):
        self.cust_id = cust_id
        self.name = name
        self.street = street
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.phone = phone
        self.email = email

    def __str__(self):
        customer_string = f"{self.cust_id},{self.name},{self.street},{self.city},{self.state},{self.postal_code},{self.phone},{self.email}"
        return customer_string
    
    @staticmethod
    def read_customer(fname):
        with open(fname, 'r') as file:
            return file.readlines()

class Order():
    """Order Object
            fields
                order_id:string
                order_date:string
                cust_id:string
                line_items:list
                payment:Payment
            Methods:
                __str__():string
                total:float(@property)
                read_orders(fname:string)
    """
    def __init__(self, cust_id, order_id, order_date, line_items, payment):
        self.cust_id = cust_id
        self.order_id = order_id
        self.order_date = order_date
        self.line_items = line_items
        self.payment = payment
    @property
    def total():
        pass
    @staticmethod
    def read_orders(fname):
        with open(fname, 'r') as file:
            return file.readlines()
    def __str__(self):
        line_items_string = ""
        for i in self.line_items : line_items_string += f"{i},"
        order_string = f"{self.cust_id},{self.order_id},{self.order_date},{line_items_string}{self.payment}"
        return order_string

class PayPal():
    """PayPal Object
            fields
                paypal_id:string
            methods
                __str__():string
    """
    def __init__(self, paypal_id):
        super().__init__()
        self.paypal_id = paypal_id

    def __str__(self):
        paypal_string = f"{self.paypal_id}"
        return paypal_string

class Wire():
    """Wire Object
        fields
            bank_id:string
            account_id:string
        methods
            __str__():string
    """
    def __init__(self, bank_id, account_id):
        super().__init__()
        self.bank_id = bank_id
        self.account_id = account_id
    def __str__(self):
        wire_string = f"{self.bank_id},{self.account_id}"
        return wire_string

class Credit():
    """Credit Object
            fields
                card_number:string
                exp_date:string
            methods
                __str__():string
    """
    def __init__(self, card_number, exp_date):
        super().__init__()
        self.card_number = card_number
        self.exp_date = exp_date
    def __str__(self):
        credit_string = f"{self.card_number},{self.exp_date}"
        return credit_string

class LineItem():
    """LineItem Object
            fields
                item_id:string
                qty:int
            methods
                sub_total():float
    """
    def __init__(self, item_id, qty):
        self.item_id = item_id
        self.qty = qty
    def sub_total(self):
        line_item_string = f"{self.item_id},{self.qty}"
        return line_item_string

class Item():
    """Item Object
        fields
            item_id:string
            description:string
            price:float
        methods
            read_items(fname:string)
    """
    def __init__(self, item_id, description, price):
        self.item_id = item_id
        self.description = description
        self.price = price
    @staticmethod
    def read_items(fname):
        with open(fname, 'r') as file:
            return file.readlines()
    def __str__(self):
        item_string = f"{self.item_id},{self.description},{self.price}"
        return item_string

def line_items(order_data):
    return order_data[3:]

def customer_database(customer_file):
    customers = {}
    for customer in customer_file:
        customer_data = customer.strip().split(',')
        cid = customer_data[0]
        cname = customer_data[1]
        cstreet = customer_data[2]
        ccity = customer_data[3]
        cstate = customer_data[4]
        cpostal_code = customer_data[5]
        cphone = customer_data[6]
        cemail = customer_data[7]
        customers[cid] = Customer(cid, cname, cstreet, ccity, cstate, cpostal_code, cphone, cemail)
    return customers

def order_database(orders_file):
    order = {}
    order_lyst = [x for x in orders_file if orders_file.index(x) % 2 == 0]
    opayment_lyst = [x for x in orders_file if orders_file.index(x) % 2 != 0]
    for opayment_line, order_line in zip(opayment_lyst, order_lyst):
        opayment_file = opayment_line.strip().split(',')
        opay_type = opayment_file[0]
        if opay_type == '1':
            ocredit_num = opayment_file[1]
            ocredit_expir = opayment_file[2]
            opayment = Credit(ocredit_num, ocredit_expir)
        elif opay_type == '2':
            opay_id = opayment_file[1]
            opayment = PayPal(opay_id)
        else:
            opay_bank = opayment_file[1]
            opay_account = opayment_file[2]
            opayment = Wire(opay_bank, opay_account)
        order_data = order_line.strip().split(',')
        ocid = order_data[0]       
        oid = order_data[1]
        odate = order_data[2]
        oline_items = line_items(order_data)
        order[oid] = Order(ocid, oid, odate, oline_items, opayment)
    return order

def items_database(items_file):
    items = {}
    for line in items_file:
        items_data = line.strip().split(',')
        iid = items_data[0]
        idescription = items_data[1]
        iprice = items_data[2]
        items[iid] = Item(iid, idescription, iprice)
    return items

def calc_total_amount(line_items, items):
    total = 0
    item_list = {}
    for item in line_items:
        item = item.split('-')
        item_list[item[0]] = LineItem(item[0], item[1])
    for id in item_list:
        item_price = float(items[id].price)
        item_qty = int(item_list[id].qty)
        total += (item_qty * item_price)
    return "{:.2f}".format(total)

def find_payment_info(payment):
    if isinstance(payment,PayPal):
        return f"Paid by PayPal ID: {payment.paypal_id}"
    elif isinstance(payment,Credit):
        return f"Paid by Credit card {payment.card_number}, exp. {payment.exp_date}"
    elif isinstance(payment,Wire):
        return f"Paid by Wire transfer from Bank ID {payment.bank_id}, Account# {payment.account_id}"
    else:
        return "FAILED"

def order_detail_page(line_items, items):
    order_detail_list = []
    item_list = {}
    for item in line_items:
        item = item.split('-')
        item_list[item[0]] = LineItem(item[0], item[1])
    for id in item_list:
        item_price = float(items[id].price)
        item_qty = int(item_list[id].qty)
        item_description = items[id].description
        order_detail_list.append(f'Item {id}: "{item_description}", {item_qty}, @ {item_price:.2f}')
    return order_detail_list

def main():
    orders = order_database(orders_file)
    items = items_database(items_file)
    customers = customer_database(customer_file)
    for order in orders:
        order_id = orders[order].order_id
        order_date = orders[order].order_date
        cust_id = orders[order].cust_id
        total_amount = calc_total_amount(orders[order].line_items, items)
        payment_information = find_payment_info(orders[order].payment)
        cust_name = customers[cust_id].name
        cust_phone = customers[cust_id].phone
        cust_email = customers[cust_id].email
        cust_street = customers[cust_id].street
        cust_city = customers[cust_id].city
        cust_state = customers[cust_id].state
        cust_postal_code = customers[cust_id].postal_code
        order_item_list = order_detail_page(orders[order].line_items, items)
        print(f"""==========================
Order#{order_id}, Date: {order_date}
Amount: ${total_amount}, {payment_information}

Customer ID #{cust_id}:
{cust_name}, ph. {cust_phone}, email: {cust_email}
{cust_street}
{cust_city}, {cust_state} {cust_postal_code}

Order Detail:""")

        for order_detail in order_item_list:
            print(f"\t{order_detail}")



if __name__ == '__main__':
 
    customer_file = Customer.read_customer("customers.txt")
    items_file = Item.read_items("items.txt")
    orders_file = Order.read_orders("orders.txt")
    main()


