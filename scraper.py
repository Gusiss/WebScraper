class Scraper:
    def __init__(self, url):
        self.url = url
        self.data = [] 
    
    def parse_data(self, soup):
        cats = []
        # Find all cat entries in the HTML
        for cat in soup.find_all('div', class_='item clearfix'):
            try:
                # Extract the name
                name = cat.find('h2').find('a').text.strip()
                # Extract the description
                description = cat.find('p').text.strip()
                # Extract the link to the detailed page
                link = cat.find('a', class_='readmore')['href']
                
                # Append the cat data to the list
                cats.append({
                    'name': name,
                    'description': description,
                    'link': link
                })
            except AttributeError as e:
                print(f"Error parsing cat entry: {e}")
        return cats

    def fetch_data(self):
        import requests
        from bs4 import BeautifulSoup

        current_url = self.url  # Start with the initial URL
        while current_url:
            response = requests.get(current_url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                self.data.extend(self.parse_data(soup))  # Append data from the current page
                
                # Find the "Next" page link
                next_page = soup.find('a', class_='next')  # Replace 'next' with the actual class or ID for the "Next" button
                if next_page:
                    current_url = next_page['href']  # Update the URL to the next page
                    if not current_url.startswith('http'):
                        # Handle relative URLs
                        current_url = f"http://www.dzd.lv{current_url}"
                else:
                    current_url = None  # Stop if no "Next" page is found
            else:
                print("Failed to retrieve data from the website.")
                break

    def get_data(self):
        return self.data