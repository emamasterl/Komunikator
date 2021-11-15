from flask import Flask, render_template, send_from_directory, request
from flask_socketio import SocketIO
import json
import conversation_main

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

@app.route('/')
def sessions():
    return render_template('index.html')

def messageReceived(methods=['GET','POST']):
    print('message was received!!!')
    
@socketio.on('my event')
def handle_my_custom_event(json1, methods=['GET','POST']):
    print('received my event: ' + str(json1))
    userinput_sound = json1['message']
    username = json1['user_name']
    botresponse = conversation_main.question_to_answer(userinput_sound)
    json1['message']=botresponse
    socketio.emit('my response', json1, callback=messageReceived)

if __name__ == '__main__':
    socketio.run(app,port = 5000, host='0.0.0.0', debug=True)