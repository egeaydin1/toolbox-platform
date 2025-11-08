# ToolBox - Railway Deployment Rehberi

Modern ve animasyonlu online araçlar platformu. Video indirme ve gelecekte daha fazla araç!

## 🚀 Railway'e Deploy Etme

### 1. Railway Hesabı Oluştur
- [railway.app](https://railway.app) adresine git
- GitHub hesabınla giriş yap

### 2. Yeni Proje Oluştur
1. "New Project" butonuna tıkla
2. "Deploy from GitHub repo" seç
3. Bu repository'yi seç
4. Railway otomatik olarak deploy edecek

### 3. Environment Variables (Opsiyonel)
Railway otomatik olarak `PORT` değişkenini ayarlar, başka bir şey eklemeye gerek yok.

### 4. Domain Ayarla
1. Projenin "Settings" bölümüne git
2. "Generate Domain" butonuna tıkla
3. Railway size ücretsiz bir domain verecek (örn: `your-app.up.railway.app`)

## 🎯 Özellikler

- ✨ Modern ve animasyonlu arayüz
- 🎬 Video indirme (YouTube, Vimeo, 1000+ platform)
- 🎵 Sadece ses indirme (MP3)
- 📱 Responsive tasarım
- 🌟 Yıldızlı arka plan animasyonu
- 🚀 Hızlı ve kullanımı kolay

## 📦 Gelecek Araçlar

- 🖼️ Resim Düzenleyici
- 📄 PDF Dönüştürücü
- 🔗 URL Kısaltıcı
- 🎨 Renk Paleti
- 📊 QR Kod Oluşturucu

## 🛠️ Yerel Geliştirme

```bash
# Virtual environment oluştur
python3 -m venv venv
source venv/bin/activate

# Bağımlılıkları yükle
pip install -r requirements.txt

# Uygulamayı çalıştır
python app.py
```

Tarayıcıda `http://localhost:5000` adresine git.

## 📝 Notlar

- FFmpeg ses dönüştürme için gereklidir (Railway'de otomatik yüklenir)
- İndirilen dosyalar 1 saat sonra otomatik silinir
- Ücretsiz Railway planı aylık 500 saat çalışma süresi verir

## 🎨 Teknolojiler

- **Backend**: Flask (Python)
- **Video İndirme**: yt-dlp
- **Frontend**: Vanilla JavaScript, CSS3
- **Animasyonlar**: CSS Keyframes
- **Deploy**: Railway

## 📞 Destek

Herhangi bir sorun yaşarsan Railway loglarını kontrol et:
```bash
railway logs
```

Başarılar! 🚀
