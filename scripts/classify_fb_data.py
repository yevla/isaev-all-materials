import json
import os
import re

# Пути
BASE_DIR = r"c:\Users\poezd\Downloads\antigravity projects\isaev_materials"
JSON_FILE = os.path.join(BASE_DIR, "materials", "2.fb_dsisaev", "processed", "posts_cleaned.json")
MD_DIR = os.path.join(BASE_DIR, "materials", "2.fb_dsisaev", "processed", "markdown")

# Карта классификации {id: {"categories": [], "tags": []}}
CLASSIFICATION_MAP = {
    0: {"categories": ["Психология", "Социум"], "tags": ["Сценарии", "Личность", "Свобода", "Общество"]},
    1: {"categories": ["Психология", "Личное"], "tags": ["Группы", "Отношения"]},
    2: {"categories": ["Психология", "Личное"], "tags": ["Терапия", "Страх", "Семья", "Отношения"]},
    3: {"categories": ["Психология"], "tags": ["Марафоны"]},
    4: {"categories": ["Места"], "tags": ["Израиль"]},
    5: {"categories": ["Психология", "Личное"], "tags": ["Игры", "Сценарии", "Отношения"]},
    6: {"categories": ["Психология", "Места"], "tags": ["Группы", "Израиль", "Природа"]},
    7: {"categories": ["Психология", "Медицина", "Социум"], "tags": ["Психосоматика", "Врачи", "Общество"]},
    8: {"categories": ["Психология"], "tags": ["Психосоматика"]},
    9: {"categories": ["Психология", "Личное"], "tags": ["Игры", "Сценарии", "Отношения"]},
    10: {"categories": [], "tags": []},
    11: {"categories": ["Психология", "Личное"], "tags": ["Радость", "Семья"]},
    12: {"categories": ["Социум", "Психология"], "tags": ["Общество", "Границы", "Манипуляции", "Игры"]},
    13: {"categories": ["Культура", "Психология", "Личное"], "tags": ["Кино", "Личность", "Свобода", "Отношения"]},
    14: {"categories": ["Психология", "Места"], "tags": ["Терапия", "Личность", "Самара"]},
    15: {"categories": ["Психология", "Культура", "Личное"], "tags": ["Терапия", "Книги", "Близость"]},
    16: {"categories": ["Психология"], "tags": ["Личность", "Свобода"]},
    17: {"categories": ["Психология"], "tags": ["Терапия", "Психосоматика"]},
    18: {"categories": ["Социум", "Психология", "Места"], "tags": ["Общество", "Группы", "Самара", "Волга"]},
    19: {"categories": [], "tags": []},
    20: {"categories": [], "tags": []},
    21: {"categories": ["Культура"], "tags": ["Блогинг"]},
    22: {"categories": ["Личное", "Психология"], "tags": ["Семья", "Сценарии", "Игры", "Манипуляции"]},
    23: {"categories": ["Места", "Стиль"], "tags": ["Израиль", "Самара", "Технологии"]},
    24: {"categories": ["Психология", "Личное"], "tags": ["Группы", "Марафоны", "Отношения"]},
    25: {"categories": ["Психология"], "tags": ["Группы"]},
    26: {"categories": [], "tags": []},
    27: {"categories": ["Психология"], "tags": ["Страх", "Личность", "Свобода"]},
    28: {"categories": ["Психология"], "tags": ["Группы", "Выбор", "Ответственность", "Свобода"]},
    29: {"categories": ["Психология", "Личное"], "tags": ["Сценарии", "Группы", "Семья", "Воспоминания"]},
    30: {"categories": ["Психология"], "tags": ["Игры", "Сценарии", "Страх", "Терапия"]},
    31: {"categories": ["Психология", "Медицина"], "tags": ["Психосоматика", "Врачи"]},
    32: {"categories": ["Психология", "Места"], "tags": ["Группы", "Самара"]},
    33: {"categories": ["Медицина"], "tags": ["Врачи"]},
    34: {"categories": ["Личное", "Психология"], "tags": ["Отношения", "Любовь", "Игры"]},
    35: {"categories": ["Места"], "tags": ["Израиль", "Природа"]},
    36: {"categories": ["Места", "Психология"], "tags": ["Израиль", "Группы"]},
    37: {"categories": ["Медицина", "Личное"], "tags": ["Врачи", "Спасение", "Любовь"]},
    38: {"categories": ["Психология", "Места"], "tags": ["Группы", "Самара"]},
    39: {"categories": ["Психология", "Личное"], "tags": ["Отношения", "Игры", "Сценарии"]},
    40: {"categories": ["Личное", "Психология"], "tags": ["Отношения", "Игры", "Манипуляции"]},
    41: {"categories": ["Места", "Психология"], "tags": ["Израиль", "Природа", "Группы"]},
    42: {"categories": ["Психология"], "tags": ["Страх", "Выбор", "Марафоны"]},
    43: {"categories": ["Психология"], "tags": ["Сценарии", "Личность", "Свобода"]},
    44: {"categories": ["Психология", "Места"], "tags": ["Терапия", "Группы", "Самара"]},
    45: {"categories": ["Психология", "Социум"], "tags": ["Терапия", "Личность", "Общество"]},
    46: {"categories": ["Психология", "Места"], "tags": ["Группы", "Природа"]},
    47: {"categories": ["Психология", "Личное"], "tags": ["Личность", "Свобода", "Отношения"]},
    48: {"categories": ["Психология", "Места"], "tags": ["Группы", "Марафоны", "Израиль", "Самара"]},
    49: {"categories": ["Психология", "Места"], "tags": ["Марафоны", "Самара"]},
    50: {"categories": ["Психология", "Личное"], "tags": ["Страх", "Терапия", "Семья", "Отношения"]},
    51: {"categories": ["Психология"], "tags": ["Ответственность", "Свобода"]},
    52: {"categories": ["Психология"], "tags": ["Терапия", "Группы"]},
    53: {"categories": ["Психология", "Личное"], "tags": ["Свобода", "Личность", "Семья"]},
    54: {"categories": ["Психология", "Личное"], "tags": ["Сценарии", "Ответственность", "Родители", "Воспоминания"]},
    55: {"categories": ["Места", "Психология"], "tags": ["Природа", "Израиль", "Группы"]},
    56: {"categories": ["Психология"], "tags": ["Терапия"]},
    57: {"categories": [], "tags": []},
    58: {"categories": [], "tags": []},
    59: {"categories": ["Психология", "Личное"], "tags": ["Игры", "Сценарии", "Отношения"]},
    60: {"categories": ["Психология", "Места"], "tags": ["Группы", "Израиль"]},
    61: {"categories": ["Психология", "Личное"], "tags": ["Группы", "Отношения"]},
    62: {"categories": ["Психология", "Личное"], "tags": ["Личность", "Отношения"]},
    63: {"categories": ["Психология", "Личное"], "tags": ["Игры", "Сценарии", "Отношения"]},
    64: {"categories": ["Психология"], "tags": ["Терапия", "Личность", "Свобода"]},
    65: {"categories": ["Психология", "Личное"], "tags": ["Игры", "Сценарии", "Отношения"]},
    66: {"categories": ["Психология", "Личное"], "tags": ["Свобода", "Личность", "Дети"]},
    67: {"categories": ["Психология"], "tags": ["Марафоны"]},
    68: {"categories": ["Психология", "Личное"], "tags": ["Сценарии", "Группы", "Ответственность", "Родители", "Семья"]},
    69: {"categories": ["Психология", "Личное", "Медицина"], "tags": ["Группы", "Семья", "Дети", "Врачи"]},
    70: {"categories": ["Личное", "Психология"], "tags": ["Отношения", "Воспоминания", "Свобода", "Личность"]},
    71: {"categories": ["Психология"], "tags": ["Марафоны", "Вина", "Обида", "Свобода"]},
    72: {"categories": ["Психология", "Личное"], "tags": ["Радость", "Семья"]},
    73: {"categories": [], "tags": []},
    74: {"categories": ["Психология", "Места"], "tags": ["Группы", "Марафоны", "Израиль", "Самара"]},
    75: {"categories": ["Психология", "Личное"], "tags": ["Терапия", "Группы", "Марафоны", "История"]},
    76: {"categories": ["Психология", "Личное"], "tags": ["Личность", "Свобода", "Семья", "Отношения"]},
    77: {"categories": ["Медицина", "Психология"], "tags": ["Врачи", "Спасение", "Терапия"]},
    78: {"categories": ["Психология", "Личное"], "tags": ["Терапия", "Группы", "Семья"]},
    79: {"categories": ["Психология", "Личное"], "tags": ["Сценарии", "Вина", "Обида", "Отношения"]},
    80: {"categories": ["Психология", "Места"], "tags": ["Группы", "Природа", "Израиль"]},
    81: {"categories": ["Психология", "Места"], "tags": ["Группы", "Израиль"]},
}

