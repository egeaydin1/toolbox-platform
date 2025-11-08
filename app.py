from flask import Flask, render_template, request, jsonify, send_file
import yt_dlp
import os
import uuid
from pathlib import Path
import threading
import time

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 500 * 1024 * 1024  # 500MB max

DOWNLOAD_FOLDER = Path('downloads')
DOWNLOAD_FOLDER.mkdir(exist_ok=True)

# Geçici dosyaları temizleme
def cleanup_old_files():
    while True:
        time.sleep(3600)  # Her saat
        for file in DOWNLOAD_FOLDER.glob('*'):
            if time.time() - file.stat().st_mtime > 3600:  # 1 saatten eski
                try:
                    file.unlink()
                except:
                    pass

threading.Thread(target=cleanup_old_files, daemon=True).start()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/video-info', methods=['POST'])
def get_video_info():
    try:
        if not request.is_json:
            return jsonify({'error': 'Content-Type must be application/json'}), 400
            
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid JSON data'}), 400
            
        url = data.get('url')
        
        if not url:
            return jsonify({'error': 'URL gerekli'}), 400
        
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'no_color': True,
            'socket_timeout': 30,
            'extractor_retries': 3,
            'fragment_retries': 3,
            'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'en-us,en;q=0.5',
                'Sec-Fetch-Mode': 'navigate',
            },
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            
            # Formatları al
            formats = info.get('formats', [])
            available_qualities = set()
            for f in formats:
                height = f.get('height')
                if height:
                    if height >= 1080:
                        available_qualities.add('1080p')
                    if height >= 720:
                        available_qualities.add('720p')
                    if height >= 480:
                        available_qualities.add('480p')
            
            return jsonify({
                'title': info.get('title', 'Bilinmeyen'),
                'thumbnail': info.get('thumbnail', ''),
                'duration': info.get('duration', 0),
                'uploader': info.get('uploader', 'Bilinmeyen'),
                'available_qualities': sorted(list(available_qualities), reverse=True),
            })
    except Exception as e:
        print(f"Error in get_video_info: {str(e)}")
        return jsonify({'error': str(e)}), 400

@app.route('/api/download', methods=['POST'])
def download_video():
    try:
        if not request.is_json:
            return jsonify({'error': 'Content-Type must be application/json'}), 400
            
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid JSON data'}), 400
            
        url = data.get('url')
        format_type = data.get('format', 'video')
        quality = data.get('quality', 'best')
        
        if not url:
            return jsonify({'error': 'URL gerekli'}), 400
        
        file_id = str(uuid.uuid4())
        
        ydl_opts = {
            'outtmpl': str(DOWNLOAD_FOLDER / f'{file_id}.%(ext)s'),
            'quiet': True,
            'no_warnings': True,
            'no_color': True,
            'socket_timeout': 30,
            'extractor_retries': 3,
            'fragment_retries': 3,
            'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'http_headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Language': 'en-us,en;q=0.5',
                'Sec-Fetch-Mode': 'navigate',
            },
        }
        
        if format_type == 'audio':
            ydl_opts['format'] = 'bestaudio/best'
            ydl_opts['postprocessors'] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        else:
            if quality == '1080p':
                ydl_opts['format'] = 'bestvideo[height<=1080]+bestaudio/best[height<=1080]'
            elif quality == '720p':
                ydl_opts['format'] = 'bestvideo[height<=720]+bestaudio/best[height<=720]'
            elif quality == '480p':
                ydl_opts['format'] = 'bestvideo[height<=480]+bestaudio/best[height<=480]'
            else:
                ydl_opts['format'] = 'bestvideo+bestaudio/best'
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            
            # İndirilen dosyayı bul
            for file in DOWNLOAD_FOLDER.glob(f'{file_id}.*'):
                return jsonify({
                    'success': True,
                    'file_id': file_id,
                    'filename': info.get('title', 'video'),
                    'extension': file.suffix
                })
        
        return jsonify({'error': 'Dosya bulunamadı'}), 500
        
    except Exception as e:
        print(f"Error in download_video: {str(e)}")
        return jsonify({'error': str(e)}), 400

@app.route('/api/download-file/<file_id>')
def download_file(file_id):
    try:
        for file in DOWNLOAD_FOLDER.glob(f'{file_id}.*'):
            return send_file(file, as_attachment=True)
        return jsonify({'error': 'Dosya bulunamadı'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
