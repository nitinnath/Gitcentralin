from functools import wraps

import datetime
import jwt, os
import pymysql.cursors
from flask import Flask, redirect, request, render_template, session, flash, url_for
from werkzeug.security import *
from werkzeug.utils import secure_filename

from Consultant import ConsultantClass
from personallinks import PersonalLink
from userFile import UserModel

global data_dic

app = Flask(__name__)


@app.route("/")
def loadDefaultPage():
    return render_template('/login.html')


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
    if session:
        session.clear()
    if request.method == 'POST':
        user = request.form['username']
        password = request.form['password']
        userclass = UserModel.CheckUserExsist(user, password)
        # print("ssssssssssss",userclass)
        if userclass != None:
            session["isLogin"] = True
            session["userId"] = userclass['Id']
            session["fullName"] = userclass['fullname']
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
        # print("userrrr is authored")
        return render_template('consultation.html', paramName=session['fullName'])


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
    return render_template('consultationStep7.html', paramName=data_dic)

@app.route("/PostJob", methods=['POST', 'GET'])
def consultantPagesevenPostJob():
    print("in to consultantPagesevenPostJob")
    if request.method == 'POST':
        userid: object = session["userId"]
        steps = request.form['steps']
        Plan = request.form.get('plan', '')
        Title = request.form.get('Title', '')
        JobCategory = request.form.get('JobCategory', '')
        SubCategory = request.form.get('SubCategory', '')
        Description = request.form.get('Description', '')
        FileName = request.form.get('file', '')
        FileLocation = request.form.get('FileLocation', '')
        FileData = request.form.get('FileData', '')
        ProjectType = request.form.get('ProjectType', '')
        Describes = request.form.get('Describes', '')
        WorkType = request.form.get('WorkType', '')
        ApiToIntegrate = request.form.get('API', '')
        ProjectStage = request.form.get('ProjectStage', '')
        ImpSkills = request.form.get('ImpSkills', '')
        LookingSkills = request.form.get('LookingSkills', '')
        JobCanSeenBy = request.form.get('JobCanSeenBy', '')
        PayBy = request.form.get('PayBy', '')
        ProjectDuration = request.form.get('ProjectDuration', '')
        TimeRequirement = request.form.get('TimeRequirement', '')
        SpecificBudget = request.form.get('SpecificBudget', '')
        Urgency = request.form.get('Urgency', '')
        Feature = request.form['Feature']
        sevenbutton = request.form['sevenbutton']

        print("Retrieved from main->saveconsultant: ",userid, steps, Plan, Title, JobCategory, SubCategory, Description, FileName,
              FileLocation, FileData, ProjectType, Describes, WorkType, ApiToIntegrate, ProjectStage, ImpSkills, LookingSkills,
              JobCanSeenBy, PayBy, ProjectDuration, TimeRequirement, SpecificBudget, Urgency, Feature, sevenbutton)

        consultantObj = ConsultantClass(userid, steps, Plan, Title, JobCategory, SubCategory, Description, FileName, FileLocation,
                                        FileData, ProjectType, Describes, WorkType, ApiToIntegrate, ProjectStage, ImpSkills,
                                        LookingSkills, JobCanSeenBy, PayBy, ProjectDuration, TimeRequirement, SpecificBudget,
                                        Urgency, Feature, sevenbutton)
        if sevenbutton=='PostJob':
            print("Postjob if")
            consultantObj.FromSevenPostJob(steps, userid)
        elif sevenbutton=='SaveExit':
            print("SaveExit if")
            consultantObj.FromSevenSaveExit(steps, userid)

    return ""

'''@app.route("/SaveExit", methods=['POST', 'GET'])
def consultantPagesevenSaveExit():
    print("in to consultantPagesevenSaveEXIOT")
    if request.method == 'POST':
        userid: object = session["userId"]
        steps = request.form['steps']
        Plan = request.form.get('plan', '')
        Title = request.form.get('Title', '')
        JobCategory = request.form.get('JobCategory', '')
        SubCategory = request.form.get('SubCategory', '')
        Description = request.form.get('Description', '')
        FileName = request.form.get('file', '')
        FileLocation = request.form.get('FileLocation', '')
        FileData = request.form.get('FileData', '')
        ProjectType = request.form.get('ProjectType', '')
        Describes = request.form.get('Describes', '')
        WorkType = request.form.get('WorkType', '')
        ApiToIntegrate = request.form.get('API', '')
        ProjectStage = request.form.get('ProjectStage', '')
        ImpSkills = request.form.get('ImpSkills', '')
        LookingSkills = request.form.get('LookingSkills', '')
        JobCanSeenBy = request.form.get('JobCanSeenBy', '')
        PayBy = request.form.get('PayBy', '')
        ProjectDuration = request.form.get('ProjectDuration', '')
        TimeRequirement = request.form.get('TimeRequirement', '')
        SpecificBudget = request.form.get('SpecificBudget', '')
        Urgency = request.form.get('Urgency', '')
        Feature = request.form.get('Feature', '')
        print("Retrieved from main->saveconsultant: ",userid, steps, Plan, Title, JobCategory, SubCategory, Description, FileName,
              FileLocation, FileData, ProjectType, Describes, WorkType, ApiToIntegrate, ProjectStage, ImpSkills, LookingSkills,
              JobCanSeenBy, PayBy, ProjectDuration, TimeRequirement, SpecificBudget, Urgency, Feature)

        consultantObj = ConsultantClass(userid, steps, Plan, Title, JobCategory, SubCategory, Description, FileName, FileLocation,
                                        FileData, ProjectType, Describes, WorkType, ApiToIntegrate, ProjectStage, ImpSkills,
                                        LookingSkills, JobCanSeenBy, PayBy, ProjectDuration, TimeRequirement, SpecificBudget,
                                        Urgency, Feature)
        consultantObj.FromSevenSaveExit(steps, userid)

    return ""
'''

