from flask import Flask, render_template
import os  # Import the os module

app = Flask(__name__)

@app.route('/')
def index():
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
    # Construct the path to the lyrics file
    lyrics_file_path = os.path.join(app.root_path, 'lyrics', f'{song}.txt')
    
    # Read the contents of the lyrics file
    with open(lyrics_file_path, 'r') as file:
        lyrics = file.read()
    
    # Render the HTML template with the lyrics
    return render_template('lyrics.html', lyrics=lyrics)

#@app.route('/songs')
#def songs():
#    # files from folder
#    pass
#
#@app.route('/song/:song')
#def song_site(song):
#    return render_template("song.html", song)

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

if __name__ == '__main__':
    app.run(debug=True)
