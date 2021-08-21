from flask import Flask , redirect , url_for , json , render_template , request

from flask_sqlalchemy import SQLAlchemy

from flaskext.mysql import MySQL

import pymysql


app = Flask(__name__ , static_folder='static' , template_folder='templates')


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/khanhcuto'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



##### OOP ####

class User(db.Model):
    
    id = db.Column(db.Integer , primary_key = True)
    
    username = db.Column(db.String(50) , nullable = False)
    
    password = db.Column(db.String(50) , nullable = False)
    
    def __init__ (self,username, password):
        
        self.username = username
        
        self.password = password
    

    


@app.route('/' , methods = ['GET' , 'POST'])
def Login():
    
    if request.method == "POST":
        
        username = request.form['username']
        
        password = request.form['password']
        
        user = User.query.filter_by(username = username , password = password).first()
        
        if user:
            
            return "You Have Been Login"
        
        if not user:
            
            return "You Not Create Account Yet"
        
    if request.method == "GET":
    
        return render_template('login.html')
    
    
@app.route('/Register' , methods = ['GET' , 'POST'])
def Register():
    
    return render_template('register.html')
    










######################################


if __name__ == '__main__':
    
    app.run(host='127.0.0.1' , port=5000 , debug=True)