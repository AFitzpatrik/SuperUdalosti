# SUPER UDÁLOSTI.COM

### Služba sdružování událostí
- Franců Patrik

## Technologie
- Python
- Django
- Django REST Framework
- SQLite
- HTML + CSS
- JavaScript
- python-dotenv (pro .env soubor)

### .gitignore
* .idea/
* *.pyc
* db.sqlite3
* .env
* /media/
* /static/

### Struktura projektu
```plaintext
Finalni_projekt_sluzba_sdruzovani_udalosti/
│
├── SuperUdalosti/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
├── venv/
└── requirements.txt
```

### Struktura aplikce "viewer"


## Funkcionality aplikace

- [ ] **1.0 Registrace a přihlášení uživatele**
  - [ ] Email jako přihlašovací údaj
  - [ ] Ověření platnosti emailu
  - [ ] Heslo 8–30 znaků
  - [ ] Zobrazované jméno – nepovolené prázdné nebo jen mezery
  - [ ] Role: běžný uživatel / organizátor
  - [ ] Heslo bezpečně uložené (hash)

- [ ] **2.0 Přidávání událostí (jen organizátor)**
  - [ ] Název (povinný)
  - [ ] Datum od/do
  - [ ] Popis (min. 20 znaků)
  - [ ] Vlastník (uživatel, který ji vytvořil)
  - [ ] Obrázek (volitelně)

- [ ] **3.0 Seznam událostí**
  - [ ] Seřazeno podle nejbližšího data
  - [ ] Titulek, datum, prvních 50 znaků popisu

- [ ] **4.0 Vyhledávač událostí**
  - [ ] Textové pole pro hledání v názvu
  - [ ] Filtrování podle času:
    - [ ] Budoucí
    - [ ] Probíhající a budoucí
    - [ ] Všechny
  - [ ] Výsledky na nové stránce s možností opětovného hledání

- [ ] **5.0 Detail události**
  - [ ] Název, datum od/do, celý popis
  - [ ] Obrázek (pokud je)
  - [ ] Propojení z domovské stránky

- [ ] **6.0 Komentáře k události**
  - [ ] Pouze přihlášení uživatelé
  - [ ] Max. 500 znaků
  - [ ] Seřazené od nejnovějších

- [ ] **7.0 Přihlašování na událost**
  - [ ] Tlačítko pro přihlášení / odhlášení
  - [ ] Pouze pro přihlášené uživatele
  - [ ] Zobrazení všech registrovaných uživatelů

- [ ] **8.0 Moje události**
  - [ ] Seznam vlastních událostí a těch, na které je uživatel přihlášen
  - [ ] Filtrování podle role (organizátor / účastník)
  - [ ] Filtrování podle data (budoucí, probíhající, minulé)
  - [ ] Volitelně: filtrování podle rozsahu datumů

- [ ] **9.0 Úprava události**
  - [ ] Pouze vlastník nebo administrátor
  - [ ] Možnost úpravy z detailu události

- [ ] **10.0 API**
  - [ ] REST API se seznamem všech budoucích událostí
  - [ ] Možnost filtrování podle časového období

- [ ] **11.0 Externí frontend aplikace**
  - [ ] Využívá REST API pro zobrazení událostí
  - [ ] (volitelně) filtrování na straně frontend aplikace