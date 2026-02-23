import csv
import os

def convert_fb():
    input_file = r'materials\2.fb_dsisaev\fb_classified.csv'
    output_file = r'materials\2.fb_dsisaev\FB_posts.md'
    
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    with open(input_file, mode='r', encoding='utf-8') as infile, \
         open(output_file, mode='w', encoding='utf-8') as outfile:
        
        reader = csv.DictReader(infile)
        for row in reader:
            date = row.get('date', '').strip()
            content = row.get('content', '').strip()
            categories = row.get('categories', '').strip()
            tags = row.get('tags', '').strip()
            
            # Пропускаем пустые посты
            if not content:
                continue
                
            outfile.write(f"# FB Пост от {date}\n")
            
            meta_parts = []
            if categories:
                meta_parts.append(f"**Категории:** {categories}")
            if tags:
                meta_parts.append(f"**Теги:** {tags}")
                
            if meta_parts:
                outfile.write(" | ".join(meta_parts) + "\n")
                
            outfile.write("\n")
            outfile.write(content + "\n\n---\n\n")

if __name__ == '__main__':
    convert_fb()
    print("Facebook Markdown file generated successfully without comment counts.")
