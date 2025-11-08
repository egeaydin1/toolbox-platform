# Video Downloader

Python ile yazılmış basit ve kullanışlı video indirme uygulaması. YouTube ve diğer platformlardan video veya ses indirebilirsiniz.

## Özellikler

- 🎬 Video indirme (farklı kalite seçenekleri)
- 🎵 Sadece ses indirme (MP3 formatında)
- 📊 İndirme ilerlemesi gösterimi
- 🎯 Kullanıcı dostu menü sistemi

## Kurulum

1. Gerekli kütüphaneyi yükleyin:
```bash
pip install -r requirements.txt
```

2. (Opsiyonel) Ses dönüştürme için FFmpeg gereklidir:
```bash
# macOS
brew install ffmpeg

# Linux (Ubuntu/Debian)
sudo apt install ffmpeg

# Windows
# https://ffmpeg.org/download.html adresinden indirin
```

## Kullanım

Uygulamayı çalıştırın:
```bash
python video_downloader.py
```

Menüden istediğiniz işlemi seçin:
- Video indirmek için URL girin ve kalite seçin
- Sadece ses indirmek için MP3 seçeneğini kullanın
- İndirilen dosyalar `downloads` klasörüne kaydedilir

## Desteklenen Platformlar

- YouTube
- Vimeo
- Dailymotion
- Twitter
- Facebook
- Instagram
- Ve 1000+ platform daha

## Notlar

- İndirilen videolar `downloads` klasörüne kaydedilir
- Ses dosyaları MP3 formatına dönüştürülür (FFmpeg gerektirir)
- İnternet bağlantınızın hızına göre indirme süresi değişir
