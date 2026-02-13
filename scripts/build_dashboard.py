import pandas as pd
import json
import os

# Configuration
PATHS = {
    'lj': 'materials/1.LJ/data/final_posts.csv',
    'fb': 'materials/2.fb_dsisaev/processed/posts_cleaned.json',
    'yt': 'materials/3.yt/yt_classified.csv',
    'template': 'dashboard/template.html',
    'output': 'dashboard/index.html'
}

def clean_list(val):
    if pd.isna(val) or val == '' or val == 'Нет':
        return []
    if isinstance(val, list):
        return val
    # Handle CSV list format
    if isinstance(val, str):
        return [x.strip() for x in val.split(',') if x.strip()]
    return []

def collect_data():
    master_data = []

    # 1. LiveJournal
    if os.path.exists(PATHS['lj']):
        try:
            df = pd.read_csv(PATHS['lj'])
            for _, row in df.iterrows():
                master_data.append({
                    "source": "LJ",
                    "id": f"lj_{row.get('Num', '')}",
                    "title": str(row.get('Title', 'Без заголовка')),
                    "date": str(row.get('Date', '')),
                    "categories": clean_list(row.get('Categories')),
                    "tags": clean_list(row.get('Tags')),
                    "content": str(row.get('Full Content', '')),
                    "url": str(row.get('URL', ''))
                })
            print(f"Loaded {len(df)} LJ posts")
        except Exception as e:
            print(f"Error loading LJ: {e}")

    # 2. Facebook
    if os.path.exists(PATHS['fb']):
        try:
            with open(PATHS['fb'], 'r', encoding='utf-8') as f:
                posts = json.load(f)
            for p in posts:
                master_data.append({
                    "source": "FB",
                    "id": f"fb_{p.get('id', '')}",
                    "title": "Facebook Post",
                    "date": str(p.get('date', '')),
                    "categories": p.get('categories', []),
                    "tags": p.get('tags', []),
                    "content": str(p.get('content', '')),
                    "url": str(p.get('url', ''))
                })
            print(f"Loaded {len(posts)} FB posts")
        except Exception as e:
            print(f"Error loading FB: {e}")

    # 3. YouTube
    if os.path.exists(PATHS['yt']):
        try:
            df = pd.read_csv(PATHS['yt'])
            for _, row in df.iterrows():
                # Fix categories/tags being potentially float/nan
                cats = clean_list(row.get('LJ_Categories'))
                tags = clean_list(row.get('LJ_Tags'))
                
                master_data.append({
                    "source": "YT",
                    "id": f"yt_{row.get('video_id', '')}",
                    "title": str(row.get('title', 'YouTube Video')),
                    "date": str(row.get('date', '')),
                    "categories": cats,
                    "tags": tags,
                    "content": str(row.get('summary', '')),
                    "url": str(row.get('url', '')),
                    "duration": str(row.get('duration', ''))
                })
            print(f"Loaded {len(df)} YT videos")
        except Exception as e:
            print(f"Error loading YT: {e}")

    return master_data

def build_dashboard():
    print("Collecting data...")
    data = collect_data()
    
    # Serialize to JSON string
    json_str = json.dumps(data, ensure_ascii=False)
    js_variable = f"const ISAEV_DATA = {json_str};"
    
    # Read Template
    if not os.path.exists(PATHS['template']):
        print("Template not found!")
        return

    with open(PATHS['template'], 'r', encoding='utf-8') as f:
        html = f.read()

    # Inject
    final_html = html.replace('/* DATA_HERE */', js_variable)

    # Write Output
    with open(PATHS['output'], 'w', encoding='utf-8') as f:
        f.write(final_html)
    
    print(f"Dashboard generated at: {os.path.abspath(PATHS['output'])}")
    print(f"Total items: {len(data)}")

if __name__ == "__main__":
    build_dashboard()
