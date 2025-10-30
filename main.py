from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/balance', methods=['POST'])
def balance():
    equation = request.form['equation']
    balanced_equation = balance_equation(equation)
    return render_template('index.html', balanced_equation=balanced_equation, equation=equation)

def balance_equation(equation):
    try:
        from chempy import balance_stoichiometry
        left_side, right_side = equation.split('->')
        left = [x.strip() for x in left_side.split('+')]
        right = [x.strip() for x in right_side.split('+')]
        react, prod = balance_stoichiometry(left, right)
        left_balanced = ' + '.join([f'{react[c]} {c}' for c in react])
        right_balanced = ' + '.join([f'{prod[c]} {c}' for c in prod])
        return f'{left_balanced} -> {right_balanced}'
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)
