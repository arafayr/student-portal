import json
from flask import Flask, request, jsonify,render_template
app=Flask(__name__)
with open("students.json") as f:
    data = json.load(f)
    @app.route('/home',methods=['GET','POST'])
    def index():
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']
            for i in data['Students']:
                if i['Email'] == email and i['Password'] == password:
                    return render_template('index.html',data=data["Students"],email=email,password=password)
        return render_template('index.html',data=data)
    @app.route('/')
    @app.route('/login',methods=['GET','POST'])
    def login():
        
        return render_template('login.html')


app.run(debug=True)