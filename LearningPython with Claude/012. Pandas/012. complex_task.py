"""
Projekt: Analiza sprzedaży e-commerce z przygotowaniem danych do hurtowni

Scenariusz: Pracujesz jako Data Engineer dla firmy e-commerce. Otrzymałeś 3 pliki źródłowe:
1. transakcje.csv - dane transakcyjne z ostatnich 6 miesięcy
2. produkty.csv - katalog produktów
3. klienci.csv - informacje o klientach

Twoim zadaniem jest przetworzenie tych danych, przygotowanie ich do załadowania do hurtowni danych
oraz przeprowadzenie analiz, które będą podstawą do raportów dla działu sprzedaży.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import os

# Tworzymy katalog na dane i wyniki
os.makedirs('data', exist_ok=True)
os.makedirs('output', exist_ok=True)

# ---------- 1. GENEROWANIE PRZYKŁADOWYCH DANYCH ----------

# Funkcja do generowania przykładowych danych
def generate_sample_data():
    # Generowanie danych klientów
    np.random.seed(42)
    n_customers = 1000
    
    klienci = pd.DataFrame({
        'id_klienta': ['K' + str(i).zfill(6) for i in range(1, n_customers + 1)],
        'imie': np.random.choice(['Jan', 'Anna', 'Piotr', 'Maria', 'Tomasz', 'Katarzyna', 'Michał', 'Magdalena'], size=n_customers),
        'nazwisko': np.random.choice(['Kowalski', 'Nowak', 'Wiśniewski', 'Dąbrowski', 'Lewandowski', 'Wójcik', 'Kamiński'], size=n_customers),
        'email': ['user' + str(i) + '@example.com' for i in range(1, n_customers + 1)],
        'data_rejestracji': pd.date_range(start='2022-01-01', end='2023-06-30', periods=n_customers),
        'miasto': np.random.choice(['Warszawa', 'Kraków', 'Gdańsk', 'Poznań', 'Wrocław', 'Łódź', 'Szczecin'], size=n_customers),
        'kraj': 'Polska',
        'segment': np.random.choice(['Standard', 'Premium', 'VIP'], size=n_customers, p=[0.7, 0.2, 0.1])
    })
    
    # Generowanie danych produktów
    n_products = 200
    kategorie = ['Elektronika', 'Odzież', 'Dom i Ogród', 'Sport', 'Książki', 'Zabawki', 'Zdrowie']
    podkategorie = {
        'Elektronika': ['Smartfony', 'Laptopy', 'Telewizory', 'Audio', 'Akcesoria'],
        'Odzież': ['Męska', 'Damska', 'Dziecięca', 'Sportowa', 'Dodatki'],
        'Dom i Ogród': ['Meble', 'Narzędzia', 'Ogród', 'Dekoracje', 'AGD'],
        'Sport': ['Fitness', 'Rowery', 'Turystyka', 'Sporty zimowe', 'Sporty wodne'],
        'Książki': ['Kryminały', 'Fantastyka', 'Literatura faktu', 'Poradniki', 'Dziecięce'],
        'Zabawki': ['Klocki', 'Gry planszowe', 'Lalki', 'Zabawki edukacyjne', 'Modele'],
        'Zdrowie': ['Suplementy', 'Kosmetyki', 'Higiena', 'Medycyna naturalna', 'Sprzęt medyczny']
    }
    
    kategoria_lista = []
    podkategoria_lista = []
    
    for _ in range(n_products):
        kat = np.random.choice(kategorie)
        kategoria_lista.append(kat)
        podkategoria_lista.append(np.random.choice(podkategorie[kat]))
    
    produkty = pd.DataFrame({
        'id_produktu': ['P' + str(i).zfill(6) for i in range(1, n_products + 1)],
        'nazwa_produktu': ['Produkt ' + str(i) for i in range(1, n_products + 1)],
        'kategoria': kategoria_lista,
        'podkategoria': podkategoria_lista,
        'cena_bazowa': np.random.uniform(10, 2000, size=n_products).round(2),
        'koszt_zakupu': np.random.uniform(5, 1500, size=n_products).round(2),
        'waga_kg': np.random.uniform(0.1, 30, size=n_products).round(1),
        'dostepny': np.random.choice([True, False], size=n_products, p=[0.9, 0.1]),
        'data_dodania': pd.date_range(start='2022-01-01', end='2023-06-30', periods=n_products)
    })
    
    # Upewnij się, że koszt jest zawsze mniejszy od ceny
    produkty.loc[produkty['koszt_zakupu'] >= produkty['cena_bazowa'], 'koszt_zakupu'] = produkty['cena_bazowa'] * 0.7
    
    # Generowanie danych transakcji
    n_transactions = 50000
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 6, 30)
    
    date_list = [start_date + timedelta(days=np.random.randint(0, (end_date - start_date).days)) for _ in range(n_transactions)]
    date_list.sort()  # Sortujemy daty chronologicznie
    
    customer_ids = np.random.choice(klienci['id_klienta'], size=n_transactions)
    metody_platnosci = ['Karta kredytowa', 'PayPal', 'Przelew bankowy', 'BLIK', 'Płatność przy odbiorze']
    statusy = ['Zrealizowane', 'Anulowane', 'Zwrócone', 'W trakcie realizacji']
    
    transakcje = pd.DataFrame({
        'id_transakcji': ['T' + str(i).zfill(8) for i in range(1, n_transactions + 1)],
        'id_klienta': customer_ids,
        'data_transakcji': date_list,
        'metoda_platnosci': np.random.choice(metody_platnosci, size=n_transactions, p=[0.4, 0.3, 0.1, 0.15, 0.05]),
        'status': np.random.choice(statusy, size=n_transactions, p=[0.85, 0.05, 0.05, 0.05])
    })
    
    # Generowanie szczegółów transakcji (linie zamówień)
    # Każda transakcja będzie miała od 1 do 5 produktów
    wszystkie_linie = []
    
    for i, transaction in transakcje.iterrows():
        n_lines = np.random.randint(1, 6)
        
        # Wybierz losowe produkty dla tej transakcji
        products_sample = np.random.choice(produkty['id_produktu'], size=n_lines, replace=False)
        
        for j, product_id in enumerate(products_sample):
            product = produkty[produkty['id_produktu'] == product_id].iloc[0]
            
            # Dodaj losowe zniżki dla niektórych produktów
            discount_pct = np.random.choice([0, 0.05, 0.1, 0.15, 0.2], p=[0.7, 0.1, 0.1, 0.05, 0.05])
            qty = np.random.randint(1, 4)
            
            # Oblicz cenę po rabacie
            price_after_discount = product['cena_bazowa'] * (1 - discount_pct)
            
            line_item = {
                'id_transakcji': transaction['id_transakcji'],
                'id_produktu': product_id,
                'ilosc': qty,
                'cena_jednostkowa': product['cena_bazowa'],
                'rabat_procent': discount_pct * 100,
                'cena_po_rabacie': price_after_discount,
                'wartosc_sprzedazy': price_after_discount * qty
            }
            wszystkie_linie.append(line_item)
    
    linie_transakcji = pd.DataFrame(wszystkie_linie)
    
    # Zapisz dane do plików CSV
    klienci.to_csv('data/klienci.csv', index=False)
    produkty.to_csv('data/produkty.csv', index=False)
    transakcje.to_csv('data/transakcje.csv', index=False)
    linie_transakcji.to_csv('data/linie_transakcji.csv', index=False)
    
    print("Wygenerowano przykładowe dane i zapisano do plików CSV")
    return klienci, produkty, transakcje, linie_transakcji

# Generujemy dane
klienci, produkty, transakcje, linie_transakcji = generate_sample_data()

# ---------- 2. PRZETWARZANIE I CZYSZCZENIE DANYCH ----------

def process_and_clean_data():
    # Wczytaj dane z plików CSV (symulacja rzeczywistego scenariusza)
    klienci = pd.read_csv('data/klienci.csv', parse_dates=['data_rejestracji'])
    produkty = pd.read_csv('data/produkty.csv', parse_dates=['data_dodania'])
    transakcje = pd.read_csv('data/transakcje.csv', parse_dates=['data_transakcji'])
    linie_transakcji = pd.read_csv('data/linie_transakcji.csv')
    
    print(f"Wczytane dane - statystyki:")
    print(f"Klienci: {klienci.shape[0]} rekordów")
    print(f"Produkty: {produkty.shape[0]} rekordów")
    print(f"Transakcje: {transakcje.shape[0]} rekordów")
    print(f"Linie transakcji: {linie_transakcji.shape[0]} rekordów")
    
    # Sprawdzanie brakujących wartości
    print("\nBrakujące wartości:")
    for df_name, df in [("Klienci", klienci), ("Produkty", produkty), 
                        ("Transakcje", transakcje), ("Linie transakcji", linie_transakcji)]:
        missing_values = df.isna().sum().sum()
        print(f"{df_name}: {missing_values} brakujących wartości")
    
    # Czyszczenie danych - wypełnianie lub usuwanie braków
    # W tym przypadku dane są wygenerowane, więc nie ma braków, ale dodajmy przykładową logikę
    
    # Usuwanie duplikatów
    klienci_unique = klienci.drop_duplicates(subset=['id_klienta'])
    produkty_unique = produkty.drop_duplicates(subset=['id_produktu'])
    transakcje_unique = transakcje.drop_duplicates(subset=['id_transakcji'])
    
    # Sprawdzenie różnic po usunięciu duplikatów
    print("\nUsunięte duplikaty:")
    print(f"Klienci: {klienci.shape[0] - klienci_unique.shape[0]}")
    print(f"Produkty: {produkty.shape[0] - produkty_unique.shape[0]}")
    print(f"Transakcje: {transakcje.shape[0] - transakcje_unique.shape[0]}")
    
    # Obliczanie dodatkowych kolumn
    produkty['marza'] = produkty['cena_bazowa'] - produkty['koszt_zakupu']
    produkty['marza_procent'] = (produkty['marza'] / produkty['cena_bazowa'] * 100).round(2)
    
    # Sprawdzanie poprawności danych
    # Sprawdzenie, czy wszystkie transakcje mają linie
    transakcje_bez_linii = set(transakcje['id_transakcji']) - set(linie_transakcji['id_transakcji'])
    print(f"\nTransakcje bez linii: {len(transakcje_bez_linii)}")
    
    # Oznaczenie wieku klienta (dni od rejestracji do końca okresu)
    ostatnia_data = transakcje['data_transakcji'].max()
    klienci['dni_od_rejestracji'] = (ostatnia_data - klienci['data_rejestracji']).dt.days
    
    # Konwersja typów danych dla optymalizacji pamięci
    transakcje['metoda_platnosci'] = transakcje['metoda_platnosci'].astype('category')
    transakcje['status'] = transakcje['status'].astype('category')
    produkty['kategoria'] = produkty['kategoria'].astype('category')
    produkty['podkategoria'] = produkty['podkategoria'].astype('category')
    klienci['miasto'] = klienci['miasto'].astype('category')
    klienci['segment'] = klienci['segment'].astype('category')
    
    # Zapisz przetworzone dane
    klienci.to_csv('output/klienci_processed.csv', index=False)
    produkty.to_csv('output/produkty_processed.csv', index=False)
    transakcje.to_csv('output/transakcje_processed.csv', index=False)
    linie_transakcji.to_csv('output/linie_transakcji_processed.csv', index=False)
    
    return klienci, produkty, transakcje, linie_transakcji

# Przetwarzamy dane
klienci, produkty, transakcje, linie_transakcji = process_and_clean_data()

# ---------- 3. TWORZENIE TABEL ANALITYCZNYCH ----------

def create_analytical_tables():
    # Agregacja sprzedaży produktów
    sprzedaz_produktow = linie_transakcji.groupby('id_produktu').agg(
        liczba_sprzedazy=('id_transakcji', 'count'),
        laczna_ilosc=('ilosc', 'sum'),
        przychod_calkowity=('wartosc_sprzedazy', 'sum'),
        srednia_cena=('cena_po_rabacie', 'mean'),
        sredni_rabat=('rabat_procent', 'mean')
    ).reset_index()
    
    # Dołączenie informacji o produktach
    sprzedaz_produktow = sprzedaz_produktow.merge(
        produkty[['id_produktu', 'nazwa_produktu', 'kategoria', 'podkategoria', 'cena_bazowa', 'koszt_zakupu']],
        on='id_produktu',
        how='left'
    )
    
    # Obliczanie marży
    sprzedaz_produktow['koszt_calkowity'] = sprzedaz_produktow['laczna_ilosc'] * sprzedaz_produktow['koszt_zakupu']
    sprzedaz_produktow['marza_calkowita'] = sprzedaz_produktow['przychod_calkowity'] - sprzedaz_produktow['koszt_calkowity']
    sprzedaz_produktow['marza_procent'] = (sprzedaz_produktow['marza_calkowita'] / sprzedaz_produktow['przychod_calkowity'] * 100).round(2)
    
    # Agregacja transakcji klientów
    transakcje_klientow = transakcje.groupby('id_klienta').agg(
        liczba_transakcji=('id_transakcji', 'count'),
        pierwsza_transakcja=('data_transakcji', 'min'),
        ostatnia_transakcja=('data_transakcji', 'max')
    ).reset_index()
    
    # Dołączenie wartości transakcji
    wartosc_transakcji = linie_transakcji.groupby('id_transakcji').agg(
        wartosc_zamowienia=('wartosc_sprzedazy', 'sum')
    ).reset_index()
    
    transakcje_z_wartoscia = transakcje.merge(wartosc_transakcji, on='id_transakcji', how='left')
    
    # Agregacja wartości transakcji klientów
    wartosc_klientow = transakcje_z_wartoscia.groupby('id_klienta').agg(
        laczna_wartosc=('wartosc_zamowienia', 'sum'),
        srednia_wartosc_zamowienia=('wartosc_zamowienia', 'mean'),
        min_wartosc_zamowienia=('wartosc_zamowienia', 'min'),
        max_wartosc_zamowienia=('wartosc_zamowienia', 'max')
    ).reset_index()
    
    # Łączenie danych o klientach
    analiza_klientow = transakcje_klientow.merge(wartosc_klientow, on='id_klienta', how='left')
    analiza_klientow = analiza_klientow.merge(
        klienci[['id_klienta', 'miasto', 'segment', 'data_rejestracji']],
        on='id_klienta',
        how='left'
    )
    
    # Obliczanie dodatkowych wskaźników
    analiza_klientow['dni_miedzy_transakcjami'] = (
        analiza_klientow['ostatnia_transakcja'] - analiza_klientow['pierwsza_transakcja']
    ).dt.days / np.maximum(analiza_klientow['liczba_transakcji'] - 1, 1)
    
    analiza_klientow['dni_od_rejestracji_do_pierwszego_zakupu'] = (
        analiza_klientow['pierwsza_transakcja'] - analiza_klientow['data_rejestracji']
    ).dt.days
    
    analiza_klientow['dni_od_ostatniego_zakupu'] = (
        transakcje['data_transakcji'].max() - analiza_klientow['ostatnia_transakcja']
    ).dt.days
    
    # Agregacja sprzedaży miesięcznej
    transakcje_z_wartoscia['rok_miesiac'] = transakcje_z_wartoscia['data_transakcji'].dt.to_period('M')
    sprzedaz_miesieczna = transakcje_z_wartoscia.groupby('rok_miesiac').agg(
        liczba_transakcji=('id_transakcji', 'count'),
        liczba_klientow=('id_klienta', 'nunique'),
        laczna_wartosc=('wartosc_zamowienia', 'sum')
    ).reset_index()
    
    # Agregacja sprzedaży kategorii
    linie_z_kategoriami = linie_transakcji.merge(
        produkty[['id_produktu', 'kategoria', 'podkategoria', 'koszt_zakupu']],
        on='id_produktu',
        how='left'
    )
    
    sprzedaz_kategorii = linie_z_kategoriami.groupby(['kategoria', 'podkategoria']).agg(
        liczba_sprzedazy=('id_transakcji', 'count'),
        laczna_ilosc=('ilosc', 'sum'),
        przychod_calkowity=('wartosc_sprzedazy', 'sum')
    ).reset_index()
    
    # Dołączenie informacji o kosztach
    sprzedaz_kategorii['koszt_calkowity'] = linie_z_kategoriami.groupby(['kategoria', 'podkategoria']).apply(
        lambda x: (x['ilosc'] * x['koszt_zakupu']).sum()
    ).reset_index(drop=True)
    
    sprzedaz_kategorii['marza_calkowita'] = sprzedaz_kategorii['przychod_calkowity'] - sprzedaz_kategorii['koszt_calkowity']
    sprzedaz_kategorii['marza_procent'] = (sprzedaz_kategorii['marza_calkowita'] / sprzedaz_kategorii['przychod_calkowity'] * 100).round(2)
    
    # Zapisanie tabel analitycznych
    sprzedaz_produktow.to_csv('output/sprzedaz_produktow.csv', index=False)
    analiza_klientow.to_csv('output/analiza_klientow.csv', index=False)
    sprzedaz_miesieczna.to_csv('output/sprzedaz_miesieczna.csv', index=False)
    sprzedaz_kategorii.to_csv('output/sprzedaz_kategorii.csv', index=False)
    
    return sprzedaz_produktow, analiza_klientow, sprzedaz_miesieczna, sprzedaz_kategorii

# Tworzymy tabele analityczne
sprzedaz_produktow, analiza_klientow, sprzedaz_miesieczna, sprzedaz_kategorii = create_analytical_tables()

# ---------- 4. ANALIZY I RAPORTY ----------

def perform_analyses():
    # Analiza 1: Top 10 najlepiej sprzedających się produktów
    top_produkty = sprzedaz_produktow.sort_values('przychod_calkowity', ascending=False).head(10)
    print("\nTop 10 najlepiej sprzedających się produktów:")
    print(top_produkty[['nazwa_produktu', 'kategoria', 'laczna_ilosc', 'przychod_calkowity']])
    
    # Analiza 2: Najbardziej dochodowe kategorie
    top_kategorie = sprzedaz_kategorii.sort_values('marza_calkowita', ascending=False).head(10)
    print("\nNajbardziej dochodowe kategorie:")
    print(top_kategorie[['kategoria', 'podkategoria', 'przychod_calkowity', 'marza_calkowita', 'marza_procent']])
    
    # Analiza 3: Segmentacja klientów według wartości zakupów
    analiza_klientow['segment_wartosci'] = pd.qcut(
        analiza_klientow['laczna_wartosc'], 
        q=[0, 0.5, 0.8, 0.95, 1.0], 
        labels=['Niski', 'Średni', 'Wysoki', 'Premium']
    )
    
    segmentacja_klientow = analiza_klientow.groupby('segment_wartosci').agg(
        liczba_klientow=('id_klienta', 'count'),
        srednia_wartosc=('laczna_wartosc', 'mean'),
        srednia_liczba_transakcji=('liczba_transakcji', 'mean'),
        srednia_wartosc_zamowienia=('srednia_wartosc_zamowienia', 'mean')
    ).reset_index()
    
    print("\nSegmentacja klientów według wartości zakupów:")
    print(segmentacja_klientow)
    
    # Analiza 4: Trendy sprzedaży miesięcznej
    # Konwersja okresu na datę dla wykresu
    sprzedaz_miesieczna['data'] = sprzedaz_miesieczna['rok_miesiac'].dt.to_timestamp()
    
    print("\nTrendy sprzedaży miesięcznej:")
    print(sprzedaz_miesieczna[['rok_miesiac', 'liczba_transakcji', 'liczba_klientow', 'laczna_wartosc']])
    
    # Analiza 5: RFM Analysis (Recency, Frequency, Monetary)
    analiza_klientow['recency_score'] = pd.qcut(
        analiza_klientow['dni_od_ostatniego_zakupu'], 
        q=5, 
        labels=[5, 4, 3, 2, 1]  # 5 to najlepszy wynik (najnowszy zakup)
    )
    
    analiza_klientow['frequency_score'] = pd.qcut(
        analiza_klientow['liczba_transakcji'].rank(method='first'), 
        q=5, 
        labels=[1, 2, 3, 4, 5]  # 5 to najlepszy wynik (najwięcej transakcji)
    )
    
    analiza_klientow['monetary_score'] = pd.qcut(
        analiza_klientow['laczna_wartosc'].rank(method='first'), 
        q=5, 
        labels=[1, 2, 3, 4, 5]  # 5 to najlepszy wynik (największa wartość)
    )
    
    # Wyliczenie łącznego wyniku RFM
    analiza_klientow['rfm_score'] = (
        analiza_klientow['recency_score'].astype(int) + 
        analiza_klientow['frequency_score'].astype(int) + 
        analiza_klientow['monetary_score'].astype(int)
    )
    
    # Segmentacja klientów na podstawie RFM
    analiza_klientow['rfm_segment'] = pd.qcut(
        analiza_klientow['rfm_score'], 
        q=[0, 0.2, 0.4, 0.6, 0.8, 1.0], 
        labels=['Uśpieni', 'Zagrożeni odpływem', 'Potencjalni', 'Lojalni', 'Najcenniejsi']
    )
    
    rfm_segmentacja = analiza_klientow.groupby('rfm_segment').agg(
        liczba_klientow=('id_klienta', 'count'),
        srednia_wartosc=('laczna_wartosc', 'mean'),
        srednia_liczba_transakcji=('liczba_transakcji', 'mean'),
        srednia_dni_od_ostatniego=('dni_od_ostatniego_zakupu', 'mean')
    ).reset_index()
    
    print("\nSegmentacja RFM klientów:")
    print(rfm_segmentacja)
    
    # Analiza 6: Analiza metod płatności
    metody_platnosci = transakcje.groupby('metoda_platnosci').agg(
        liczba_transakcji=('id_transakcji', 'count'),
        procent_transakcji=('id_transakcji', lambda x: len(x) / len(transakcje) * 100)
    ).reset_index()
    
    print("\nPopularność metod płatności:")
    print(metody_platnosci)
    
    # Analiza 7: Status zamówień
    status_zamowien = transakcje.groupby('status').agg(
        liczba_transakcji=('id_transakcji', 'count'),
        procent_transakcji=('id_transakcji', lambda x: len(x) / len(transakcje) * 100)
    ).reset_index()
    
    print("\nStatus zamówień:")
    print(status_zamowien)
    
    # Analiza 8: Analiza koszyków - najczęściej kupowane razem produkty
    # To jest uproszczona wersja analizy koszyków
    koszyki = linie_transakcji.merge(
        produkty[['id_produktu', 'nazwa_produktu', 'kategoria']], 
        on='id_produktu', 
        how='left'
    )
    
    # Grupowanie po transakcjach
    produkty_w_transakcjach = koszyki.groupby('id_transakcji')['nazwa_produktu'].apply(list).reset_index()
    
    # Zapisanie wyników analiz
    top_produkty.to_csv('output/top_produkty.csv', index=False)
    top_kategorie.to_csv('output/top_kategorie.csv', index=False)
    segmentacja_klientow.to_csv('output/segmentacja_klientow.csv', index=False)
    rfm_segmentacja.to_csv('output/rfm_segmentacja.csv', index=False)
    
    # Przygotowanie danych do wizualizacji
    return top_produkty, top_kategorie, sprzedaz_miesieczna, segmentacja_klientow, rfm_segmentacja

# Wykonujemy analizy
top_produkty, top_kategorie, sprzedaz_miesieczna, segmentacja_klientow, rfm_segmentacja = perform_analyses()

# ---------- 5. WIZUALIZACJE ----------

def create_visualizations():
    # Ustawienie stylu
    plt.style.use('seaborn-v0_8-whitegrid')
    
    # Wykres 1: Trendy sprzedaży miesięcznej
    plt.figure(figsize=(12, 6))
    plt.plot(sprzedaz_miesieczna['data'], sprzedaz_miesieczna['laczna_wartosc'], marker='o', linewidth=2)
    plt.title('Trendy sprzedaży miesięcznej', fontsize=14)
    plt.xlabel('Miesiąc', fontsize=12)
    plt.ylabel('Wartość sprzedaży (PLN)', fontsize=12)
    plt.grid(True)
    plt.tight_layout()
    plt.sav


xxx= create_visualizations()
print(xxx)