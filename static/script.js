let currentVideoUrl = '';

function openTool(toolName) {
    const modal = document.getElementById(`${toolName}-modal`);
    if (modal) {
        modal.classList.add('active');
        document.body.style.overflow = 'hidden';
    }
}

function closeModal() {
    const modals = document.querySelectorAll('.modal');
    modals.forEach(modal => {
        modal.classList.remove('active');
    });
    document.body.style.overflow = 'auto';
    
    // Reset form
    document.getElementById('video-url').value = '';
    document.getElementById('video-info').style.display = 'none';
    document.getElementById('download-status').innerHTML = '';
}

async function getVideoInfo() {
    const urlInput = document.getElementById('video-url');
    const url = urlInput.value.trim();
    
    if (!url) {
        showStatus('Lütfen bir URL girin', 'error');
        return;
    }
    
    currentVideoUrl = url;
    const btn = event.target;
    btn.classList.add('loading');
    btn.disabled = true;
    
    try {
        const response = await fetch('/api/video-info', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ url })
        });
        
        const data = await response.json();
        
        if (response.ok) {
            displayVideoInfo(data);
        } else {
            showStatus(data.error || 'Bir hata oluştu', 'error');
        }
    } catch (error) {
        showStatus('Bağlantı hatası: ' + error.message, 'error');
    } finally {
        btn.classList.remove('loading');
        btn.disabled = false;
    }
}

function displayVideoInfo(info) {
    document.getElementById('video-thumbnail').src = info.thumbnail;
    document.getElementById('video-title').textContent = info.title;
    document.getElementById('video-uploader').textContent = '👤 ' + info.uploader;
    
    const duration = formatDuration(info.duration);
    document.getElementById('video-duration').textContent = '⏱️ ' + duration;
    
    document.getElementById('video-info').style.display = 'block';
    document.getElementById('download-status').innerHTML = '';
}

function formatDuration(seconds) {
    if (!seconds) return 'Bilinmiyor';
    
    const hours = Math.floor(seconds / 3600);
    const minutes = Math.floor((seconds % 3600) / 60);
    const secs = seconds % 60;
    
    if (hours > 0) {
        return `${hours}:${minutes.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
    }
    return `${minutes}:${secs.toString().padStart(2, '0')}`;
}

async function downloadVideo() {
    if (!currentVideoUrl) {
        showStatus('Önce video bilgilerini alın', 'error');
        return;
    }
    
    const format = document.querySelector('input[name="format"]:checked').value;
    const quality = document.getElementById('quality-select').value;
    
    const btn = event.target;
    btn.classList.add('loading');
    btn.disabled = true;
    
    showStatus('İndiriliyor... Lütfen bekleyin', 'info');
    
    try {
        const response = await fetch('/api/download', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                url: currentVideoUrl,
                format: format,
                quality: quality
            })
        });
        
        const data = await response.json();
        
        if (response.ok) {
            showStatus('✅ İndirme hazır! Dosya indiriliyor...', 'success');
            
            // Dosyayı indir
            const downloadUrl = `/api/download-file/${data.file_id}`;
            const a = document.createElement('a');
            a.href = downloadUrl;
            a.download = data.filename + data.extension;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            
            setTimeout(() => {
                showStatus('✅ İndirme tamamlandı!', 'success');
            }, 1000);
        } else {
            showStatus('❌ ' + (data.error || 'İndirme başarısız'), 'error');
        }
    } catch (error) {
        showStatus('❌ Bağlantı hatası: ' + error.message, 'error');
    } finally {
        btn.classList.remove('loading');
        btn.disabled = false;
    }
}

function showStatus(message, type) {
    const statusDiv = document.getElementById('download-status');
    statusDiv.textContent = message;
    statusDiv.className = 'download-status ' + type;
}

// Format değiştiğinde kalite seçeneğini göster/gizle
document.addEventListener('DOMContentLoaded', () => {
    const formatRadios = document.querySelectorAll('input[name="format"]');
    const qualityGroup = document.getElementById('quality-group');
    
    formatRadios.forEach(radio => {
        radio.addEventListener('change', (e) => {
            if (e.target.value === 'audio') {
                qualityGroup.style.display = 'none';
            } else {
                qualityGroup.style.display = 'block';
            }
        });
    });
    
    // Modal dışına tıklandığında kapat
    document.querySelectorAll('.modal').forEach(modal => {
        modal.addEventListener('click', (e) => {
            if (e.target === modal) {
                closeModal();
            }
        });
    });
    
    // Enter tuşu ile video bilgisi al
    document.getElementById('video-url').addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            getVideoInfo();
        }
    });
});
