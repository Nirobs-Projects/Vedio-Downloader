#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
import yt_dlp
import traceback

# কালার কোডসমূহ
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"
BOLD = "\033[1m"

# ==============================
# Setup Directories (Termux & PC)
# ==============================
# টারমাক্সে ফোনের গ্যালারিতে দেখানোর জন্য মেইন ডাউনলোড ফোল্ডার টার্গেট করবে
termux_path = os.path.expanduser("~/storage/downloads")
if os.path.exists(termux_path):
    BASE_DIR = os.path.join(termux_path, "UltimateDownloader")
else:
    BASE_DIR = os.path.expanduser("~/Downloads/UltimateDownloader")

VIDEO_DIR = os.path.join(BASE_DIR, "Videos")
PLAYLIST_DIR = os.path.join(BASE_DIR, "Playlists")

os.makedirs(VIDEO_DIR, exist_ok=True)
os.makedirs(PLAYLIST_DIR, exist_ok=True)

# ==============================
# GUI & Banner
# ==============================
def show_banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    banner = f"""{RED}{BOLD}
    
 ███╗   ██╗██╗██████╗  ██████╗ ██████╗ 
 ████╗  ██║██║██╔══██╗██╔═══██╗██╔══██╗
 ██╔██╗ ██║██║██████╔╝██║   ██║██████╔╝
 ██║╚██╗██║██║██╔══██╗██║   ██║██╔══██╗
 ██║ ╚████║██║██║  ██║╚██████╔╝██████╔╝
 ╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ 
                                       
    {CYAN}--- Multi-Platform Video Downloader ---{RESET}
    """
    print(banner)

def print_menu():
    print(f"{YELLOW}{BOLD}========= 🎛 MAIN MENU =========")
    print(f"{WHITE}1) ⚡ Auto Best Quality (No Sub)")
    print(f"2) 🇧🇩 Auto Best + Bangla Subtitle")
    print(f"3) 🎬 Choose Quality Manually")
    print(f"4) 🎵 Audio Only (MP3)")
    print(f"5) 📂 Playlist Download")
    print(f"{YELLOW}================================{RESET}")

# ==============================
# Progress Hook with Animation
# ==============================
def progress_hook(d):
    if d['status'] == 'downloading':
        # পারসেন্টেজ বের করা
        p_str = d.get('_percent_str', '0%').replace('%','')
        try:
            p = float(p_str)
        except:
            p = 0
            
        # এনিমেশন লাইন (Progress Bar)
        bar_width = 25
        filled = int(p * bar_width / 100)
        bar = '█' * filled + '░' * (bar_width - filled)
        
        # স্পিড এবং ইটিএ
        speed = d.get('_speed_str', 'N/A')
        eta = d.get('_eta_str', 'N/A')
        
        # এক লাইনে আউটপুট
        sys.stdout.write(f"\r{GREEN}⚡ [{bar}] {p:>5}% | {speed} | ETA: {eta}{RESET}")
        sys.stdout.flush()
        
    elif d['status'] == 'finished':
        print(f"\n{CYAN}✅ Download Complete! Finalizing file...{RESET}")

# ==============================
# Manual Format Picker
# ==============================
def get_manual_format(url):
    print(f"\n{CYAN}📊 Fetching available formats...{RESET}")
    os.system(f'yt-dlp --user-agent "Mozilla/5.0" -F "{url}"')
    code = input(f"\n{BOLD}{YELLOW}👉 Enter format code (e.g., 137+251): {RESET}").strip()
    return code if code else "bv*+ba/best"

# ==============================
# Main Process
# ==============================
def main():
    show_banner()
    
    print(f"{BOLD}{CYAN}📥 Paste link (YouTube/FB/Insta/etc):{RESET}")
    url = input(f"{RED}>>> {RESET}").strip()

    if not url:
        print(f"\n{RED}❌ Error: No link provided!{RESET}")
        return

    print()
    print_menu()
    opt = input(f"{BOLD}{YELLOW}Choice (1-5): {RESET}").strip()

    # ডিফল্ট সেটিংস
    ydl_opts = {
        'format': 'bv*+ba/best',
        'merge_output_format': 'mp4',
        'outtmpl': os.path.join(VIDEO_DIR, '%(title)s.%(ext)s'),
        'writethumbnail': True,
        'http_headers': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
        },
        'writeinfojson': False,
        'progress_hooks': [progress_hook],
        'continuedl': True,
        'retries': 10,
        'noplaylist': True,
        'postprocessors': [{'key': 'FFmpegMetadata'}, {'key': 'EmbedThumbnail'}]
    }

    # অপশন অনুযায়ী সেটিংস পরিবর্তন
    if opt == "2":
        # বাংলা সাবটাইটেল এম্বেড লজিক
        ydl_opts.update({
            'writesubtitles': True,
            'writeautomaticsub': True,
            'subtitleslangs': ['bn', 'bn.*', 'bn-BD'],
            'subtitlesformat': 'srt/best',
        })
        ydl_opts['postprocessors'].insert(0, {'key': 'FFmpegSubtitlesConvertor', 'format': 'srt'})
        ydl_opts['postprocessors'].insert(1, {'key': 'FFmpegEmbedSubtitle'})

    elif opt == "3":
        ydl_opts['format'] = get_manual_format(url)

    elif opt == "4":
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [
                {'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', 'preferredquality': '192'},
                {'key': 'FFmpegMetadata'},
                {'key': 'EmbedThumbnail'},
            ]
        })

    elif opt == "5":
        ydl_opts.update({
            'outtmpl': os.path.join(PLAYLIST_DIR, '%(playlist_title)s/%(title)s.%(ext)s'),
            'noplaylist': False
        })

    print(f"\n{YELLOW}🚀 Requesting from server...{RESET}\n")
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"\n{BOLD}{GREEN}🎉 Success! Check your downloads.{RESET}")
        print(f"{WHITE}📂 Path: {BASE_DIR}{RESET}")
    except Exception:
        print(f"\n{RED}❌ Error occurred while downloading!{RESET}")
        traceback.print_exc()

if __name__ == "__main__":
    main()