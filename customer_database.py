import sqlite3
from cust_class import Customer

conn = sqlite3.connect("customers.db", check_same_thread=False)

c = conn.cursor()

#3 functions
def insert_customer(cust):
    with conn:
        c.execute("INSERT INTO customers VALUES (:first, :last, :mail, :phone)",
                  {"first": cust.first, "last": cust.last, "mail": cust.mail,
                   "phone": cust.phone})

def get_cust_by_name(lastname):
    c.execute("SELECT * FROM customers WHERE last=:last", {'last': lastname})
    return c.fetchall()

def update_phone(cust, new_number):
    with conn:
        c.execute("""UPDATE customers SET phone = :phone WHERE first= :first AND last= :last""",
                  {'first': cust.first, 'last': cust.last, 'phone': new_number})

def remove_cust(cust):
    with conn:
        c.execute("DELETE from customers WHERE first = :first AND last = :last",
                  {"first": cust.first, "last": cust.last})


if __name__ == "__main__":
    c.execute("""CREATE TABLE customers (
                first text,
                last text,
                email text,
                phone text
                )""")
