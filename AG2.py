from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

dados = pd.read_csv("dados\palmerpenguins.csv")
amostras = dados.shape[0] - 1

mapa_island = {'Biscoe': 0,'Dream':1,'Torgersen': 2}
mapa_sex = {'FEMALE':0,'MALE': 1}
mapa_species = {'Adelie': 0, 'Chinstrap': 1, 'Gentoo': 2}

dados['island'] = dados['island'].replace(mapa_island)
dados['sex'] = dados['sex'].replace(mapa_sex)
dados['species'] = dados['species'].replace(mapa_species)

print(dados)

dados = dados.reindex(columns=['island', 'sex', 'culmen_length_mm', 'culmen_depth_mm','body_mass_g','species'])

print(dados)

x_train, x_test = train_test_split(dados, test_size=0.2,random_state=42)

print(x_train, x_test)