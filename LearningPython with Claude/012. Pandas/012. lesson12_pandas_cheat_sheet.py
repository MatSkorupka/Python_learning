import pandas as pd
import numpy as np

# --- 1. PODSTAWOWE STRUKTURY DANYCH ---

# Series - jednowymiarowa tablica z etykietami
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print("Series:")
print(s)

# DataFrame - dwuwymiarowa tabela z etykietami wierszy i kolumn
dates = pd.date_range('20230101', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print("\nDataFrame z losowymi danymi:")
print(df)

# Tworzenie DataFrame ze słownika
data = {'miasto': ['Warszawa', 'Kraków', 'Gdańsk', 'Poznań'],
        'populacja': [1790658, 780000, 470907, 538633],
        'powierzchnia': [517.2, 326.8, 262.0, 261.8]}
df2 = pd.DataFrame(data)
print("\nDataFrame ze słownika:")
print(df2)

# --- 2. WCZYTYWANIE I ZAPISYWANIE DANYCH ---

# Wczytywanie CSV
df_csv = pd.read_csv('dane.csv', sep=',', encoding='utf-8')

# Wczytywanie Excel
df_excel = pd.read_excel('dane.xlsx', sheet_name='Arkusz1')

# Wczytywanie JSON
df_json = pd.read_json('dane.json')

# Wczytywanie z bazy SQL
from sqlalchemy import create_engine
engine = create_engine('sqlite:///baza.db')
df_sql = pd.read_sql_query("SELECT * FROM tabela", engine)

# Zapisywanie danych
df.to_csv('wynik.csv', index=False)
df.to_excel('wynik.xlsx', sheet_name='Arkusz1')
df.to_parquet('wynik.parquet', compression='snappy')  # Format kolumnowy

# --- 3. PRZEGLĄDANIE I ANALIZA DANYCH ---

print("\nPodgląd danych - head():")
print(df.head(3))  # Pierwsze 3 wiersze

print("\nPodgląd danych - tail():")
print(df.tail(2))  # Ostatnie 2 wiersze

print("\nLosowe wiersze - sample():")
print(df.sample(2))  # Losowe 2 wiersze

print("\nInformacje o DataFrame - info():")
df.info()  # Typy danych i liczba niepustych wartości

print("\nStatystyki - describe():")
print(df.describe())  # Statystyki dla kolumn numerycznych

print("\nWybieranie pojedynczej kolumny:")
print(df['A'])  # Pojedyncza kolumna

print("\nWybieranie wielu kolumn:")
print(df[['A', 'B']])  # Wiele kolumn

print("\nWybieranie wiersza po indeksie etykiety:")
print(df.loc[dates[0]])  # Wiersz po indeksie etykiety

print("\nWybieranie wierszy i kolumn po pozycji numerycznej:")
print(df.iloc[1:3, 0:2])  # Wiersze i kolumny po pozycji numerycznej

print("\nFiltrowanie wg warunku:")
print(df[df['A'] > 0])  # Filtrowanie wg warunku

# --- 4. TRANSFORMACJE DANYCH ---

print("\nSortowanie wg wartości:")
print(df.sort_values(by='B', ascending=False))

print("\nSortowanie wg indeksu:")
print(df.sort_index())

print("\nGrupowanie i suma:")
# Tworzymy nowy DataFrame dla przykładu grupowania
df_group = pd.DataFrame({
    'A': ['one', 'one', 'two', 'three', 'two', 'one'],
    'B': ['x', 'y', 'x', 'y', 'y', 'x'],
    'C': np.random.randn(6),
    'D': np.random.randn(6)
})
print(df_group.groupby('A').sum())

print("\nGrupowanie z wieloma agregacjami:")
print(df_group.groupby(['A', 'B']).agg({'C': 'mean', 'D': ['min', 'max']}))

print("\nŁączenie danych - merge():")
left = pd.DataFrame({'klucz': ['K0', 'K1', 'K2', 'K3'],
                     'A': ['A0', 'A1', 'A2', 'A3'],
                     'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'klucz': ['K0', 'K1', 'K2', 'K3'],
                      'C': ['C0', 'C1', 'C2', 'C3'],
                      'D': ['D0', 'D1', 'D2', 'D3']})
print(pd.merge(left, right, on='klucz', how='inner'))

print("\nŁączenie w pionie - concat() axis=0:")
print(pd.concat([left, right], axis=0))

print("\nTransformacje kształtu - pivot():")
df_pivot = pd.DataFrame({
    'data': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02'],
    'kategoria': ['A', 'B', 'A', 'B'],
    'wartość': [100, 200, 150, 250]
})
print(pd.pivot_table(df_pivot, values='wartość', index='data', columns='kategoria'))

print("\nTransformacje kształtu - melt():")
df_wide = pd.DataFrame({
    'id': [1, 2, 3],
    'A': [10, 20, 30],
    'B': [100, 200, 300]
})
print(pd.melt(df_wide, id_vars=['id'], value_vars=['A', 'B']))

# --- 5. CZYSZCZENIE DANYCH ---

print("\nBrakujące wartości - tworzenie DataFrame z brakami:")
df_na = pd.DataFrame({
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, np.nan, 8],
    'C': [9, 10, 11, 12]
})
print(df_na)