@app.route('/saveConsultantpage', methods=['POST', 'GET'])
def saveconsultant():
    userid: object = session["userId"]
    steps = request.form['steps']
    Plan = request.form.get('plan', '')
    Title = request.form.get('Title', '')
    JobCategory = request.form.get('JobCategory', '')
    SubCategory = request.form.get('SubCategory', '')
    Description = request.form.get('Description', '')
    FileName = request.form.get('file', '')
    FileLocation = request.form.get('FileLocation', '')
    FileData = request.form.get('FileData', '')
    ProjectType = request.form.get('ProjectType', '')
    Describes = request.form.get('Describes', '')
    WorkType = request.form.get('WorkType', '')
    ApiToIntegrate = request.form.get('API', '')
    ProjectStage = request.form.get('ProjectStage', '')
    ImpSkills = request.form.get('ImpSkills', '')
    LookingSkills = request.form.get('LookingSkills', '')
    JobCanSeenBy = request.form.get('JobCanSeenBy', '')
    PayBy = request.form.get('PayBy', '')
    ProjectDuration = request.form.get('ProjectDuration', '')
    TimeRequirement = request.form.get('TimeRequirement', '')
    SpecificBudget = request.form.get('SpecificBudget', '')
    Urgency = request.form.get('Urgency', '')
    Feature='NO'
    sevenbutton='0'
    print("Retrieved from main->saveconsultant: ",userid, steps, Plan, Title, JobCategory, SubCategory, Description, FileName,
          FileLocation, FileData, ProjectType, Describes, WorkType, ApiToIntegrate, ProjectStage, ImpSkills, LookingSkills,
          JobCanSeenBy, PayBy, ProjectDuration, TimeRequirement, SpecificBudget, Urgency, Feature, sevenbutton)

    consultantObj = ConsultantClass(userid, steps, Plan, Title, JobCategory, SubCategory, Description, FileName, FileLocation,
                                    FileData, ProjectType, Describes, WorkType, ApiToIntegrate, ProjectStage, ImpSkills,
                                    LookingSkills, JobCanSeenBy, PayBy, ProjectDuration, TimeRequirement, SpecificBudget,
                                    Urgency, Feature, sevenbutton)
    consultantObj.SaveConsultant()
    global data_dic
    data_dic= consultantObj.getConsultantById()
    print("DATA FOR DICTIOARY: ", data_dic)
    return steps


@app.route("/title")
def TitlePage():
    return render_template('title.html')


'''def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSION


@app.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)
        file = request.files['file']
        print("file is sssssssssssss: ", file)
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            print('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            print("filename is : ", filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # return redirect(url_for('uploaded_file', filename=filename))
return 
 <!doctype html>
 <title>Upload new File</title>
 <h1>Upload new File</h1>
 <form method=post enctype=multipart/form-data>
   <input type=file name=file>
   <input type=submit value=Upload>
 </form>
 '''


@app.route("/register", methods=['POST', 'GET'])
def RegistrationPage():
    if request.method == 'POST':
        name = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        paswd = request.form['paswd']
        ps = generate_password_hash(paswd)
        if (name == '' or name.isspace == True) or (lname == '' or lname.isspace() == True) or (
                email == '' or email.isspace() == True) or (paswd == '' or paswd.isspace() == True):
            error = "Please fill all the above details correctly."
            return render_template('landing-page.html', paramName=error)
        else:
            #print("All the details are : ", name, lname, email, paswd)
            fullname = name + " " + lname
            with connection.cursor() as cur:
                cur.execute(
                    "select * from user where username = '" + email + "' ")
                data = cur.fetchone()
                if data is not None:
                    error = "Email Id already used."
                    return render_template('landing-page.html', paramName=error)
                else:
                    sql = "INSERT INTO user ( username,email,password_hash,fullname, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s)"
                    cur.execute(sql, (email, email, paswd, fullname, datetime.datetime.now(), datetime.datetime.now()))
                    connection.commit()
                    ############
                    userclass = UserModel.CheckUserExsist(email, paswd)
                    # print("ssssssssssss",userclass)
                    if userclass != None:
                        session["isLogin"] = True
                        session["userId"] = userclass['Id']
                        session["fullName"] = userclass['fullname']
                        print("userId for session is : ", session["userId"])
                    return render_template('consultation.html', paramName=fullname)
                    ######
                cur.close()

    return render_template('landing-page.html')


if __name__ == '__main__':
    app.run(debug=True)
