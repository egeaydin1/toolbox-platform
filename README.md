# 🎬 Video Downloader - macOS Edition

Python ile yazılmış güçlü ve kullanıcı dostu video indirme uygulaması. YouTube ve 1000+ platformdan video veya ses indirebilirsiniz.

## ✨ Özellikler

- 🎬 **Video İndirme** - 1080p, 720p, 480p veya en iyi kalite
- 🎵 **MP3 Dönüştürme** - Sadece ses indirme (MP3 formatında)
- 📊 **Video Bilgisi** - İndirmeden önce video detaylarını görüntüleme
- ⏳ **İlerleme Göstergesi** - Gerçek zamanlı indirme durumu
- 🎯 **Kullanıcı Dostu** - Renkli ve interaktif menü sistemi
- 🌐 **1000+ Platform** - YouTube, Vimeo, Twitter, Instagram ve daha fazlası

## 🚀 Kurulum

### 1. Gerekli Kütüphaneyi Yükleyin

```bash
pip install -r requirements.txt
```

### 2. FFmpeg Yükleyin (Gerekli)

FFmpeg video birleştirme ve MP3 dönüştürme için gereklidir:

```bash
brew install ffmpeg
```

## 💻 Kullanım

Uygulamayı çalıştırın:

```bash
python video_downloader.py
```

### Menü Seçenekleri

1. **Video İndir** - Kalite seçerek video indirin
2. **Sadece Ses İndir** - MP3 formatında ses dosyası indirin
3. **Video Bilgisi Al** - Video hakkında detaylı bilgi alın
4. **Çıkış** - Programdan çıkın

### Örnek Kullanım

```
🔗 Video URL'sini girin: https://www.youtube.com/watch?v=xxxxx

🎬 KALİTE SEÇİMİ
1️⃣  En İyi Kalite
2️⃣  1080p
3️⃣  720p
4️⃣  480p

👉 Seçim (1-4): 2

⏳ İlerleme: 45.2% | 🚀 Hız: 2.5MiB/s | ⏱️  Kalan: 00:15
```

## 📦 Desteklenen Platformlar

- ✅ YouTube
- ✅ Vimeo
- ✅ Dailymotion
- ✅ Twitter / X
- ✅ Facebook
- ✅ Instagram
- ✅ TikTok
- ✅ Reddit
- ✅ Ve 1000+ platform daha!

## 📁 İndirilen Dosyalar

İndirilen tüm dosyalar `downloads` klasörüne kaydedilir.

## 🛠️ Gereksinimler

- Python 3.7+
- yt-dlp
- FFmpeg (video birleştirme ve MP3 dönüştürme için)

## 💡 İpuçları

- YouTube bot koruması için user-agent otomatik ayarlanır
- Yüksek kaliteli videolar daha fazla yer kaplar
- MP3 dönüştürme için FFmpeg gereklidir
- İnternet hızınıza göre indirme süresi değişir

## 🐛 Sorun Giderme

**"yt-dlp bulunamadı" hatası:**
```bash
pip install yt-dlp
```

**"FFmpeg bulunamadı" hatası:**
```bash
brew install ffmpeg
```

**YouTube bot koruması:**
Uygulama otomatik olarak user-agent ayarlar, genellikle sorun yaşanmaz.

## 📝 Lisans

Bu proje açık kaynaklıdır ve özgürce kullanılabilir.

---

**Not:** Bu araç yalnızca eğitim amaçlıdır. Telif hakkı korumalı içerikleri indirirken yerel yasalara uyun.
