from datetime import datetime
import requests
from bs4 import BeautifulSoup

class Scraper:
    LATVIAN_MONTHS = {
        "JANVāRIS": "January",
        "FEBRUāRIS": "February",
        "MARTS": "March",
        "APRīLIS": "April",
        "MAIJS": "May",
        "JūNIJS": "June",
        "JūLIJS": "July",
        "AUGUSTS": "August",
        "SEPTEMBRIS": "September",
        "OKTOBRIS": "October",
        "NOVEMBRIS": "November",
        "DECEMBRIS": "December"
    }

    def __init__(self, url):
        self.url = url
        self.data = []

    def parse_latvian_date(self, date_str):
        try:
            
            for lv_month, en_month in self.LATVIAN_MONTHS.items():
                if lv_month in date_str:
                    date_str = date_str.replace(lv_month, en_month)
                    break
            
            return datetime.strptime(date_str, "%d.%B,%Y").date()
        except ValueError:
            return None  

    def parse_data(self, soup):
        cats = []
        for cat in soup.find_all('div', class_='item clearfix'):
            try:
                name = cat.find('h2').find('a').text.strip()
                description = cat.find('p').text.strip()
                link = cat.find('a', class_='readmore')['href']
                date_div = cat.find('div', class_='date')
                if date_div:
                    date_text = date_div.text.strip()
                    if '|' in date_text:
                        gender, date = map(str.strip, date_text.split('|', 1))
                    else:
                        gender = "Nav norādīts"
                        date = date_text
                else:
                    gender = "Nav norādīts"
                    date = "Nav norādīts"

    
                parsed_date = self.parse_latvian_date(date)

                cats.append({
                    'name': name,
                    'description': description,
                    'link': link,
                    'gender': gender,
                    'date': parsed_date,  
                    'original_date': date  
                })
            except AttributeError as e:
                print(f"Error parsing cat entry: {e}")
        return cats

    def fetch_data(self):
        current_url = self.url
        while current_url:
            response = requests.get(current_url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                self.data.extend(self.parse_data(soup))

             
                next_page = soup.find('a', class_='next')
                if next_page:
                    current_url = next_page['href']
                    if not current_url.startswith('http'):
                        current_url = f"http://www.dzd.lv{current_url}"
                else:
                    current_url = None  
            else:
                print("Failed to retrieve data from the website.")
                break

    def get_data(self):
        return self.data