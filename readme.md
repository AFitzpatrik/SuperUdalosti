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

- [x] **3.0 Seznam událostí**
  - [x] 3.1 Seřazeno podle nejbližšího data
  - [x] 3.2 Titulek, datum, prvních 50 znaků popisu

- [ ] **4.0 Vyhledávač událostí**
  - [ ] Textové pole pro hledání v názvu
  - [ ] Filtrování podle času:
    - [ ] Budoucí
    - [ ] Probíhající a budoucí
    - [ ] Všechny
  - [ ] Výsledky na nové stránce s možností opětovného hledání

- [x] **5.0 Detail události**
  - [x] 5.1 Název, datum od/do, celý popis
  - [x] 5.2 Obrázek (pokud je)
  - [x] 5.3 Propojení z domovské stránky

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


### Struktura databáze

#### Databáze


- [x] 1.0 Country
  - [x] 1.1 name

- [x] 2.0 City
  - [x] 2.1 name
  - [x] 2.2 country (FK -> Country)
  - [x] 2.3 zip_code

- [x] 3.0 Location
  - [x] 3.1 name
  - [x] 3.2 address (street, number)
  - [x] 3.3 city (FK -> City)
  - [x] 3.4 latitude
  - [x] 3.5 longitude

- [x] 4.0 Event
  - [x] 4.1 name
  - [x] 4.2 description
  - [x] 4.3 start_date
  - [x] 4.4 end_date
  - [x] 4.5 event_image
  - [x] 4.6 owner_of_event (FK -> User)
  - [x] 4.7 location (FK - > Location)
 
- [x] 5.0 Comment
  - [x 5.1 user (FK -> User)
  - [x] 5.2 event (FK -> Event)
  - [x 5.3 content
  - [x] 5.4 date_posted

```plaintext
Event ---* Comment --- User
  |
  |
 Location

Event má 1 Lokaci (Location) 
Event může mít více Komentářů (Comment)
Jeden komentář (Comment) patří 1 Uživateli (User)
Jeden Event patří 1 Uživateli (User) *Musí to být organizátor



```
# DODĚLAT!!!



- V budoucnu:
- LIGHT/DARK REŽIM
