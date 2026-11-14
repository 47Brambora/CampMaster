# CampMaster - Roadmap & TODO

**Cíl aplikace:**  

Minimalistický táborový bodovací manažer pro jednotlivce s terminálovým vzhledem.  
Hlavním výstupem je přehledná tabulka výsledků pro tisk z Excelu (`.xlsx`).  

---

## Fáze 1: Databázové schéma (SQLite)

- [x] Automatické zakládání adresáře `data/` a detekce existujících databází
- [x] Dialogové okno pro vytvoření nové databáze tábora (`camp_YYYY.db`)
- [x] Implementace SQLite tabulek při zakládání databáze:
  - `participants` (jméno, příjmení, datum narození, tým, kategorie, pohlaví)
  - `games` (soutěže / disciplíny, typ hry a pravidlo bodování)
  - `scores` (výsledky jednotlivců v hrách, stav účasti, časy a body)

## Fáze 2: Uživatelské rozhraní (Tkinter)

- [x] Úvodní obrazovka (Splash screen) s animovaným ASCII loading barem
- [x] Hlavní menu s dynamickým výpisem dostupných táborů
- [x] Spodní navigační panel (klávesové zkratky / Enter navigace)
- [ ] Zobrazení dat do příslušných záložek
- [ ] Zapsání nových dat do databáze
- [ ] Úprava starých dat a zapsání do databáze
- [ ] Smazání dat z databáze
- [ ] Import účastníků ze souboru (CSV / `.xlsx`)

## Fáze 3: Bodování a výpočty

- [ ] Body za pořadí podle pravidla hry (`fixed_max_XX`, `descending_by_participants`, ...)
- [ ] Časové disciplíny: intervalové starty a výpočet čistého času
- [ ] Stavy účasti (`OK`, `DNS`, `DNF`, `DQ`) a jejich vliv na pořadí
- [ ] Ruční přepsání bodů a ručně posunutý start (volba, zda posun ovlivní další starty)
- [ ] Celkové pořadí jednotlivců podle kategorií A až E

## Fáze 4: Export do Excelu (`openpyxl`)

- [ ] Návrh struktury exportu (celkové pořadí jednotlivců + přehled her)
- [ ] Implementace generování `.xlsx` souboru pro snadný tisk

## Fáze 5: Kvalita a distribuce

- [ ] Testy (`pytest`) pro databázi, bodování a časy + běh v CI
- [ ] Sestavení samostatného `.exe` přes PyInstaller a vyzkoušení na Windows
- [ ] Ochrana osobních údajů dětí (rozhodnout o zdravotních záznamech a smlouvách z README)
