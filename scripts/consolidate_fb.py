import json
import pandas as pd
import os
import shutil

# Config
INPUT_JSON = 'materials/2.fb_dsisaev/processed/posts_cleaned.json'
OUTPUT_CSV = 'materials/2.fb_dsisaev/fb_classified.csv'
MARKDOWN_DIR = 'materials/2.fb_dsisaev/processed/markdown'

def main():
    # 1. Read JSON
    if not os.path.exists(INPUT_JSON):
        print(f"Error: {INPUT_JSON} not found.")
        return

    with open(INPUT_JSON, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print(f"Loaded {len(data)} items from JSON.")

    # 2. Convert to DataFrame
    rows = []
    for item in data:
        row = {
            'id': item.get('id'),
            'date': item.get('date'),
            'content': item.get('content'),
            'url': item.get('url'),
            'categories': ','.join(item.get('categories', [])),
            'tags': ','.join(item.get('tags', [])),
            'comments_count': item.get('comments_count'),
            'has_images': item.get('has_images')
        }
        rows.append(row)

    df = pd.DataFrame(rows)
    
    # 3. Save CSV
    df.to_csv(OUTPUT_CSV, index=False, encoding='utf-8')
    print(f"Saved CSV to {OUTPUT_CSV}")

    # 4. Remove Markdown Directory
    if os.path.exists(MARKDOWN_DIR):
        try:
            shutil.rmtree(MARKDOWN_DIR)
            print(f"Deleted DataFrame directory: {MARKDOWN_DIR}")
        except Exception as e:
            print(f"Error deleting directory: {e}")
    else:
        print("Markdown directory not found, skipping delete.")

if __name__ == "__main__":
    main()
