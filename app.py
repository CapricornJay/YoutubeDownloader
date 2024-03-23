from flask import Flask, render_template, request
from pytube import YouTube
import os
import uuid

app = Flask(__name__)

# Set up secure secret key
app.secret_key = os.urandom(24)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        video_url = request.form.get('video_url')
        if not video_url:
            return render_template('index.html', error="Please provide a valid YouTube URL.")
        
        try:
            yt = YouTube(video_url)
            video_stream = yt.streams.filter(progressive=True).order_by('resolution').desc().first()
            if not video_stream:
                return render_template('index.html', error="No suitable video stream found.")
            
            download_dir = os.path.join('downloads', str(uuid.uuid4()))
            os.makedirs(download_dir, exist_ok=True)
            download_path = os.path.join(download_dir, video_stream.default_filename)
            video_stream.download(download_dir)
            
            return render_template('index.html', video_url=video_url, download_path=download_path, downloaded=True)
        except Exception as e:
            return render_template('index.html', error=f"An error occurred: {str(e)}")
    
    return render_template('index.html')

if __name__ == '__main__':
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
    app.run(debug=False)  # Disable debug mode in production
