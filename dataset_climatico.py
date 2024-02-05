import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
file_name = 'dataset_climatico.csv'

df = pd.read_csv(file_name)

# pulizia dei dati

df.dropna(inplace=True)
#colonne da normalizzare
colonne_data = ['temperatura_media', 'precipitazioni', 'umidita','velocita_vento']
#media 
mean = df[colonne_data].mean()
#calcola la deviazione standard
std_dev = df[colonne_data].std()
#Normalizzazione Z-score
z_score = (df[colonne_data]-mean)/std_dev
#printiamo
print('dati normalizzati Z-score', z_score)

df.describe()

print(df.describe())

#creare grafici(istogrammi,box plots) per visualizzare la distribuzione di ciascuna variabile normalizzata.

# Creazione di una figura e dei sotto-grafici
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# Istogramma per la temperatura media
axs[0, 0].hist(z_score['temperatura_media'], bins=20, color='blue', alpha=0.7,edgecolor='black')
axs[0, 0].set_title('Distribuzione della temperatura media')

# Istogramma per le precipitazioni
axs[0, 1].hist(z_score['precipitazioni'], bins=20, color='green', alpha=0.7, edgecolor='black')
axs[0, 1].set_title('Distribuzione delle precipitazioni')

# Istogramma per l'umidità
axs[1, 0].hist(z_score['umidita'], bins=20, color='red', alpha=0.7,edgecolor='black')
axs[1, 0].set_title('Distribuzione dell\'umidità')

# Istogramma per la velocità del vento
axs[1, 1].hist(z_score['velocita_vento'], bins=20, color='orange', alpha=0.7,edgecolor='black')
axs[1, 1].set_title('Distribuzione della velocità del vento')

# Aggiunta di spaziatura tra i grafici
plt.tight_layout()

# Mostra il grafico
plt.show()
#Istogramma del dataframe normalizzato
plt.hist(z_score)
plt.title('Distribuzione delle variabili normalizzate')
plt.xlabel('Valore normalizzato')
plt.ylabel('Frequenza')
plt.legend()
plt.show()

#visualizzazione della distribuzione tramite box plots

plt.figure(figsize=(10,6))

plt.boxplot(z_score.values, labels = colonne_data)
plt.title('Box plot delle variabili normalizzate')
plt.xlabel('Variabile')
plt.ylabel('Valore normalizzato')
plt.grid(True)
plt.show()

# Calcolo della matrice di correlazione
correlation_matrix = z_score.corr()

# Creazione della heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlazione tra variabili meteorologiche')
plt.show()

