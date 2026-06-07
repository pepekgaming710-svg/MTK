# 🎬 Grafik Invers Aljabar 3D — Manim Animation

Animasi 3D yang menampilkan fungsi paraboloid `f(x,y) = x² + y²` dan invers aljabarnya.

---

## ⚙️ Persiapan Awal (Sekali Saja)

### 1. Install Python
Download Python 3.8+ dari https://python.org — pastikan centang **"Add to PATH"** saat install.

### 2. Install FFmpeg
- **Windows**: Download dari https://ffmpeg.org/download.html, extract, lalu tambahkan ke PATH.
  - Atau pakai winget: `winget install ffmpeg`
- **Mac**: `brew install ffmpeg`
- **Linux**: `sudo apt install ffmpeg`

### 3. Install LaTeX (untuk render rumus matematika)
- **Windows**: Download MiKTeX dari https://miktex.org/download
- **Mac**: `brew install --cask mactex`
- **Linux**: `sudo apt install texlive-full`

---

## 🚀 Cara Menjalankan di VSCode

### Metode 1 — Terminal VSCode (Paling Mudah)
Buka terminal di VSCode (`Ctrl+`` ` ``), lalu ketik:

```bash
# Install dependencies dulu (sekali saja)
pip install -r requirements.txt

# Render video kualitas HD (1080p)
manim -pqh inverse_algebra_3d.py InverseAlgebra3D

# Atau render cepat untuk preview (480p)
manim -pql inverse_algebra_3d.py InverseAlgebra3D
```

### Metode 2 — VSCode Tasks (Ctrl+Shift+B)
1. Tekan `Ctrl+Shift+B`
2. Pilih salah satu task:
   - **🎬 Render HD (1080p)** — kualitas tinggi
   - **⚡ Render Cepat (480p preview)** — lebih cepat
   - **📦 Install Dependencies** — install manim pertama kali

### Metode 3 — Run & Debug (F5)
1. Tekan `F5` atau klik ikon ▶️ di sidebar
2. Pilih konfigurasi:
   - **🎬 Manim - Render HD**
   - **⚡ Manim - Preview Cepat**

---

## 📁 Hasil Video
Setelah render, video tersimpan di:
```
media/videos/inverse_algebra_3d/
├── 480p15/    ← hasil render cepat (-ql)
└── 1080p60/   ← hasil render HD (-qh)
```

---

## 🎛️ Opsi Kualitas Render

| Perintah | Resolusi | FPS | Kecepatan |
|----------|----------|-----|-----------|
| `-ql` | 480p | 15 | ⚡ Cepat |
| `-qm` | 720p | 30 | 🔸 Sedang |
| `-qh` | 1080p | 60 | 🐢 Lambat |
| `-qk` | 2160p (4K) | 60 | 🐢🐢 Sangat Lambat |

---

## ❓ Troubleshooting

**Error: `manim not found`**
→ Jalankan `pip install manim` di terminal

**Error: `ffmpeg not found`**
→ Install FFmpeg dan pastikan sudah ada di PATH sistem

**Error: LaTeX / MathTex gagal**
→ Install MiKTeX (Windows) atau texlive (Linux/Mac)

**Render sangat lambat**
→ Gunakan `-ql` untuk preview dulu sebelum render HD
