from flask import Flask 
from flask import request
from flask import render_template

app = Flask(__name__)

total_without_tax = 0
@app.route("/")
def calculator():
    #if request.method == "POST":
    #    quantity = request.form["quantity"]
    #    unitPrice = request.form["unitPrice"]
        #db = get_db()
        #error = None

        #if not quantity:
        #    error = "Quantity is required."
        #elif not unitPrice:
        #    error = "Unit price is required."

        # calculate the total amount of the product = quantity * unitPrice
    #    total_without_tax = quantity * unitPrice 
    return render_template("base.html")

if __name__ == '__main__':
   app.run()