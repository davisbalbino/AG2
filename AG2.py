import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


dados = pd.read_csv("AG2\dados\palmerpenguins.csv")

island= {'Biscoe': 0, 'Dream': 1, 'Torgersen': 2}
coluna_island = 'island' 
sex= {'FEMALE': 0,'MALE': 1 }
coluna_sex = 'sex'  
species= {'Adeline': 0, 'Adelie': 0, 'Chinstrap': 1, 'Gentoo': 2}
coluna_species = 'species'  


dados[coluna_island] = dados[coluna_island].replace(island)
dados[coluna_sex] = dados[coluna_sex].replace(sex)
dados[coluna_species] = dados[coluna_species].replace(species)

ordem_colunas_desejada = []
dados = dados.reindex(columns=['island', 'sex', 'culmen_length_mm', 'culmen_depth_mm', 'flipper_length_mm', 'body_mass_g', 'species'])
dados.to_csv("AG2\dados\palmerpenguins.csv", index=False)

X = dados.drop(columns=['species'])  # Recursos (features)
y = dados['species']  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar um modelo de árvore de decisão
modelo = DecisionTreeClassifier(random_state=42)
modelo.fit(X_train, y_train)

# Avaliar a precisão do modelo
acuracia = modelo.score(X_test, y_test)
print(f"Acurácia do modelo: {acuracia:.2f}")