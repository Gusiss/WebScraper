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
  - `gender`: kaķa dzimums (mātīte/tēviņš).
  - `date`: uzņemšanas datums kā `datetime.date` objekts (kārtotam sarakstam).
  - `original_date`: uzņemšanas datums oriģinālajā formātā (lietotāja ērtībai).

## Lietošanas instrukcija
1. Klonējiet šo repozitoriju uz savu datoru:
   ```bash
   git clone <repo-url>
   ```
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
6. Izvēlieties, vai vēlaties filtrēt vai kārtot datus:
   - Ievadiet `1`, lai filtrētu pēc dzimuma:
     - Ievadiet `mātīte`, lai parādītu tikai mātītes.
     - Ievadiet `tēviņš`, lai parādītu tikai tēviņus.
   - Ievadiet `2`, lai kārtotu pēc uzņemšanas datuma:
     - Ievadiet `jā`, lai kārtotu dilstošā secībā (no jaunākā uz vecāko).
     - Ievadiet `nē`, lai kārtotu augošā secībā (no vecākā uz jaunāko).
   - Ievadiet `3`, lai parādītu visus datus bez filtrēšanas vai kārtošanas.

## Autori
Šo projektu izstrādāja [Gustavs Šics].