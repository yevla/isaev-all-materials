import pandas as pd
import json
import re

TAXONOMY_FILE = 'materials/1.LJ/data/categories.txt'
YT_FILE = 'materials/3.yt/notebooklm_merged_final.csv'
OUTPUT_FILE = 'materials/3.yt/yt_classified.csv'

# Mapping YT columns to English
HEADER_MAP = {
    "Title": "title",
    "Участники": "participants",
    "Название по содержанию": "summary_title",
    "Краткое содержание": "summary",
    "Категории": "yt_categories",
    "URL": "url",
    "ID": "video_id",
    "Date (YYYY-M-D)": "date",
    "Duration": "duration",
    "Likes": "likes",
    "Views": "views",
    "Comments": "comments"
}

def load_taxonomy():
    taxonomy = {}
    with open(TAXONOMY_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            if ':' in line and not line.startswith('#'):
                cat, tags = line.split(':')
                cat = cat.strip()
                tags_list = [t.strip() for t in tags.split(',')]
                taxonomy[cat] = tags_list
    return taxonomy

def classify_row(row, taxonomy):
    text = f"{row['Название по содержанию']} {row['Краткое содержание']} {row['Категории']}".lower()
    
    found_categories = []
    found_tags = []
    
    # Priority tags (if we find a specific tag, its category follows)
    for cat, tags in taxonomy.items():
        for tag in tags:
            # Check for whole word match
            if re.search(rf'\b{tag.lower()}\b', text):
                if tag not in found_tags:
                    found_tags.append(tag)
                if cat not in found_categories:
                    found_categories.append(cat)

    # Basic category mapping based on YT 'Категории' if nothing found yet
    yt_cats = str(row['Категории']).lower()
    if not found_categories:
        if 'психология' in yt_cats: found_categories.append('Психология')
        if 'медицина' in yt_cats or 'здоровье' in yt_cats: found_categories.append('Медицина')
        if 'отношения' in yt_cats or 'родительство' in yt_cats: found_categories.append('Личное')

    # Ensure uniqueness and priority
    # Let's say top 2 categories and top 4 tags
    return ", ".join(found_categories[:2]), ", ".join(found_tags[:5])

def main():
    df = pd.read_csv(YT_FILE)
    taxonomy = load_taxonomy()
    
    print(f"Loaded {len(df)} rows from YT CSV.")
    
    lj_categories = []
    lj_tags = []
    
    for _, row in df.iterrows():
        cats, tags = classify_row(row, taxonomy)
        lj_categories.append(cats)
        lj_tags.append(tags)
        
    df['LJ_Categories'] = lj_categories
    df['LJ_Tags'] = lj_tags
    
    # Translate headers
    df_english = df.rename(columns=HEADER_MAP)
    
    # Add newly created columns to map if they weren't there
    # But rename manual step is safer
    
    df_english.to_csv(OUTPUT_FILE, index=False, encoding='utf-8-sig')
    print(f"Saved classified and translated data to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
