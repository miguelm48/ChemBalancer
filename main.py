from flask import Flask, render_template, request
from chempy import balance_stoichiometry

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/balance", methods=["POST"])
def balance():
    equation = request.form["equation"]
    try:
        left, right = equation.split("->")
        balanced = balance_stoichiometry(
            {c.strip() for c in left.split("+")},
            {c.strip() for c in right.split("+")}
        )
        result = " + ".join(f"{v} {k}" for k, v in balanced[0].items()) + " → " + " + ".join(f"{v} {k}" for k, v in balanced[1].items())
        return render_template("index.html", equation=equation, balanced_equation=result)
    except Exception as e:
        return render_template("index.html", equation=equation, balanced_equation="Error balancing equation 😅")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=81)
