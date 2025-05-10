class Scraper:
    def __init__(self, url):
        self.url = url
        self.data = [] 
    
    def parse_data(self, soup):
        cats = []
        # Find all cat entries in the HTML
        for cat in soup.find_all('div', class_='item clearfix'):
            print(cat)  # Print the raw HTML of each cat entry for debugging
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

        # Fetch the HTML content of the page
        response = requests.get(self.url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            print(soup.prettify())  # Print the raw HTML for debugging
            self.data = self.parse_data(soup)
        else:
            print("Failed to retrieve data from the website.")

    def get_data(self):
        return self.data