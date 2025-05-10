from scraper import Scraper

def test_scraper():
    print("Izvēlieties, kuru sadaļu vēlaties apskatīt:")
    print("1. Kaķi adopcijas centrā")
    print("2. Kaķi hosteļa sadaļā")
    
    choice = input("Ievadiet savu izvēli (1 vai 2): ").strip()
    
    if choice == "1":
        url = "http://www.dzd.lv/mekle-majas/dzivnieks/"
    elif choice == "2":
        url = "http://www.dzd.lv/mekle-majas/hostelis/"
    else:
        print("Nederīga izvēle. Lūdzu, mēģiniet vēlreiz.")
        return
    
    # Initialize the scraper
    scraper = Scraper(url)
    
    # Fetch data
    scraper.fetch_data()
    
    # Get and print the data
    data = scraper.get_data()
    if data:
        print("Kaķi, kas atrasti visās lapās:\n")
        for index, cat in enumerate(data, start=1):
            print(f"Kaķis #{index}")
            print(f"Vārds: {cat['name']}")
            print(f"Apraksts: {cat['description']}")
            print(f"Saite: {cat['link']}")
            print("-" * 40)  # Separator for better readability
    else:
        print("Netika atrasti kaķi.")

if __name__ == "__main__":
    test_scraper()