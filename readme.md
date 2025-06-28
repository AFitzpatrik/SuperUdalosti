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
  - [ ] 1.1 Zobrazení přihlášeného uživatele
  - [ ] 1.2 Omezení zobrazení pouze pro přihlášené uživatele/role (LoginRequiredMixin)
  - [ ] 1.3 Login
  - [ ] 1.4 Logout
  - [ ] 1.5 Registrační formulář

## Požadavky pro uživatelský panel
  - [ ] 1.6 Email jako přihlašovací údaj
  - [ ] 1.7 Ověření platnosti emailu
  - [ ] 1.8 Heslo 8–30 znaků
  - [ ] 1.9 Zobrazované jméno – nepovolené prázdné nebo jen mezery
  - [ ] 1.10 Role: běžný uživatel / organizátor
  - [ ] 1.11 Heslo bezpečně uložené (hash)


- [ ] **2.0 Přidávání událostí**
  - [ ] 2.1 Přidávat může jen organizátor *DODĚLAT PO HOTOVÉ FEATURE 1.0
  - [x] 2.1 Název (povinný)
  - [x] 2.2 Datum od/do (povinný)
  - [x] 2.3 Popis (min. 20 znaků)
  - [x] 2.4 Vlastník (uživatel, který ji vytvořil)
  - [x] 2.5 Obrázek (volitelně)

- [x] **3.0 Seznam událostí**
  - [x] 3.1 Seřazeno podle nejbližšího data
  - [x] 3.2 Titulek, datum, prvních 50 znaků popisu

- [ ] **4.0 Vyhledávač událostí**
  - [ ] 4.1 Textové pole pro hledání v názvu
  - [ ] 4.2 Filtrování podle času:
    - [ ] 4.2.0 Budoucí
    - [ ] 4.2.1 Probíhající a budoucí
    - [ ] 4.2.2 Všechny
  - [ ] 4.3 Výsledky na nové stránce s možností opětovného hledání

- [x] **5.0 Detail události**
  - [x] 5.1 Název, datum od/do, celý popis
  - [x] 5.2 Obrázek (pokud je)
  - [x] 5.3 Propojení z domovské stránky

- [ ] **6.0 Komentáře k události**
  - [ ] 6.1 Pouze přihlášení uživatelé
  - [ ] 6.2 Max. 500 znaků
  - [ ] 6.3 Seřazené od nejnovějších

- [ ] **7.0 Přihlašování na událost**
  - [ ] 7.1 Tlačítko pro přihlášení / odhlášení
  - [ ] 7.2 Pouze pro přihlášené uživatele
  - [ ] 7.3 Zobrazení všech registrovaných uživatelů

- [ ] **8.0 Moje události**
  - [ ] 8.1 Seznam vlastních událostí a těch, na které je uživatel přihlášen
  - [ ] 8.2 Filtrování podle role (organizátor / účastník)
  - [ ] 8.3 Filtrování podle data (budoucí, probíhající, minulé)
  - [ ] 8.4 Volitelně: filtrování podle rozsahu datumů

- [ ] **9.0 Úprava události**
  - [ ] 9.1 Pouze vlastník nebo administrátor
  - [ ] 9.2 Možnost úpravy z detailu události

- [ ] **10.0 API**
  - [ ] 10.1 REST API se seznamem všech budoucích událostí
  - [ ] 10.2 Možnost filtrování podle časového období

- [ ] **11.0 Externí frontend aplikace**
  - [ ] 11.1 Využívá REST API pro zobrazení událostí
  - [ ] 11.2 (volitelně) filtrování na straně frontend aplikace


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
- https://www.color-hex.com/color-palette/1061837 paleta barev
