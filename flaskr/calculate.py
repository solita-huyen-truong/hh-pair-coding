from flask import Blueprint
from flask import request
from flask import render_template

bp = Blueprint("calculate", __name__, url_prefix="")

@bp.route("/register", methods=("POST"))
def register():
    if request.method == "POST":
        quantity = request.form["quantity"]
        unitPrice = request.form["unitPrice"]
        #db = get_db()
        error = None

        if not quantity:
            error = "Quantity is required."
        elif not unitPrice:
            error = "Unit price is required."
        
        
            
    return render_template("base.html")