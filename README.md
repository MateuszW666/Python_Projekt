# Python_Projekt

## Opis:
Projekt polega na stworzeniu gry, Zgadnij liczbę, w której użytkownik musi zgadnąć liczbę, wylosowaną przez komputer:  
- dodatkowo gracz ma do wyboru tryby gry, w których wybiera, czy ma być to trudny tryb (im trudniejszy, tym większy przedział liczb, którą musi zgadnąć)  
- gracz ma parę żyć, za każdym razem, gdy nie trafi liczby, informowany jest o tym, że nie trafił i traci życie; ilość żyć jest predefiniowana oraz zależna od trybu gry  
- po wprowadzeniu liczby, gdy gracz nie trafił na prawidłową, wyświetla się podpowiedź, czy liczba jest większa lub mniejsza  
- jeśli gracz zgadnie liczbę za pierwszym razem, wyświetla się inny komunikat, niż gdy zgadnie za n'tą próbą  
- program przechowuje liczby, które wprowadził gracz i wyświetla po każdym jego "ruchu"  
- jeśli ilość żyć gracza będzie równa 0, automatycznie przegrywa i wyświetla się komunikat o końcu gry  
- jeśli użytkownik nie wprowadzi liczby, a coś innego, program poprosi o wprowadzenie prawidłowej liczby  
- program przechowuje najlepsze wyniki graczy w pliku CSV i umożliwia ich przeglądanie

## Instrukcja obsługi:
- Uruchom program.  
- Wybierz opcję:
  - 1: Zagraj w grę.
  - 2: Wyświetl leaderboard.
  - 3: Wyjdź z programu.
- W trybie gry:
  - Podaj swoje imię.
  - Wybierz tryb gry.
  - Podaj liczbę, którą chcesz zgadnąć, gdy program o to poprosi.
  - Program poinformuje Cię, czy liczba jest za wysoka, za niska, czy poprawna, oraz ile żyć Ci pozostało.
  - Kontynuuj zgadywanie, aż trafisz na właściwą liczbę lub stracisz wszystkie życia.
  - Sprawdź historię zgadywanych liczb i korzystaj ze wskaźnika "ciepła/zimna".
- Po zakończeniu gry wynik zostanie zapisany w pliku `game_results.csv`.
- W trybie leaderboard:
  - Zostaną wyświetlone najlepsze wyniki graczy zapisane w pliku `game_results.csv`.
