import requests
from bs4 import BeautifulSoup
import json

# Replace with your PSNProfiles URL
URL = "https://psnprofiles.com/raymystyro/trophies/6622-thehunter-call-of-the-wild"

def sync():
    response = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(response.text, 'html.parser')
    
    trophies = []
    # This finds every trophy row on the page
    rows = soup.find_all('tr')
    
    for row in rows:
        title_info = row.find('a', class_='title')
        if title_info:
            name = title_info.text.strip()
            # Check if the row has an 'earned' class or date
            is_done = "completed" in row.get('class', []) or row.find('span', class_='typo-top')
            
            trophies.append({
                "name": name,
                "current": 1 if is_done else 0,
                "goal": 1,
                "status": "done" if is_done else "prog"
            })
            
    with open('trophies.json', 'w') as f:
        json.dump(trophies, f, indent=2)

sync()
