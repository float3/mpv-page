from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

playlist = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video_url = request.form['video_url']
        playlist.append(video_url)
        subprocess.Popen(['mpv', '--fs', video_url.replace('piped.video','youtube.com')])
        return render_template('index.html', video_url=video_url, playlist=playlist)
    return render_template('index.html', video_url='', playlist=playlist)

@app.route('/skip', methods=['GET'])
def skip():
    if playlist:
        playlist.pop(0)
        return jsonify({'message': 'Video skipped'})
    return jsonify({'message': 'Playlist is empty'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
