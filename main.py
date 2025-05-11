from scraper import Scraper
from filters import filter_by_gender, sort_by_date

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
      
    scraper = Scraper(url)
    scraper.fetch_data()
    data = scraper.get_data()

    if data:
        print("Vai vēlaties filtrēt vai kārtot datus?")
        print("1. Filtrēt pēc dzimuma")
        print("2. Kārtot pēc uzņemšanas datuma")
        print("3. Parādīt visus datus")
        
        filter_choice = input("Ievadiet savu izvēli (1-3): ").strip()
        
        if filter_choice == "1":
            gender = input("Ievadiet dzimumu (mātīte/tēviņš): ").strip()
            data = filter_by_gender(data, gender)
        elif filter_choice == "2":
            reverse = input("Kārtot dilstošā secībā? (jā/nē): ").strip().lower() == "jā"
            data = sort_by_date(data, reverse=reverse)
        
        print("Kaķi, kas atrasti visās lapās:\n")
        for index, cat in enumerate(data, start=1):
            print(f"Kaķis #{index}")
            print(f"Vārds: {cat['name']}")
            print(f"Dzimums: {cat['gender']}")
            print(f"Uzņemšanas datums: {cat['original_date']}")
            print(f"Apraksts: {cat['description']}")
            print(f"Saite: {cat['link']}")
            print("-" * 40)
    else:
        print("Netika atrasti kaķi.")

if __name__ == "__main__":
    test_scraper()