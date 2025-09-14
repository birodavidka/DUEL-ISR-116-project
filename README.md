## LOGIN FELÜLET A TOVÁBBI KONZULTÁCIÓK PROJEKTJÉHEZ 

## Hallgató
Biró Dávid
TUXOLP

## Feladat rövid leírása
Egy egyszerű grafikus Python alkalmazás CustomTkinter segítségével.  
Az ablakban megadható email és jelszó, valamint egy slider értéke.  
Az adatok egy `userCred` objektumba kerülnek és kiírásra a terminálban.  
A program tartalmaz saját modult, függvényt és osztályt, a monogrammal ellátva (BD).

A továbbiakban szeretném a Firebase cloud megoldásaival összekötni, valamint kidolgozni valódi atutentikációt, valamint adatbázis CRUD megoldásokat.

## Modulok és függvények

### Saját modul: `BD_module.py`
- `bd_format_email(email)` → az email kisbetűsítése és tisztítása  
- `bd_validate_email(email)` → email cím ellenőrzése regex segítségével  
- `bd_mask_password(pw)` → jelszó maszkolása csillagokkal  
- `BDUser` osztály → email és jelszó tárolása, dict-re alakítás

### Főprogram: `main.py`
- `BD_login_handler()` → a bevitt adatok feldolgozása, `BDUser` példány létrehozása, `userCred` frissítése  
- `slider_event(value)` → frissíti a slider aktuális értékét a labelben  
- GUI elemek: logó, email és jelszó mezők, login gomb ikonokkal, slider

## Példa kimenet (terminálban)
```
User credentials: {'email': 'teszt@example.com', 'password': 'titok', 'slider': 42}
User object: BDUser(email=teszt@example.com, password=*****)
```
