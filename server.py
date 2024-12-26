
from flask import Flask, request, send_file
import yt_dlp

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <form method="POST" action="/download">
            <input type="text" name="url" placeholder="Cole o link do vídeo" required>
            <button type="submit">Baixar Vídeo</button>
        </form>
    '''

@app.route('/download', methods=['POST'])
def download_video():
    url = request.form['url']
    ydl_opts = {
        'format': 'best',
        'outtmpl': 'video.mp4',  # Caminho temporário do arquivo
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return send_file('video.mp4', as_attachment=True, download_name='video.mp4')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
