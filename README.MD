# Azeno Flashcards

## Algorytm postępowania

1. Czy potrzebujemy django app?
   1. `python manage.py startapp <name>`
   2. Dodaj do installl apps -> settings.py
2. Czy potrzebujemy do dane?
   1. Narysowanie na kartce ERD diagramu.
   2. Implementacja w models.py
      1. Każdy model powinien mieć __str__
      2. Zastanowienie się czy ma mieć sortowanie danych
      3. itp.
   3. `python manage.py makemigrations <app_name>`
   4. `python manage.py migrate <app_name>`
   5. Unit tests - pytest
3. Czy potrzebujemy zarządać zasobem z CMS (Django admin)?
   1. Jeżeli tak rejestrujemy modele w admin.py
4. Czy wystawiamy dane w widoku?
   1. Jeżeli tak tworzymy pilk serializers.py i tam tworzymy klasy serializatora (format danych)
   2. Unit test -> pytest
5. Tworzymy widoki (logikę)
    1. Dobieramy odpowiednią klasę do obsługi widoku [wyszukiwarka widoków](https://www.cdrf.co/)
    2. Widok musi zwracać response lub redirect
    3. Logika uprawnień permissions.py
    4. Unit tests -> pytest
6. Tworzymy lokalny router
   1. W pliku urls.py tworzymy urlpatterns lub router
   2. Podpinamy lokalne urls do globalnych url -> config/urls.py
   3. Unit test -> pytest
7. Postman i stworzenie kolekcji
   1. Wyeksportowanie kolekcji do repozytorium