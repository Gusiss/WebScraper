from scraper import Scraper

def test_scraper():
    # URL for the first page of cats
    url = "http://www.dzd.lv/mekle-majas/dzivnieks/"
    
    # Initialize the scraper
    scraper = Scraper(url)
    
    # Fetch data
    scraper.fetch_data()
    
    # Get and print the data
    data = scraper.get_data()
    if data:
        print("Cats found on the first page:")
        for cat in data:
            print(cat)
    else:
        print("No cats found on the first page.")

if __name__ == "__main__":
    test_scraper()