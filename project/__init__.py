# project/__init__.py

from flask import Flask,jsonify

#初始化app

app = Flask(__name__)
app.config.from_object('project.config.DevelopmentConfig')

@app.route('/ping',methods=['GET'])
def ping_pong():
    return jsonify({
        'status':'sucess',
        'message':'pong!'
    })