print("\nSuma brakujących wartości w każdej kolumnie:")
print(df_na.isna().sum())

print("\nUsuwanie wierszy z brakującymi wartościami:")
print(df_na.dropna())

print("\nWypełnianie braków:")
print(df_na.fillna(value={'A': 0, 'B': df_na['B'].mean()}))

print("\nSprawdzanie duplikatów:")
df_dup = pd.DataFrame({
    'A': [1, 1, 2, 3],
    'B': [1, 1, 2, 3]
})
print(df_dup)
print("Liczba zduplikowanych wierszy:", df_dup.duplicated().sum())

print("\nUsuwanie duplikatów:")
print(df_dup.drop_duplicates())

print("\nTransformacje typów:")
df_types = pd.DataFrame({
    'data': ['2023-01-01', '2023-01-02', '2023-01-03'],
    'kategoria': ['A', 'B', 'A'],
    'wartość': ['10', '20', '30']
})
print("Przed konwersją:")
print(df_types.dtypes)

df_types['data'] = pd.to_datetime(df_types['data'])
df_types['kategoria'] = df_types['kategoria'].astype('category')
df_types['wartość'] = pd.to_numeric(df_types['wartość'])

print("Po konwersji:")
print(df_types.dtypes)

# --- 6. OPERACJE WYDAJNOŚCIOWE ---

print("\nWektoryzacja zamiast pętli:")
df['nowa'] = df['A'] * 2 + df['B']
print(df.head(3))

print("\nStosowanie funkcji apply():")
print(df['A'].apply(lambda x: x * 2))

print("\nStosowanie funkcji apply() na całym DataFrame:")
print(df.apply(lambda x: x.max() - x.min()))

print("\nOptymalizacja pamięci - informacja o użyciu pamięci:")
print(df.memory_usage(deep=True))

# --- 7. ANALIZA CZASOWA ---

print("\nTworzenie serii dat:")
daty = pd.date_range(start='2023-01-01', end='2023-01-10', freq='D')
print(daty)

print("\nTworzenie DataFrame z datami:")
df_time = pd.DataFrame({
    'data': daty,
    'wartosc': np.random.randn(len(daty))
})
print(df_time)

print("\nUstawienie indeksu daty i resampling:")
df_time = df_time.set_index('data')
print("Dane miesięczne (średnia):")
print(df_time.resample('3D').mean())  # Agregacja co 3 dni

print("\nPrzesunięcia czasowe:")
df_time['poprzedni_dzien'] = df_time['wartosc'].shift(1)
df_time['zmiana'] = df_time['wartosc'] - df_time['poprzedni_dzien']
print(df_time)

print("\nOkna czasowe (średnia krocząca):")
df_time['srednia_kroczaca'] = df_time['wartosc'].rolling(window=3).mean()
print(df_time)

# --- 8. PRZYPADEK PRAKTYCZNY DLA DATA ENGINEERING ---

print("\nPrzykład na danych transakcyjnych:")
# Tworzenie przykładowych danych transakcyjnych
transakcje = pd.DataFrame({
    'data_transakcji': pd.date_range(start='2023-01-01', periods=100, freq='D').repeat(5),
    'id_klienta': np.random.choice(['K001', 'K002', 'K003', 'K004', 'K005'], size=500),
    'id_transakcji': ['T' + str(i).zfill(6) for i in range(1, 501)],
    'kwota': np.random.randint(10, 1000, size=500)
})

print("Przykładowe dane transakcyjne:")
print(transakcje.head())

print("\nAgregacje miesięczne:")
miesieczne_obroty = transakcje.set_index('data_transakcji').resample('M').agg({
    'kwota': 'sum',
    'id_transakcji': 'count'
}).rename(columns={'id_transakcji': 'liczba_transakcji'})
print(miesieczne_obroty)

print("\nTop klienci:")
top_klienci = transakcje.groupby('id_klienta').agg({
    'kwota': ['sum', 'mean', 'count']
}).sort_values(('kwota', 'sum'), ascending=False)
print(top_klienci)

# --- 9. INTEGRACJA Z GCP ---

# Łączenie z BigQuery - przykładowy kod
"""
from google.cloud import bigquery
client = bigquery.Client()

# Wczytywanie danych z BigQuery do pandas
query = '''
SELECT * 
FROM `projekt.dataset.tabela`
WHERE data > '2023-01-01'
'''
df_bq = client.query(query).to_dataframe()

# Zapisywanie danych do BigQuery
df.to_gbq(destination_table='projekt.dataset.nowa_tabela',
          project_id='twoj-projekt-gcp',
          if_exists='replace')

# Wczytywanie/zapisywanie do Cloud Storage
df.to_csv('gs://twoj-bucket/dane.csv')
df = pd.read_csv('gs://twoj-bucket/dane.csv')
"""