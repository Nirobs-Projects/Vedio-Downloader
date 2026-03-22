# 🚀 Ultimate Downloader

A professional, high-speed, and CLI-based video/audio downloader designed for **Android (Termux)**, **Linux**, and **Windows**. It leverages the power of `yt-dlp` to provide a seamless downloading experience from YouTube, Facebook, Instagram, and 1000+ other platforms.

---

## ✨ Features

- **⚡ Auto Best Quality:** Automatically fetches and downloads the highest resolution available (up to 4K/8K).
- **🇧🇩 Auto Bangla Subtitles:** One-click download with Bangla subtitles embedded directly into the video.
- **🎵 MP3 Extraction:** High-quality 192kbps audio extraction with original thumbnail as cover art.
- **📂 Playlist Support:** Download entire playlists effortlessly with organized folder structures.
- **📊 Progress Bar Animation:** A professional, real-time loading bar showing download percentage, speed, and ETA.
- **📱 Termux & PC Friendly:** Optimized storage paths for both Android Gallery and PC Downloads folder.
- **🛡️ Anti-Bot Bypass:** Integrated custom headers to avoid "Too Many Requests" errors.

---

## 🛠️ Installation Guide

### 📱 For Termux (Android)
Open Termux and run these commands one by one:

git clone https://github.com/Nirobs-Projects/Vedio-Downloader.git
cd Vedio-Downloader
chmod +x setup.sh
./setup.sh
python downloader.py

### 💻 For Linux / Windows
1. Install Dependencies: Make sure you have Python 3 and FFmpeg installed.
2. Then run: pip install -r requirements.txt
3. Start the tool: python downloader.py

---

## 🚀 How to Use

1. **Start the Script:** Type `python downloader.py` and hit Enter.
2. **Paste Link:** Right-click or long-press to paste the video or playlist URL.
3. **Choose Your Option:**
   - **Option 1:** Best video quality (No Subtitles).
   - **Option 2:** Best video quality + **Bangla Subtitles** (Auto-Embed).
   - **Option 3:** Manually select resolution (e.g., 720p, 1080p).
   - **Option 4:** Download as **MP3 Audio**.
   - **Option 5:** Download an entire **Playlist**.
4. **Download:** Watch the animated progress bar do its magic!

---

## 📂 Download Location

- **Termux (Android):** Files are saved directly to your phone's main download folder:  
  `Internal Storage > Downloads > UltimateDownloader`
- **PC (Windows/Linux):** Files are saved in your default download path:  
  `Downloads > UltimateDownloader`

---

## 📦 Requirements

The tool is powered by:
- `yt-dlp` - The core downloading engine.
- `FFmpeg` - For merging high-quality video and audio.
- `mutagen` - For handling audio metadata and thumbnails.
- `curl_cffi` - To bypass platform security blocks.

---

## 📜 Disclaimer
*This tool is developed for educational and personal use only. The developer is not responsible for any misuse. Please respect the copyright terms of the content owners.*

---
Developed with ❤️ by **[NIROB](https://github.com/Nirobs-Projects)**
