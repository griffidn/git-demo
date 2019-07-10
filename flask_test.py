from flask import Flask, redirect, render_template, request, session  # , flash, abort
from dbconn.dbconn import db2conn

# import ibm_db_dbi as dbi

# Test comment for git branch
app = Flask(__name__)
@app.route('/HelloWorld')
def hello_world():
    # show the user profile for that user
    return 'Hello World!<br/><a href="/">Reset</a><br/>'


@app.errorhandler(404)
@app.route('/')
@app.route('/user/<username>')
@app.route('/<wild1>/user/<username>')
@app.route('/<wild1>/<wild2>/user/<username>')
@app.route('/<wild1>/<wild2>/<wild3>/user/<username>')
@app.route('/<wild1>/<wild2>/<wild3>/<wild4>/user/<username>')
@app.route('/<wild1>/<wild2>/<wild3>/<wild4>/<wild5>/user/<username>')
def show_user_profile(**kwargs):
    # show the user profile for that user
    othervar = request.args.get('username')

    if othervar is not None:
        name = othervar
    elif 'username' in kwargs:
        name = kwargs['username']
    else:
        name = 'Please add "/user/*your username*" to the web address to display your username'
    return render_template('index.html', name=name)


@app.route('/formAddSupply')
def form_add_supply():
    if 'user' not in session:
        return redirect("/login")
    return render_template('formAddSupply.html')


@app.route('/addSupply', methods=['POST'])
def add_supply():
    # read the posted values from the UI
    supply_name = request.form['supply_name']
    supply_brand = request.form['supply_brand']
    supply_type = request.form['supply_type']

    try:
        cost = int(request.form['cost'])
    except ValueError:
        cost = -1

    if request.form['in_stock'] == 'I':
        in_stock = 'IN STOCK'
    else:
        in_stock = 'OUT OF STOCK'

    errors = {}
    if supply_name == '':
        errors['supply_name'] = 'Please enter a value for supply name'
    if supply_brand == '':
        errors['supply_brand'] = 'Please enter a value for supply brand'
    if int(cost) < 0:
        errors['cost'] = 'Please enter a number greater than zero for cost'

    if not errors:
        c1, conn = db2conn()
        cur = conn.cursor()
        sql = """INSERT INTO DGRIFFITH/SUPPLIES (supply_brand, supply_type)
              values(?, ?)
              """
        cur.execute(sql, (supply_brand, supply_type))
        return render_template('addSupply.html', supply_name=supply_name, supply_brand=supply_brand, supply_type=supply_type, in_stock=in_stock)
    else:
        return render_template('formAddSupply.html', errors=errors)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        username = request.form['username']
        # password = request.form['password']
        session['user'] = username

        return redirect("/formAddSupply")
    else:
        return render_template('login.html')


@app.route('/sqltest', methods=['GET', 'POST'])
def sql_test():
    # show the user profile for that user
    if request.method == 'POST':
        if request.form['table'] != '':
            file = request.form['table']
        else:
            file = 'dgriffith/ngtsav0'
    else:
        file = 'dgriffith/ngtsav0'

    c1, conn = db2conn()
    cur = conn.cursor()

    cur.execute(f"select * from {file}")
    d = cur.description
    print(d[0][0])  # column name
    sql = list(cur)
    return render_template('sqlTable.html', header=d, sql=sql)


if __name__ == "__main__":
    app.secret_key = 'cutcokey'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(host='0.0.0.0', debug=False, port=9108)  # where xxxx is your port number