def update_json():
    with open(JSON_FILE, 'r', encoding='utf-8') as f:
        posts = json.load(f)
    
    for post in posts:
        post_id = post.get("id")
        if post_id in CLASSIFICATION_MAP:
            post["categories"] = CLASSIFICATION_MAP[post_id]["categories"]
            post["tags"] = CLASSIFICATION_MAP[post_id]["tags"]
    
    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)
    print(f"Updated {JSON_FILE}")

def update_markdown():
    for filename in os.listdir(MD_DIR):
        if not filename.endswith(".md"):
            continue
        
        filepath = os.path.join(MD_DIR, filename)
        
        # Извлекаем ID из имени файла (format: YYYY-MM-DD_ID.md)
        try:
            # Берем часть после последнего подчеркивания и до .md
            post_id_str = filename.split("_")[-1].replace(".md", "")
            post_id = int(post_id_str)
        except Exception as e:
            print(f"Skipping {filename}: could not extract ID ({e})")
            continue
        
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        if post_id in CLASSIFICATION_MAP:
            cats = CLASSIFICATION_MAP[post_id]["categories"]
            tags = CLASSIFICATION_MAP[post_id]["tags"]
            
            new_yaml_lines = []
            content_start_index = -1
            
            # Разбираем YAML
            if lines[0].strip() == "---":
                for i in range(1, len(lines)):
                    if lines[i].strip() == "---":
                        content_start_index = i + 1
                        break
                    # Пропускаем старые категории и теги, если они были
                    if lines[i].startswith("categories:") or lines[i].startswith("tags:"):
                        continue
                    new_yaml_lines.append(lines[i])
            
            # Формируем новый файл
            final_lines = ["---\n"]
            final_lines.extend(new_yaml_lines)
            final_lines.append(f"id: {post_id}\n") # Добавим ID для будущего
            if cats:
                final_lines.append(f"categories: {cats}\n")
            if tags:
                final_lines.append(f"tags: {tags}\n")
            final_lines.append("---\n")
            
            if content_start_index != -1:
                final_lines.extend(lines[content_start_index:])
            else:
                final_lines.extend(lines)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.writelines(final_lines)
            print(f"Updated {filename}")

if __name__ == "__main__":
    update_json()
    update_markdown()
