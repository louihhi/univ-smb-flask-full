from flask import Flask, render_template, redirect, url_for, request, flash, session, jsonify
from flask_mysqldb import MySQL
import requests
from flask_mysqldb import MySQL

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'louis'
app.config['MYSQL_PASSWORD'] = 'louis'
app.config['MYSQL_DB'] = 'identity'
mysql = MySQL(app)

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' :
        url = 'http://localhost:5000/'
        username = request.form['username']
        password = request.form['password']
        data = {'username': username, 'password': password}

        #cur = mysql.connection.cursor()
        #cur.execute("SELECT motdepasse FROM auth WHERE user="+username + ";")
        #rows = cur.fetchall()

        response = requests.get(url, params=data)
        # Traitez la réponse de la requête ici
        print(response)
        return response.json()
        

    # Le code suivant est exécuté si la méthode de requête est GET
    #return render_template('start.html')
        

    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=password name=password>
            <p><input type=submit value=Login>
        </form>
        '''

if __name__ == '__main__':
    app.run(debug=True)