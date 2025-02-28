"""
Zadanie: Analiza sprzedaży sklepu

Opis: W tym ćwiczeniu przeanalizujesz dane sprzedażowe małego sklepu internetowego.
Przejdziesz przez podstawowe operacje Pandas, takie jak wczytywanie danych, 
czyszczenie, transformacje, grupowanie i wizualizację.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# 1. Generowanie przykładowych danych
def generate_data():
    # Ustawienie seeda dla powtarzalności wyników
    np.random.seed(42)
    
    # Generowanie dat
    start_date = datetime(2023, 1, 1)
    end_date = datetime(2023, 3, 31)
    days = (end_date - start_date).days + 1
    
    dates = [start_date + timedelta(days=i) for i in range(days)]
    # Losowo wybieramy podzbiór dat, aby symulować nieregularne zakupy
    selected_dates = np.random.choice(dates, size=500, replace=True)
    selected_dates.sort()
    
    # Produkty
    products = ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Keyboard', 'Mouse', 'Monitor', 'Printer']
    categories = {
        'Laptop': 'Electronics',
        'Smartphone': 'Electronics',
        'Tablet': 'Electronics',
        'Headphones': 'Accessories',
        'Keyboard': 'Accessories',
        'Mouse': 'Accessories',
        'Monitor': 'Electronics',
        'Printer': 'Electronics'
    }
    
    prices = {
        'Laptop': 3500,
        'Smartphone': 1800,
        'Tablet': 1200,
        'Headphones': 350,
        'Keyboard': 150,
        'Mouse': 80,
        'Monitor': 800,
        'Printer': 600
    }
    
    # Generowanie danych sprzedaży
    data = []
    
    for i in range(500):
        date = selected_dates[i]
        product = np.random.choice(products)
        category = categories[product]
        price = prices[product]
        quantity = np.random.randint(1, 4)
        
        # Dodajemy losowy rabat dla niektórych produktów
        discount = np.random.choice([0, 5, 10, 15], p=[0.7, 0.1, 0.1, 0.1])
        price_after_discount = price * (1 - discount/100)
        
        # Region
        region = np.random.choice(['North', 'South', 'East', 'West'], p=[0.3, 0.2, 0.25, 0.25])
        
        data.append({
            'order_id': f'ORD-{i+1000}',
            'date': date,
            'product': product,
            'category': category,
            'price': price,
            'discount_percent': discount,
            'price_after_discount': price_after_discount,
            'quantity': quantity,
            'total_amount': price_after_discount * quantity,
            'region': region
        })
    
    # Tworzenie DataFrame
    df = pd.DataFrame(data)
    
    # Zapisanie do CSV
    df.to_csv('sales_data.csv', index=False)
    
    print("Dane zostały wygenerowane i zapisane do pliku 'sales_data.csv'")
    return df

# Generowanie danych
sales_df = generate_data()

# 2. Zadania do wykonania

# ZADANIE 1: Wczytaj dane z pliku CSV i wyświetl podstawowe informacje
# ------------------------------------------------------------------
# TODO: Wczytaj dane z 'sales_data.csv' i wyświetl podstawowe informacje
# Wskazówka: Użyj funkcji read_csv, head(), info(), describe()

# Twój kod tutaj:

df = pd.read_csv('sales_data.csv')
df.info()
df.head(10)
df.describe()



# ZADANIE 2: Przygotowanie i czyszczenie danych
# ------------------------------------------------------------------
# TODO: Wykonaj poniższe kroki:
# 1. Sprawdź czy istnieją brakujące wartości
# 2. Upewnij się, że kolumna 'date' jest typu datetime
# 3. Dodaj nowe kolumny: 'year', 'month', 'day' na podstawie kolumny 'date'
# 4. Oblicz kolumnę 'profit' jako różnicę między 'total_amount' a kosztem
#    (załóżmy, że koszt to 60% ceny przed rabatem)

# Twój kod tutaj:

df.isna().any()

df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
df['profit'] = df['total_amount'] - (df['price'] * df['quantity'] * 0.6)
 
print(df)


# ZADANIE 3: Analiza sprzedaży
# ------------------------------------------------------------------
# TODO: Wykonaj poniższe analizy:
# 1. Oblicz całkowitą sprzedaż, liczbę zamówień i średnią wartość zamówienia
# 2. Znajdź 3 najlepiej sprzedające się produkty pod względem wartości
# 3. Przeanalizuj sprzedaż miesięczną

# Twój kod tutaj:

product_sales = df.groupby('product').agg({
    'total_amount': ['sum', 'count', 'mean']
}).sort_values(('total_amount', 'sum'), ascending=False).head(3)

print(product_sales)

# ZADANIE 4: Grupowanie i agregacja danych
# ------------------------------------------------------------------
# TODO: Wykonaj poniższe grupowania i agregacje:
# 1. Sprzedaż według kategorii produktów
# 2. Sprzedaż według regionów
# 3. Sprzedaż miesięczna z podziałem na kategorie

# Twój kod tutaj:
category_sales = df.groupby('category')['total_amount'].sum().sort_values(ascending=False)
print(category_sales)

region_sales = df.groupby('region')['total_amount'].sum().sort_values(ascending=False)
print(region_sales)

monthy_category_sales = df.groupby(['month','region'])['total_amount'].sum().sort_values(ascending=False)
print(monthy_category_sales)

# ZADANIE 5: Analiza rabatów
# ------------------------------------------------------------------
# TODO: Przeanalizuj wpływ rabatów na sprzedaż:
# 1. Jaki jest średni rabat dla każdej kategorii?
# 2. Jak rabaty wpływają na liczbę sprzedanych produktów?
# 3. Który region ma najwyższe rabaty?

# Twój kod tutaj:



# ZADANIE 6: Wizualizacja danych
# ------------------------------------------------------------------
# TODO: Stwórz następujące wizualizacje:
# 1. Wykres słupkowy przedstawiający sprzedaż według kategorii
# 2. Wykres liniowy przedstawiający miesięczną sprzedaż
# 3. Wykres kołowy przedstawiający udział regionów w sprzedaży

# Twój kod tutaj:



# ZADANIE 7: Zaawansowana analiza
# ------------------------------------------------------------------
# TODO: Wykonaj bardziej zaawansowane analizy:
# 1. Znajdź produkty, których sprzedaż rośnie najbardziej miesiąc do miesiąca
# 2. Zidentyfikuj dni tygodnia z najwyższą sprzedażą
# 3. Przeanalizuj korelację między wielkością rabatu a ilością sprzedanych produktów

# Twój kod tutaj:



# ZADANIE 8: Zapisz przetworzone dane i wyniki
# ------------------------------------------------------------------
# TODO: Zapisz przetworzone dane i wyniki analizy:
# 1. Zapisz przetworzony DataFrame do pliku CSV
# 2. Zapisz tabele przestawne dla kategorii i regionów do pliku Excel
# 3. Zapisz wykresy do plików PNG

# Twój kod tutaj:


# Rozwiązania do zadań:

# Przykładowe rozwiązanie ZADANIA 1:
print("\n--- ROZWIĄZANIE ZADANIA 1 ---")
# Wczytywanie danych
sales = pd.read_csv('sales_data.csv')
print("Pierwsze 5 wierszy:")
print(sales.head())

print("\nInformacje o danych:")
sales.info()

print("\nStatystyki opisowe:")
print(sales.describe())