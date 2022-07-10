import time 
from flask import Flask, request
# from flaskext.mysql import MySQL
import mysql.connector
import env
import json
from DBs import sign_new_user, auth_new_user, \
    show_all_users, login_user, show_event, \
    add_points_to_user, change_dynamic_event, create_event,\
        check_admin, check_user


from QRs import create_QR





app = Flask(__name__)

@app.route("/api")
def test_connection():

    

    
    
    
    return "Пользователь зареган"

@app.route("/api/users")
def api_users():
    return show_all_users()
    
    


@app.route("/api/check_user")
def api_check_user():
    if 'session_token' in request.cookies:
        
        session_token = request.cookies['session_token']
        if check_user(session_token):
            return {'statusSuccess':True}
        else:
            return {'statusSuccess':False}
            
        
        
        
        

    else:
        return {'statusSuccess':False}
    
    return {'statusSuccess':False}


@app.route("/api/admin/createevent", methods=['POST'])
def api_admin_createevent():
    post_data = request.data
    data_json = json.loads(post_data.decode('utf-8'))
    # print(data_json)
    title = data_json['title']
    description = data_json['description']
    value = data_json['value']
    # dynamic = data_json['dynamic']
    dynamic = False
    print(title)
    event_creditentials = create_event(title, description, value, dynamic)
    create_QR(event_creditentials['event_ID'], event_creditentials['event_url'])
    
    
    
    
    return {'url': f'event/{title}'}

@app.route("/api/signuser", methods=['POST'])
def api_signuser():
    try:
        post_data = request.data
        data_json = json.loads(post_data.decode('utf-8'))
        firstname = data_json['firstname']
        lastname = data_json['lastname']
        grade = data_json['grade']

        email = data_json['email']
        password = data_json['password']
        
        print(firstname, email, password)
        user_id = auth_new_user(email, password)
        print(user_id)
        sign_new_user(user_id, lastname, firstname, grade, email)
        
        return {'statusSuccess':True, 'session_token':user_id}
    except:
        return {'statusSuccess':False}
        
    
@app.route("/api/loginuser", methods=['POST'])
def api_loginuser():
    
    try:
        post_data = request.data
        data_json = json.loads(post_data.decode('utf-8'))

        email = data_json['email']
        password = data_json['password']
        user_id = login_user(email, password) 
        print(user_id)
        if user_id!="Login Failed":
            return {'statusSuccess':True, 'session_token':user_id}
        
        return {'statusSuccess':False}
        

    except:
        return {'statusSuccess':False}


@app.route('/api/event/<event_PATH>', methods=['POST'])
def api_event(event_PATH):
    if 'session_token' in request.cookies:
        
        session_token = request.cookies['session_token']
        
        response = show_event(event_PATH)    
        add_points_to_user(session_token, response['value'], response['event_id'])
        change_dynamic_event(response["event_id"])
        return response

    else:
        return {'statusSuccess':False}
    
    
    
    return {'statusSuccess':False}
         

@app.route("/api/user")
def api_user():
    return ""

@app.route('/api/time')
def get_current_time():
    return {'time': time.time()}
