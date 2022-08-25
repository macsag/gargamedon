# gargamedon

## o co chodzi?
Gargamedon to aplikacja webowa do zarządzania domowym katalogiem książek. Jeśli masz problem z odnalezieniem swojej 
książki na domowych półkach/stosach, nie wiesz, czy nie kupujesz trzeci raz tej samej, nie wiesz, komu ją pożyczyłeś/aś, 
może warto zrobić w końcu porządek z tym gargamedonem (czyli armagedonem).

W większości przypadków, dzięki integracji z bazą danych Biblioteki Narodowej, skatalogowanie książki wymaga jedynie
wpisania lub skopiowania jej ISBN.

## funkcje
- [ ] zarządzanie domową biblioteką (tworzenie nowej biblioteki, tworzenie nowej "filii" biblioteki 
(np. mieszkanie mamy, akademik), tworzenie nowej lokalizacji (np. strych w mieszkaniu mamy, salon, biblioteczka))
- [ ] zarządzanie użytkownikami biblioteki (administrator, czytelnik)
- [ ] katalogowanie książek (dodawanie nowych pozycji zgodnie z modelem FRBR)
- [ ] udostępnianie książek (rezerwacja, wypożyczanie)
- [ ] wyszukiwanie książek (wyszukiwanie po tytule, autorze, temacie)
- [ ] opcjonalne udostępnianie książek innych użytkownikom katalogu (poszukujesz jakiejś
rzadkiej książki i nie ma jej ani w lokalnych bibliotekach, ani w ksiągarniach? może ma ją ktoś w Twojej okolicy
i zgodzi się ją wypożyczyć?)

## po co?
Przede wszystkim, żeby nauczyć się programować. W drugiej kolejności, żeby uporządkować swój księgozbiór. A jeśli 
dodatkowo przyda się to może jeszcze komuś innemu...

## architektura
Backend aplikacji napisany jest w Pythonie przy wykorzystaniu frameworka FastAPI. Baza danych to MongoDB.
Silnik wyszukiwania pełnotekstowego to Elasticsearch. 

Tymczasowy frontend również napisany w Pythonie przy użyciu silnika szablonów Jinja2 i frameworka CSS Bootstrap.
Docelowo planowane napisanie frontendu w frameworku Vue.js.