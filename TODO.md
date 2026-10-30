# CampMaster - Roadmap & TODO

**Cíl aplikace:**  

Minimalistický táborový bodovací manažer pro jednotlivce s terminálovým vzhledem.  
Hlavním výstupem je přehledná tabulka výsledků pro tisk z Excelu (`.xlsx`).  

---

## Fáze 1: Databázové schéma (SQLite)

- [x] Automatické zakládání adresáře `data/` a detekce existujících databází
- [x] Dialogové okno pro vytvoření nové databáze tábora (`camp_YYYY.db`)
- [ ] Implementace SQLite tabulek při zakládání databáze:
  - `participants` (jméno a příjmení účastníků)
  - `games` (soutěže / disciplíny)
  - `scores` (bodování jednotlivců v hrách)

## Fáze 2: Uživatelské rozhraní (Tkinter)

- [x] Úvodní obrazovka (Splash screen) s animovaným ASCII loading barem
- [x] Hlavní menu s dynamickým výpisem dostupných táborů
- [x] Spodní navigační panel (klávesové zkratky / Enter navigace)
- [ ] Obrazovka pro správu účastníků (přidání / výpis dětí)
- [ ] Obrazovka pro správu her a zadávání bodů / výsledků

## Fáze 3: Export do Excelu (`openpyxl`)

- [ ] Návrh struktury exportu (celkové pořadí jednotlivců + přehled her)
- [ ] Implementace generování `.xlsx` souboru pro snadný tisk
