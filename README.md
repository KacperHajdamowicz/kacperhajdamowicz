# Strona osobista

Czysty HTML i CSS. Bez buildu, bez zależności.

## Podgląd

Podwójne kliknięcie w `index.html` działa. Wersja bliższa produkcji:

    python -m http.server 8080

i `http://localhost:8080/`.

## Nowy wpis na blogu

1. Skopiuj `blog/_template.html` do `blog/RRRR-MM-slug.html` (bez polskich znaków w nazwie, bez podkreślnika na początku).
2. Uzupełnij komentarze 1-3 w pliku: tytuł, opis, datę, treść.
3. Dopisz wiersz na górze listy w `blog/index.html` i w `index.html` (sekcja „Ostatnie wpisy", maksymalnie 4 pozycje; starsze usuwaj tylko z `index.html`).
4. `python check_links.py` musi wypisać `OK`.

## CV

Treść: `cv/index.html`. PDF: podmień `cv/Kacper_Hajdamowicz_CV.pdf`, nazwa bez zmian. Ctrl+P na stronie CV daje wersję do druku bez paska bocznego.

## Zdjęcie

`photo.jpg` w katalogu głównym, kwadrat, minimum 500x500 px. Nazwa bez zmian. Teraz leży tam szary kafel zastępczy.

## Kolory i kroje

Wszystko na górze `style.css`, w `:root`. Nic innego nie trzeba ruszać.

## Publikacja

GitHub Pages: Settings, Pages, „Deploy from a branch", gałąź `main`, katalog `/ (root)`. Każdy `git push` na `main` publikuje stronę po około minucie. Plik `.nojekyll` musi zostać.

Własna domena: dodaj plik `CNAME` z samą nazwą domeny i wskaż DNS zgodnie z dokumentacją GitHub Pages. Linki na stronie są względne, więc nic więcej nie zmieniasz.
