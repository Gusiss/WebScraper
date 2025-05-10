# Kaķu patversmes web scraper

## Projekta mērķis
Šis projekts ir izstrādāts, lai izveidotu tīmekļa skrāpi, kas iegūst datus no kaķu patversmes tīmekļa vietnes. Lietotāji var apskatīt kaķu sarakstu un iegūt informāciju par tiem gan adopcijas centrā, gan hosteļa sadaļā.

## Izmantotās bibliotēkas
Projekts izmanto šādas Python bibliotēkas:
- `requests`: lai veiktu HTTP pieprasījumus un iegūtu HTML saturu.
- `BeautifulSoup`: lai analizētu un izvilktu datus no HTML.

## Datu struktūras
Projekts izmanto šādas datu struktūras:
- **Kaķu dati**: katrs kaķis tiek attēlots kā vārdnīca ar šādiem laukiem:
  - `name`: kaķa vārds.
  - `description`: īss apraksts par kaķi.
  - `link`: saite uz detalizētu informāciju par kaķi.

## Lietošanas instrukcija
1. Klonējiet šo repozitoriju uz savu datoru.
2. Instalējiet nepieciešamās bibliotēkas, izmantojot komandu:
   ```bash
   pip install -r requirements.txt
   ```
3. Palaidiet galveno skriptu:
   ```bash
   python main.py
   ```
4. Izvēlieties, kuru sadaļu vēlaties apskatīt:
   - Ievadiet `1`, lai apskatītu kaķus adopcijas centrā.
   - Ievadiet `2`, lai apskatītu kaķus hosteļa sadaļā.
5. Skripts iegūs un parādīs kaķu sarakstu no izvēlētās sadaļas.

## Testēšana
Lai pārbaudītu, vai skrāpis darbojas pareizi, veiciet šādas darbības:
1. Pārliecinieties, ka `main.py` fails satur šādu kodu:
   ```python
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
       
       # Inicializē skrāpi
       scraper = Scraper(url)
       
       # Iegūst datus
       scraper.fetch_data()
       
       # Parāda datus
       data = scraper.get_data()
       if data:
           print("Kaķi, kas atrasti visās lapās:\n")
           for index, cat in enumerate(data, start=1):
               print(f"Kaķis #{index}")
               print(f"Vārds: {cat['name']}")
               print(f"Apraksts: {cat['description']}")
               print(f"Saite: {cat['link']}")
               print("-" * 40)
       else:
           print("Netika atrasti kaķi.")

   if __name__ == "__main__":
       test_scraper()
   ```
2. Palaidiet skriptu:
   ```bash
   python main.py
   ```
3. Rezultātā terminālā tiks parādīts kaķu saraksts no izvēlētās sadaļas, piemēram:
   ```plaintext
   Kaķi, kas atrasti visās lapās:

   Kaķis #1
   Vārds: Masja
   Apraksts: Masja līdz šim bijis mājas kaķītis.
   Saite: http://www.dzd.lv/mekle-majas/dzivnieks/masja-2/
   ----------------------------------------

   Kaķis #2
   Vārds: Nensija
   Apraksts: Nensija mitinājās netālu no Dienvidu tilta, Bauskas ielā, kādā mazdārziņā.
   Saite: http://www.dzd.lv/mekle-majas/dzivnieks/nensija/
   ----------------------------------------
   ```

## Autori
Šo projektu izstrādāja [Gustavs Šics].