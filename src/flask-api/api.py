from flask import Flask, render_template, redirect, url_for, request, flash, session, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def login():
    url = 'https://5001-louihhi-univsmbflaskful-obxdyg3fi4i.ws-eu92.gitpod.io/'
    username = request.args.get('username')
    password = request.args.get('password')
    print(f"toto {username}")

    if username == 'admin' and password == 'admin':
        data = 'Connecté avec succès'
        return jsonify({'success': True, 'message': 'Connecté avec succès'})
    else:
        data = 'Nom d\'utilisateur ou mot de passe incorrect'
        return  jsonify({'success': False, 'message': 'Nom d\'utilisateur ou mot de passe incorrect}'})

if __name__ == '__main__':
    app.run()




