// groceries_template.cpp: Stores Orders in a list.

#include <fstream>
#include <iostream>
#include <list>
#include <stdexcept>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>
//#include "split.h"
using namespace std;

//////////////////
// Customer code /
//////////////////
struct Customer {
    int cust_id;
    string name;
    string street;
    string city;
    string state;
    string zip;
    string phone;
    string email;
    Customer(int id, const string& name, const string& street, const string& city,
        const string& state, const string& zip, const string& phone, const string& email)
        : name(name), street(street), city(city), state(state), zip(zip), phone(phone), email(email)
    {
        cust_id = id;
    }
    string print_detail() const {
        string string_detail;
        string_detail = (
            "Customer ID #" + to_string(cust_id) + ":" +"\n"
            + name + ", ph. " + phone + ", " + "email: " + email + "\n"
            + street + "\n" + city + ", " + state + " " + zip + "\n"
            );
        return string_detail;
    }
};

vector<Customer> customers;
void read_customers(const string& fname) {
    ifstream customer_data;
    stringstream line_of_data;
    string piece_of_data;
    vector<string> customer;
    customer_data.open(fname);
    if (!customer_data.is_open()) {
        cout << "Failed to open file" << endl;
        return;
    }
    while (!customer_data.fail()) {
        getline(customer_data, piece_of_data);
        line_of_data.clear();
        line_of_data.str(piece_of_data);
        if (piece_of_data.empty()) {
        }
        else {
            while (!line_of_data.eof()) {
                getline(line_of_data, piece_of_data, ',');
                customer.push_back(piece_of_data);
            }
            customers.push_back(Customer(stoi(customer.at(0)),
                customer.at(1), customer.at(2), customer.at(3),
                customer.at(4), customer.at(5), customer.at(6), customer.at(7)));
            customer.clear();
        }
    }
    if (!customer_data.eof()) {
        cout << "Failed to read all of the data in the file" << endl;
        return;
    }
    customer_data.close();
}

int find_cust_idx(int cust_id) {
    for (int i = 0; i < customers.size(); ++i)
        if (cust_id == customers[i].cust_id)
            return i;
    throw runtime_error("Customer not found");
}

//////////////
// Item code /
//////////////
struct Item {
    int item_id;
    string description;
    double price;
    Item(int id, const string& desc, double pric) : description(desc) {
        item_id = id;
        price = pric;
    }

};

vector<Item> items;
void read_items(const string& fname) {
    ifstream item_data;
    stringstream line_of_data;
    string piece_of_data;
    vector<string> item_lyst;
    item_data.open(fname);
    if (!item_data.is_open()) {
        cout << "Failed to open file" << endl;
        return;
    }
    while (!item_data.fail()) {
        getline(item_data, piece_of_data);
        line_of_data.clear();
        line_of_data.str(piece_of_data);
        if (piece_of_data.empty()) {
        }
        else {
            while (!line_of_data.eof()) {
                getline(line_of_data, piece_of_data, ',');
                item_lyst.push_back(piece_of_data);
            }
            items.push_back(Item(stoi(item_lyst.at(0)), item_lyst.at(1), stod(item_lyst.at(2))));
            item_lyst.clear();
            item_data.clear();
        }
    }
    if (!item_data.eof()) {
        cout << "Failed to read all of the data in the file" << endl;
        return;
    }
    item_data.close();
   
}

int find_item_idx(int item_id) {
    for (int i = 0; i < items.size(); ++i)
        if (item_id == items[i].item_id)
            return i;
    throw runtime_error("Item not found");
}

class LineItem {
    int item_id;
    int qty;
    friend class Order;
public:
    LineItem(int id, int q) {
        item_id = id;
        qty = q;
    }
    double sub_total() const {
        int idx = find_item_idx(item_id);
        return items[idx].price * qty;
    }
    friend bool operator<(const LineItem& item1, const LineItem& item2) {
        return item1.item_id < item2.item_id;
    }
};

/////////////////
// Payment code /
/////////////////
class Payment {
    double amount = 0.0;
    friend class Order;
public:
    Payment() = default;
    virtual ~Payment() = default;
    virtual string print_detail() const = 0;
};

class Credit : public Payment {
    string card_number;
    string expiration;
public:
    Credit(string card_number_input, string expiration_input) {
        card_number = card_number_input;
        expiration = expiration_input;
        
    }
    string print_detail() const {
        string payment_info;
        payment_info = "Paid by Credit card " + card_number + ", exp. " + expiration;
        return payment_info;

    }
};

class Paypal : public Payment {
    string paypal_id;
public:
    Paypal(const string paypal_id_input) {
        paypal_id = paypal_id_input;
    }

