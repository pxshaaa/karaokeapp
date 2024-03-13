#from flask import Flask, render_template
#from flask_socketio import SocketIO, emit
#
#app = Flask(__name__)
#app.config['SECRET_KEY'] = 'secret!'
#socketio = SocketIO(app)
#
#@socketio.on('offer')
#def handle_offer(offer):
#    emit('offer', offer, broadcast=True)
#
#@socketio.on('answer')
#def handle_answer(answer):
#    emit('answer', answer, broadcast=True)
#
#if __name__ == '__main__':
#    socketio.run(app)