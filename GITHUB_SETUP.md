# GitHub'a Yükleme Adımları

## 1. GitHub'da Yeni Repo Oluştur

1. [github.com/new](https://github.com/new) adresine git
2. Repository adı: `toolbox-platform` (veya istediğin bir isim)
3. Description: "Modern online tools platform with video downloader"
4. Public veya Private seç
5. **README, .gitignore veya license EKLEME** (zaten var)
6. "Create repository" butonuna tıkla

## 2. Terminalden Push Et

GitHub'da repo oluşturduktan sonra, aşağıdaki komutları çalıştır:

```bash
# GitHub repo URL'ini ekle (kendi username'inle değiştir)
git remote add origin https://github.com/KULLANICI_ADIN/toolbox-platform.git

# Push et
git push -u origin main
```

## 3. Railway'e Deploy Et

1. [railway.app](https://railway.app) → Login with GitHub
2. "New Project" → "Deploy from GitHub repo"
3. Az önce oluşturduğun repo'yu seç
4. Railway otomatik deploy edecek
5. "Settings" → "Generate Domain" ile domain al

## Alternatif: GitHub CLI ile (Önce yüklemen gerekir)

```bash
# GitHub CLI yükle
brew install gh

# Login ol
gh auth login

# Repo oluştur ve push et
gh repo create toolbox-platform --public --source=. --remote=origin --push
```

## ✅ Hazır!

Repo oluşturuldu ve commit'lendi. Sadece GitHub'a push etmen kaldı!
