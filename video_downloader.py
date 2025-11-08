#!/usr/bin/env python3
"""
Video Downloader - YouTube ve diğer platformlardan video indirme uygulaması
"""

import sys
import os
from pathlib import Path

try:
    import yt_dlp
except ImportError:
    print("yt-dlp kütüphanesi bulunamadı!")
    print("Lütfen şu komutu çalıştırın: pip install yt-dlp")
    sys.exit(1)


class VideoDownloader:
    def __init__(self, output_dir="downloads"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
    
    def download_video(self, url, quality="best", audio_only=False):
        """Video indir"""
        try:
            ydl_opts = {
                'outtmpl': str(self.output_dir / '%(title)s.%(ext)s'),
                'progress_hooks': [self._progress_hook],
            }
            
            if audio_only:
                ydl_opts['format'] = 'bestaudio/best'
                ydl_opts['postprocessors'] = [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }]
            else:
                if quality == "best":
                    ydl_opts['format'] = 'bestvideo+bestaudio/best'
                elif quality == "720p":
                    ydl_opts['format'] = 'bestvideo[height<=720]+bestaudio/best[height<=720]'
                elif quality == "480p":
                    ydl_opts['format'] = 'bestvideo[height<=480]+bestaudio/best[height<=480]'
            
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                print(f"\n📥 İndiriliyor: {url}")
                info = ydl.extract_info(url, download=True)
                print(f"\n✅ İndirme tamamlandı: {info.get('title', 'Video')}")
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
            print(f"\rİlerleme: {percent} | Hız: {speed} | Kalan: {eta}", end='')
        elif d['status'] == 'finished':
            print("\n🔄 İşleniyor...")


def main():
    print("=" * 50)
    print("🎬 Video Downloader")
    print("=" * 50)
    
    downloader = VideoDownloader()
    
    while True:
        print("\n--- Menü ---")
        print("1. Video indir")
        print("2. Sadece ses indir (MP3)")
        print("3. Çıkış")
        
        choice = input("\nSeçiminiz (1-3): ").strip()
        
        if choice == "3":
            print("Çıkılıyor...")
            break
        
        if choice not in ["1", "2"]:
            print("❌ Geçersiz seçim!")
            continue
        
        url = input("\nVideo URL'sini girin: ").strip()
        
        if not url:
            print("❌ URL boş olamaz!")
            continue
        
        if choice == "1":
            print("\nKalite seçin:")
            print("1. En iyi kalite")
            print("2. 720p")
            print("3. 480p")
            quality_choice = input("Seçim (1-3): ").strip()
            
            quality_map = {"1": "best", "2": "720p", "3": "480p"}
            quality = quality_map.get(quality_choice, "best")
            
            downloader.download_video(url, quality=quality)
        
        elif choice == "2":
            downloader.download_video(url, audio_only=True)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Program sonlandırıldı.")
        sys.exit(0)
