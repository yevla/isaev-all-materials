import json
import os
import re
from datetime import datetime

# Настройки путей
BASE_DIR = r"c:\Users\poezd\Downloads\antigravity projects\isaev_materials"
INPUT_FILE = os.path.join(BASE_DIR, "materials", "2.fb_dsisaev", "posts_profile1_dsisaev.json")
OUTPUT_DIR = os.path.join(BASE_DIR, "materials", "2.fb_dsisaev", "processed")
MD_DIR = os.path.join(OUTPUT_DIR, "markdown")

# Месяцы для парсинга дат FB
MONTHS = {
    "янв": "01", "фев": "02", "мар": "03", "апр": "04", "май": "05", "июн": "06",
    "июл": "07", "авг": "08", "сен": "09", "окт": "10", "ноя": "11", "дек": "12"
}

def clean_content(text):
    if not text:
        return ""
    
    # 1. Удаление внутренних дублей (часто текст повторяется 2 раза)
    # Разбиваем по характерным разделителям FB скрапинга или просто ищем повтор
    # Сначала пробуем разделить по "\n" и найти циклическое повторение
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    n = len(lines)
    if n > 1:
        # Простая проверка на дублирование блоков
        half = n // 2
        if n % 2 == 0 and lines[:half] == lines[half:]:
            lines = lines[:half]
        elif n > 2:
            # Более сложная проверка (бывает 3 повтора или небольшие отличия в конце)
            # Берем первый длинный блок
            unique_lines = []
            for line in lines:
                if line not in unique_lines:
                    unique_lines.append(line)
            lines = unique_lines

    content = "\n\n".join(lines)

    # 2. Удаление технического мусора (реклама консультаций)
    # Пример: "Записаться на консультацию -->> +972 53-336-8817"
    junk_patterns = [
        r"(?i)Записаться на консультацию.*?\+?\d[\d\-\s]{7,}\d",
        r"(?i)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
        r"(?i)~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~",
        r"(?i)Рис\.\s+[А-Яа-я\s]+",
        r"(?i)Рисунок\s+[А-Яа-я\s]+"
    ]
    
    for pattern in junk_patterns:
        content = re.sub(pattern, "", content)
    
    return content.strip()

def normalize_date(date_str):
    # Пример: "30 май 2018 г." -> "2018-05-30"
    try:
        match = re.search(r"(\d+)\s+([а-я]+)\s+(\d{4})", date_str.lower())
        if match:
            day, month_text, year = match.groups()
            month = MONTHS.get(month_text[:3], "01")
            return f"{year}-{month}-{int(day):02d}"
    except:
        pass
    return date_str # Возвращаем оригинал если не вышло

def main():
    if not os.path.exists(MD_DIR):
        os.makedirs(MD_DIR)

    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)

    cleaned_data = []
    for i, item in enumerate(data):
        content = item.get("content", "")
        if not content and not item.get("has_images"):
            continue
            
        clean_text = clean_content(content)
        iso_date = normalize_date(item.get("date", ""))
        
        # Создаем очищенный объект
        cleaned_item = {
            "id": i,
            "date": iso_date,
            "url": item.get("url"),
            "content": clean_text,
            "comments_count": item.get("comments_count"),
            "has_images": item.get("has_images")
        }
        cleaned_data.append(cleaned_item)
        
        # Создаем Markdown
        title = clean_text[:50].replace("\n", " ") + "..." if clean_text else f"Post_{iso_date}_{i}"
        filename = f"{iso_date}_{i}.md".replace(":", "-")
        filepath = os.path.join(MD_DIR, filename)
        
        with open(filepath, 'w', encoding='utf-8') as md_f:
            md_f.write(f"---")
            md_f.write(f"\ndate: {iso_date}")
            md_f.write(f"\nurl: {item.get('url')}")
            md_f.write(f"\ncomments: {item.get('comments_count')}")
            md_f.write(f"\n---\n\n")
            md_f.write(clean_text)

    # Сохраняем общий JSON
    with open(os.path.join(OUTPUT_DIR, "posts_cleaned.json"), 'w', encoding='utf-8') as f:
        json.dump(cleaned_data, f, ensure_ascii=False, indent=2)

    # Безопасный вывод для Windows
    try:
        print(f"Обработано {len(cleaned_data)} постов.")
    except UnicodeEncodeError:
        print(f"Processed {len(cleaned_data)} posts.")

if __name__ == "__main__":
    main()
