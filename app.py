from flask import Flask,render_template,request,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY']='jhsijhgkjnjhuihIUAHENGFKJNKLAO859'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'

db= SQLAlchemy(app)

class Education(db.Model):
        id = db.Column(db.Integer,primary_key=True)
        school_name=db.Column(db.String(100),unique=True,nullable=False)
        duration=db.Column(db.String(20),nullable=False,default='Currently Schooling Here')
        degree=db.Column(db.String(50),nullable=False,default='Bachelors Degree')


        def __repr__(self):
            return self.school_name

class WorkExperience(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    role=db.Column(db.String(100),unique=True,nullable=False)
    duration=db.Column(db.String(20),nullable=False,default='Currently Works Here')
    details=db.Column(db.String(2000),nullable=False)

    def __repr__(self):
        return self.role


class Skills(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),unique=True,nullable=False)
    rate=db.Column(db.Integer,nullable=False,default=50)

    def __repr__(self):
        return self.name


class MyDetails(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100),unique=True,nullable=False,default='OMOLEYE JULIUS')
    location=db.Column(db.String(100),unique=True,nullable=False)
    phone_number=db.Column(db.String(20),nullable=False,default='08033872479')
    image_file=db.Column(db.String(20),nullable=False,default='default.jpg')
    email=db.Column(db.String(50),nullable=False,default='Joshkid610@gmail.com')

    def __repr__(self):
        return self.name

class Language(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    language=db.Column(db.String(100),unique=True,nullable=False)
    rate=db.Column(db.Integer,nullable=False,default=50)

    def __repr__(self):
        return self.language



@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    educations=Education.query.all()
    workexperiences=WorkExperience.query.all()
    languages=Language.query.all()
    skills=Skills.query.all()
    mydetails=MyDetails.query.all()
    return render_template('index.html',educations=educations,workexperiences=workexperiences,languages=languages,skills=skills,mydetails=mydetails)

if __name__=="__main__":
    app.run(debug=True)