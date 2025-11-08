#!/usr/bin/env python3
"""
Video Downloader - YouTube ve diğer platformlardan video indirme uygulaması
macOS için optimize edilmiş versiyon
"""

import sys
import os
from pathlib import Path

try:
    import yt_dlp
except ImportError:
    print("❌ yt-dlp kütüphanesi bulunamadı!")
    print("📦 Yüklemek için: pip install yt-dlp")
    sys.exit(1)


class VideoDownloader:
    def __init__(self, output_dir="downloads"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
    
    def get_video_info(self, url):
        """Video bilgilerini al"""
        try:
            ydl_opts = {
                'quiet': True,
                'no_warnings': True,
                'user_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            }
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                
                # Mevcut kaliteleri bul
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
                
                return {
                    'title': info.get('title', 'Bilinmeyen'),
                    'uploader': info.get('uploader', 'Bilinmeyen'),
                    'duration': info.get('duration', 0),
                    'qualities': sorted(list(available_qualities), reverse=True)
                }
        except Exception as e:
            print(f"❌ Video bilgisi alınamadı: {str(e)}")
            return None
    
    def download_video(self, url, quality="best", audio_only=False):
        """Video indir"""
        try:
            ydl_opts = {
                'outtmpl': str(self.output_dir / '%(title)s.%(ext)s'),
                'progress_hooks': [self._progress_hook],
                'user_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                'http_headers': {
                    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                    'Accept-Language': 'en-us,en;q=0.5',
                    'Sec-Fetch-Mode': 'navigate',
                },
            }
            
            if audio_only:
                ydl_opts['format'] = 'bestaudio/best'
                ydl_opts['postprocessors'] = [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }]
                print("\n🎵 MP3 formatında indiriliyor...")
            else:
                if quality == "best":
                    ydl_opts['format'] = 'bestvideo+bestaudio/best'
                elif quality == "1080p":
                    ydl_opts['format'] = 'bestvideo[height<=1080]+bestaudio/best[height<=1080]'
                elif quality == "720p":
                    ydl_opts['format'] = 'bestvideo[height<=720]+bestaudio/best[height<=720]'
                elif quality == "480p":
                    ydl_opts['format'] = 'bestvideo[height<=480]+bestaudio/best[height<=480]'
                print(f"\n🎬 {quality} kalitesinde indiriliyor...")
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                print(f"📥 URL: {url}")
                info = ydl.extract_info(url, download=True)
                print(f"\n✅ İndirme tamamlandı: {info.get('title', 'Video')}")
                print(f"📁 Konum: {self.output_dir}")
                return True
                
        except Exception as e:
            print(f"\n❌ Hata: {str(e)}")
            return False
    
    def _progress_hook(self, d):
        """İndirme ilerlemesini göster"""
        if d['status'] == 'downloading':
            percent = d.get('_percent_str', 'N/A')
            speed = d.get('_speed_str', 'N/A')
            eta = d.get('_eta_str', 'N/A')
            print(f"\r⏳ İlerleme: {percent} | 🚀 Hız: {speed} | ⏱️  Kalan: {eta}", end='', flush=True)
        elif d['status'] == 'finished':
            print("\n🔄 İşleniyor...")


def format_duration(seconds):
    """Süreyi formatla"""
    if not seconds:
        return "Bilinmiyor"
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    if hours > 0:
        return f"{hours}:{minutes:02d}:{secs:02d}"
    return f"{minutes}:{secs:02d}"


def main():
    print("\n" + "=" * 60)
    print("🎬  VIDEO DOWNLOADER - macOS Edition")
    print("=" * 60)
    print("📺 YouTube, Vimeo, Twitter ve 1000+ platform desteklenir")
    print("=" * 60 + "\n")
    
    downloader = VideoDownloader()
    
    while True:
        print("\n" + "─" * 60)
        print("📋 MENÜ")
        print("─" * 60)
        print("1️⃣  Video İndir")
        print("2️⃣  Sadece Ses İndir (MP3)")
        print("3️⃣  Video Bilgisi Al")
        print("4️⃣  Çıkış")
        print("─" * 60)
        
        choice = input("\n👉 Seçiminiz (1-4): ").strip()
        
        if choice == "4":
            print("\n👋 Görüşmek üzere!")
            break
        
        if choice not in ["1", "2", "3"]:
            print("❌ Geçersiz seçim! Lütfen 1-4 arası bir sayı girin.")
            continue
        
        url = input("\n🔗 Video URL'sini girin: ").strip()
        
        if not url:
            print("❌ URL boş olamaz!")
            continue
        
        if choice == "3":
            # Video bilgisi al
            print("\n🔍 Video bilgisi alınıyor...")
            info = downloader.get_video_info(url)
            if info:
                print("\n" + "─" * 60)
                print("📊 VİDEO BİLGİLERİ")
                print("─" * 60)
                print(f"📝 Başlık: {info['title']}")
                print(f"👤 Yükleyen: {info['uploader']}")
                print(f"⏱️  Süre: {format_duration(info['duration'])}")
                if info['qualities']:
                    print(f"🎬 Mevcut Kaliteler: {', '.join(info['qualities'])}")
                print("─" * 60)
        
        elif choice == "1":
            # Video indir
            print("\n🎬 KALİTE SEÇİMİ")
            print("─" * 60)
            print("1️⃣  En İyi Kalite")
            print("2️⃣  1080p")
            print("3️⃣  720p")
            print("4️⃣  480p")
            print("─" * 60)
            quality_choice = input("👉 Seçim (1-4): ").strip()
            
            quality_map = {"1": "best", "2": "1080p", "3": "720p", "4": "480p"}
            quality = quality_map.get(quality_choice, "best")
            
            downloader.download_video(url, quality=quality)
        
        elif choice == "2":
            # Sadece ses indir
            downloader.download_video(url, audio_only=True)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Program sonlandırıldı.")
        sys.exit(0)
