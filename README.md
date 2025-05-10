# Kaķu patversmes web scraper

## Projekta mērķis
Šis projekts ir izstrādāts, lai izveidotu tīmekļa skrāpi, kas iegūst datus no kaķu patversmes tīmekļa vietnes. Lietotāji var filtrēt datus, pamatojoties uz dažādiem kritērijiem, piemēram, vecumu, šķirni un izmēru.

## Izmantotās bibliotēkas
Projekts izmanto šādas Python bibliotēkas:
- `requests`: lai veiktu HTTP pieprasījumus un iegūtu HTML saturu.
- `BeautifulSoup`: lai analizētu un izvilktu datus no HTML.

## Datu struktūras
Projekts izmanto šādas datu struktūras:
- **Kaķu dati**: katrs kaķis tiek attēlots kā vārds, vecums, šķirne un izmērs.

## Lietošanas instrukcija
1. Klonējiet šo repozitoriju uz savu datoru.
2. Instalējiet nepieciešamās bibliotēkas, izmantojot komandu:
   ```
   pip install -r requirements.txt
   ```
3. Palaidiet galveno skriptu:
   ```
   python src/main.py
   ```
4. Ievadiet filtrēšanas kritērijus, kad tiksat aicināti, un skatiet rezultātus.

## Testēšana
Lai pārbaudītu, vai skrāpis darbojas pareizi, veiciet šādas darbības:
1. Pārliecinieties, ka `main.py` fails satur šādu kodu:
   ```python
   from scraper import Scraper

   def test_scraper():
       # URL pirmās lapas kaķiem
       url = "http://www.dzd.lv/mekle-majas/dzivnieks/"
       
       # Inicializē skrāpi
       scraper = Scraper(url)
       
       # Iegūst datus
       scraper.fetch_data()
       
       # Parāda datus
       data = scraper.get_data()
       if data:
           print("Kaķi, kas atrasti pirmajā lapā:")
           for cat in data:
               print(cat)
       else:
           print("Pirmajā lapā netika atrasti kaķi.")

   if __name__ == "__main__":
       test_scraper()
   ```
2. Palaidiet skriptu:
   ```bash
   python main.py
   ```
3. Rezultātā terminālā tiks parādīts kaķu saraksts no pirmās lapas, piemēram:
   ```plaintext
   Kaķi, kas atrasti pirmajā lapā:
   {'name': 'Masja', 'description': 'Masja līdz šim bijis mājas kaķītis.', 'link': 'http://www.dzd.lv/mekle-majas/dzivnieks/masja-2/'}
   {'name': 'Nensija', 'description': 'Nensija mitinājās netālu no Dienvidu tilta...', 'link': 'http://www.dzd.lv/mekle-majas/dzivnieks/nensija/'}
   ...
   ```
   

## Autori
Šo projektu izstrādāja [Gustavs Šics].