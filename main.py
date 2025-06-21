import xml.etree.ElementTree as ET
import requests, time, os
from dotenv import load_dotenv

load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_TOKEN")  # Replace with your Notion integration token
DATABASE_ID = os.getenv("DATABASE_ID")  # Replace with your database ID

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Notion-Version": "2022-06-28",
    "Content-Type": "application/json"
}

def parse_mal_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    anime_list = []

    for anime in root.findall('anime'):
        status = anime.find('my_status').text
        if status == 'Plan to Watch':
            anime_id = anime.find('series_animedb_id').text
            title = anime.find('series_title').text
            anime_list.append({
                'id': anime_id,
                'title': title
            })
    return anime_list

def get_community_score(anime_id):
    url = f"https://api.jikan.moe/v4/anime/{anime_id}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['data'].get('score', None)
        else:
            print(f"Error fetching ID {anime_id}: {response.status_code}")
            return None
    except Exception as e:
        print(f"Request failed for ID {anime_id}: {e}")
        return None

def add_to_notion(title, score):
    create_url = "https://api.notion.com/v1/pages"

    data = {
        "parent": {"database_id": DATABASE_ID},
        "properties": {
            "Name of title": {
                "title": [
                    {
                        "text": {
                            "content": title
                        }
                    }
                ]
            },
            "Rating (1-10)": {
                "number": float(score) if score else 0
            }
        }
    }
    response = requests.post(create_url, headers=headers, json=data)
    if response.status_code == 200 or response.status_code == 201:
        print(f"Added to Notion: {title} with score {score}")
    else:
        print(f"Failed to add {title} to Notion: {response.status_code}, {response.text}")

if __name__ == "__main__":
    input_file = "animelist.xml"  # Your MAL export XML change name of this or of the file to match it :)
    anime_list = parse_mal_xml(input_file)

    for anime in anime_list:
        score = get_community_score(anime['id'])
        if score is None:
            score = 0
        print(anime['title'], score)
        add_to_notion(anime['title'], score)
        time.sleep(1)  # avoid API rate limits