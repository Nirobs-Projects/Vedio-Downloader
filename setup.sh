#!/bin/bash

# কালার কোড
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' 

echo -e "${CYAN}🚀 NIROB Downloader - অটোমেটিক সেটআপ শুরু হচ্ছে...${NC}"

# টারমাক্স স্টোরেজ সেটআপ (শুধুমাত্র অ্যান্ড্রয়েড টারমাক্সের জন্য)
if [ -d "$HOME" ] && [ ! -d "$HOME/storage" ]; then
    echo -e "${YELLOW}📂 স্টোরেজ পারমিশন চাওয়া হচ্ছে, দয়া করে Allow করুন...${NC}"
    termux-setup-storage
    sleep 5
fi

# সিস্টেম আপডেট এবং প্রয়োজনীয় টুলস ইনস্টল
echo -e "${YELLOW}📦 সিস্টেম আপডেট এবং FFmpeg, NodeJS ইনস্টল করা হচ্ছে...${NC}"
if command -v pkg &> /dev/null; then
    pkg update -y && pkg upgrade -y
    pkg install python ffmpeg nodejs -y
elif command -v apt &> /dev/null; then
    sudo apt update && sudo apt install python3 python3-pip ffmpeg nodejs -y
fi

# পাইথন প্যাকেজ ইনস্টল
echo -e "${YELLOW}📥 পাইথন লাইব্রেরিগুলো (yt-dlp, mutagen, curl_cffi) ইনস্টল হচ্ছে...${NC}"
pip install -r requirements.txt

echo -e "${GREEN}✅ সেটআপ সফলভাবে সম্পন্ন হয়েছে!${NC}"
echo -e "${CYAN}🚀 এখন প্রোগ্রামটি চালাতে লিখুন: python downloader.py${NC}"