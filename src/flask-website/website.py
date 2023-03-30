from flask import Flask, render_template, redirect, url_for, request, flash, session, jsonify

import requests


app = Flask(__name__)

app.secret_key='toto:tata'



@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' :
        url = 'http://localhost:5000/'
        username = request.form['username']
        password = request.form['password']
        data = {'username': username, 'password': password}

    

        response = requests.get(url, params=data)
        if response.text == "ok":
            session['username'] = username
            return redirect(url_for('layout'))
        else: 
            return redirect('/')

        
        


    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=password name=password>
            <p><input type=submit value=Login>
        </form>
        '''

@app.route('/start')
def start():
    if 'username' in session:
        
        return render_template('start.html')
    else:
        return redirect(url_for('login'))
    
    

@app.route('/layout', methods=['GET', 'POST'])
def layout():
    if 'username' in session:
        url = 'http://localhost:5000/users'
        data = {"users":"all"}
        response = requests.get(url, params=data)
        datas = response.json()
        print(type(datas))
        return render_template('layout.html', datas=datas)
    else:
        return redirect(url_for('login'))
    

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))
    
    
if __name__ == '__main__':
    app.run(debug=True)

