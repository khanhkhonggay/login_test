from flask import Flask , redirect , url_for , json , render_template

from flask_sqlalchemy import SQLAlchemy


app = Flask(static_folder='static' , template_folder='templates')


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@login_test/khanhcuto'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)



##### OOP ####

class User(db.Model):
    
    id = db.Column(db.Integer , primary_key = True)
    
    username = db.Column(db.String(50) , nullable = False)
    
    password = db.Column(db.String(50) , nullable = False)
    
    def __init__ (self,user, password):
        
        self.username = username
        
        self.password = password
    

    


@app.route('/' , methods = ['GET' , 'POST'])
def Login():
    
    return render_template('login.html')
    











###################################


if __name__ == 'main':
    
    app.run(debug=True , host='127.0.0.1' , port=5000)