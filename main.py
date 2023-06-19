from flask import Flask, render_template, url_for, request
from customer_database import *
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        cust_name = request.form["name"]
        cust_lastname = request.form["lastname"]
        cust_mail = request.form["mail"]
        cust_phone = request.form["phone"]
        info_list = [cust_name, cust_lastname, cust_mail, cust_phone]
        not_empty = True
        for item in info_list:
            if item == "":
                not_empty = False
        if not_empty:
            new_customer = Customer(cust_name, cust_lastname, cust_mail, cust_phone)
            insert_customer(new_customer)
            return render_template("home.html")
        else:
            return "<h1>Empty Field Error</h1>"
    else:
        return render_template("home.html")

@app.route("/product")
def product():
    return render_template("product.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)