import os
import logging
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/')
def index():
    logger.info('Rendering index.html')
    return render_template('index.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/rates')
def rates():
    return render_template('rates.html')

@app.route('/play_music')
def play_music():
    return render_template('play.html')

@app.route('/lyrics/<song>')
def display_lyrics(song):
    lyrics_file_path = os.path.join(app.root_path, 'lyrics', f'{song}.txt')
    with open(lyrics_file_path, 'r') as file:
        lyrics = file.read()
    return lyrics  # Return only the lyrics content without rendering a template

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/rooms')
def rooms():
    return render_template('rooms.html')

@app.route('/events')
def events():
    return render_template('events.html')

@app.route('/drinks')
def drinks():
    return render_template('drinks.html')

@socketio.on('offer')
def handle_offer(offer):
    logger.info('Received offer')
    print(type(offer))
    emit('offer', offer, broadcast=True)

#@socketio.on('answer')
#def handle_answer(answer):
#    logger.info('Received answer')
#    emit('answer', answer, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