    string print_detail() const {
        string payment_info;
        payment_info = "Paid by Paypal ID: " + paypal_id;
        return payment_info;

    }
};

class WireTransfer : public Payment {
    string bank_id;
    string account_id;
public:
    WireTransfer(const string bank_id_input, const string account_id_input) {
        bank_id = bank_id_input;
        account_id = account_id_input;
    }

    string print_detail() const {
        string payment_info;
        payment_info = "Paid by Wire transfer from Bank ID " + bank_id + ", Account# " + account_id;
        return payment_info;

    }
};

///////////////
// Order code /
///////////////
class Order {
    int order_id;
    string order_date;
    int cust_id;
    vector<LineItem> line_items;
    Payment* payment;
    double order_total = 0.0;
public:
    Order(int c_id, int id, const string& date, const vector<LineItem>& items,Payment* p)
        : order_date(date), line_items(items) {
        order_id = id;
        cust_id = c_id;
        payment = p;
        sort(line_items.begin(), line_items.end());
        for (auto i : line_items) {
            order_total += i.sub_total();
        }

    }
    ~Order() {
        delete payment;
    }
    double total() const {
        return order_total;
    }
    string print_detail() const {
        string string_detail;
        string order_string;

        order_string = to_string(order_total);
        order_string.erase(order_string.find_last_not_of('0') + 1, string::npos);
        string_detail = ("=========================== \nOrder # "
            + to_string(order_id) + ", Date: " + to_string(this->total()) + "\n"
            + "Amount: " + order_string + ", " + payment->print_detail() 
            + "\n" + customers[find_cust_idx(cust_id)].print_detail() + "\n"
            + "Order Detail: \n");
        for (auto i : line_items) {
            string str_price;
            str_price = to_string(items[find_item_idx(i.item_id)].price);
            str_price.erase(str_price.find_last_not_of('0') + 1, string::npos);
            string_detail += "\t Item " 
                + to_string(i.item_id) + ": \"" 
                + items[find_item_idx(i.item_id)].description 
                + "\", " + to_string(i.qty) 
                + " @ " + str_price + "\n";
        }
        return string_detail;
    }
};

list<Order> orders;

void read_orders(const string& fname) {
    ifstream orderf(fname);
    string line;
    string line2;
    vector<string> temp_order_lyst;
    vector<string> order_item;
    vector<string> payment_items;
    vector<LineItem> line_items;
    vector<Payment*> payment_lyst;
    stringstream line_of_data;
    stringstream item_data;
    stringstream payment_line;
    string item_temp;
    int order_id;
    string order_date;
    int cust_id;
    bool test;
    test = true;
    Payment* pmt;
    while (getline(orderf, line)) {
        line_of_data.str(line);
        line_of_data.clear();
        while (!line_of_data.eof()) {
            getline(line_of_data, line2, ',');
            temp_order_lyst.push_back(line2);
        }
        if (temp_order_lyst.empty() || test == false) {
            test = true;
            payment_line.str(line);
            payment_line.clear();
            while (!payment_line.eof()) {
                getline(payment_line, line, ',');
                payment_items.push_back(line);
            }
            if (stoi(payment_items[0]) == 1) {
                
                payment_lyst.push_back(new Credit(payment_items[1], payment_items[2]));
            }
            else if (stoi(payment_items[0]) == 2) {
                payment_lyst.push_back(new Paypal(payment_items[1]));

            }
            else if (stoi(payment_items[0]) == 3) {
                payment_lyst.push_back(new WireTransfer(payment_items[1], payment_items[2]));
            }
            else {
                cout << "Error";
            }
            payment_items.clear();
            temp_order_lyst.clear();
        }
        else {
            cust_id = stoi(temp_order_lyst[0]);
            order_id = stoi(temp_order_lyst[1]);
            order_date = temp_order_lyst[2];
            for (int i = 3; i < temp_order_lyst.size(); i++) {
                item_data.str(temp_order_lyst[i]);
                item_data.clear();
                while (!item_data.eof()) {
                    getline(item_data, item_temp, '-');
                    order_item.push_back(item_temp);
                }
                line_items.push_back(LineItem(stoi(order_item[0]), stoi(order_item[1])));
                order_item.clear();

            }
            temp_order_lyst.clear();
            test = false;
        }

        if (payment_lyst.empty()) {

        }
        else {
            pmt = payment_lyst[0];

            orders.emplace_back(cust_id, order_id, order_date, line_items, pmt);
            line_items.clear();
            payment_lyst.erase(payment_lyst.begin());


        }


    }
}

int main() {
    read_customers("customers.txt");
    read_items("items.txt");
    read_orders("orders.txt");

    ofstream ofs("order_report.txt");
    for (const Order& order : orders)
        ofs << order.print_detail() << endl;
}