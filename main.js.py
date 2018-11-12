from functools import wraps

import datetime
import jwt
import pymysql.cursors
from flask import Flask, redirect, request, render_template, session

from Consultant import ConsultantClass
from personallinks import PersonalLink
from userFile import UserModel

app = Flask(__name__)


@app.route("/")
def loadDefaultPage():
    return render_template('/consultation.html')


app.config['SECRET_KEY'] = 'meow'

# Connect to the database
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             # password='Ets123$$$',
                             password='test',
                             db='testdb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


def token_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.args.get('token')
        try:
            jwt.decode(token, app.config['SECRET_KEY'])
            return f(*args, **kwargs)
        except:
            return 'Pass valid token'

    return wrapper


def IsAuthorized():
    if session.get('isLogin') == None or session.get('isLogin') == False:
        return False
    else:
        return True


def get_token():
    expiration_Date = datetime.datetime.now() + datetime.timedelta(seconds=1000)
    token = jwt.encode({'exp': expiration_Date}, app.config['SECRET_KEY'], algorithm='HS256')
    return token


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        password = request.form['password']
        userclass = UserModel.CheckUserExsist(user, password)
        if userclass != None:
            session["isLogin"] = True
            session["userId"] = userclass['Id']
            return redirect('/consultant')
        else:
            session["isLogin"] = False
            session["userId"] = 0
            error = 'Please enter valid username and password'
            return render_template('login.html', paramName=error)
    else:
        return render_template('login.html')


@app.route('/personallink', methods=['POST', 'GET'])
def personalLinks():
    if request.method == 'POST':
        priority = request.form['priority']
        websiteurl = request.form['url']
        websitename = request.form['webname']
        purpose = request.form['purpose']
        tags = request.form['tags']
        type = request.form['type']
        market = request.form['market']
        visualize = request.form['visualize']
        now = datetime.datetime.now()
        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')

        personalLinkClass = PersonalLink(priority, websiteurl, websitename, purpose, tags, type, market, visualize,
                                         formatted_date)
        userclass = personalLinkClass.insertPersonalLink()
        if userclass != 0:
            return render_template('personal-links.html', data=personalLinkClass.getAllData(),
                                   paramName="Saved successfully.")
        else:
            error = 'Please enter valid username and password'
            return render_template('login.html', paramName=error)
    else:
        if IsAuthorized() == False:
            return redirect('/login')
        else:
            now = datetime.datetime.now()
            formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
            personalLinkClass = PersonalLink('', '', '', '', '', '', '', '', formatted_date)
            data = personalLinkClass.getAllData()
            return render_template('personal-links.html', data=data)


@app.route("/consultant")
def consultantPage():
    if IsAuthorized() == False:
        return redirect('/login')
    else:
        return render_template('consultation.html')


@app.route("/consultantstep1")
def consultantPagefirst():
    return render_template('consultationStep1.html')


@app.route("/consultantstep2")
def consultantPagesecond():
    return render_template('consultationStep2.html')


@app.route("/consultantstep3")
def consultantPagethird():
    return render_template('consultationStep3.html')


@app.route("/consultantstep4")
def consultantPagefour():
    return render_template('consultationStep4.html')


@app.route("/consultantstep5")
def consultantPagefive():
    return render_template('consultationStep5.html')


@app.route("/consultantstep6")
def consultantPagesix():
    return render_template('consultationStep6.html')


@app.route("/consultantstep7")
def consultantPageseven():
    return render_template('consultationStep7.html')


@app.route('/saveConsultantpage', methods=['POST'])
def saveconsultant():
    #userid: object = session["userId"]#Permanent
    userid: object = session["112"]
    steps = request.form['steps']
    Plan = request.form.get('plan', '')
    #Title = request.form.get('Title', '')#permanent
    Title = request.form.get('Title', 'abc')
    Description = request.form.get('Description', '')
    ProjectType = request.form.get('ProjectType', '')
    Describes = request.form.get('Describes', '')
    ConsultantDoing = request.form.get('ConsultantDoing', '')
    API = request.form.get('API', '')
    ProjectStage = request.form.get('ProjectStage', '')
    consultantObj = ConsultantClass(steps, userid, Plan, Title, Description, ProjectType, Describes, ConsultantDoing,
                                    API, ProjectStage, '', '', '', '', '', '', '', '', '')
    consultantObj.SaveConsultant()
    return steps


if __name__ == '__main__':
    app.run(debug=True)
