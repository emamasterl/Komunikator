from flask import Flask, render_template, send_from_directory, request
from flask_socketio import SocketIO
import conversation_main
from text_to_speech import text_to_speech as tts
from speech_to_text import get_text_from_mic

import logging

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

log = logging.getLogger('werkzeug')
log.disabled = True
app.logger.disabled = True

@app.route('/')
def sessions():
    return render_template('index.html')

def messageReceived(methods=['GET','POST']):
    print('message was received!!!')
    
@socketio.on('my event')
def handle_my_custom_event(json1, methods=['GET','POST']):
    print('received my event: ' + str(json1))
    if json1 != {'data': 'User Connected'} and json1 != {'user_name': '', 'message': ''}:
        userinput_sound = json1['message']
        #userinput_sound = get_text_from_mic()
        username = json1['user_name']
        botresponse = conversation_main.question_to_answer(userinput_sound)

        json1['message']=botresponse
        socketio.emit('my response', json1, callback=messageReceived)
        tts(str(botresponse))


if __name__ == '__main__':
    socketio.run(app,port = 5000, host='0.0.0.0', debug=True)