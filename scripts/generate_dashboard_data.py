import pandas as pd
import json
import os
import re

# Paths
LJ_FILE = 'materials/1.LJ/data/final_posts.csv'
FB_FILE = 'materials/2.fb_dsisaev/processed/posts_cleaned.json'
YT_FILE = 'materials/3.yt/yt_classified.csv'
OUTPUT_DATA = 'dashboard/data.json'

def clean_list(val):
    if pd.isna(val) or val == '' or val == 'Нет':
        return []
    if isinstance(val, list):
        return val
    return [x.strip() for x in str(val).split(',')]

def generate_data():
    master_data = []

    # 1. Process LJ
    if os.path.exists(LJ_FILE):
        lj_df = pd.read_csv(LJ_FILE)
        for _, row in lj_df.iterrows():
            master_data.append({
                "source": "LJ",
                "id": str(row.get('Num', '')),
                "title": str(row.get('Title', 'Без заголовка')),
                "date": str(row.get('Date', '')),
                "categories": clean_list(row.get('Categories', '')),
                "tags": clean_list(row.get('Tags', '')),
                "content": str(row.get('Full Content', '')),
                "url": str(row.get('URL', ''))
            })
        print(f"Added {len(lj_df)} LJ posts.")

    # 2. Process FB
    if os.path.exists(FB_FILE):
        with open(FB_FILE, 'r', encoding='utf-8') as f:
            fb_posts = json.load(f)
        for post in fb_posts:
            master_data.append({
                "source": "FB",
                "id": str(post.get('id', '')),
                "title": "Facebook Post", # FB often has no title
                "date": str(post.get('date', '')),
                "categories": post.get('categories', []),
                "tags": post.get('tags', []),
                "content": str(post.get('content', '')),
                "url": str(post.get('url', ''))
            })
        print(f"Added {len(fb_posts)} FB posts.")

    # 3. Process YT
    if os.path.exists(YT_FILE):
        yt_df = pd.read_csv(YT_FILE)
        for _, row in yt_df.iterrows():
            master_data.append({
                "source": "YT",
                "id": str(row.get('video_id', '')),
                "title": str(row.get('title', 'YouTube Video')),
                "date": str(row.get('date', '')),
                "categories": clean_list(row.get('LJ_Categories', '')),
                "tags": clean_list(row.get('LJ_Tags', '')),
                "content": str(row.get('summary', '')),
                "url": str(row.get('url', '')),
                "duration": str(row.get('duration', ''))
            })
        print(f"Added {len(yt_df)} YT videos.")

    # Save to JS (to bypass CORS when opening locally)
    with open('dashboard/data.js', 'w', encoding='utf-8') as f:
        f.write("const MASTER_DATA = ")
        json.dump(master_data, f, ensure_ascii=False, indent=2)
        f.write(";")
    print(f"Master data saved to dashboard/data.js")

if __name__ == "__main__":
    generate_data()
