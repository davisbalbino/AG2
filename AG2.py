from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

dados = pd.read_csv("AG2\dados\palmerpenguins.csv")

island = {'Biscoe': 0, 'Dream': 1, 'Torgersen': 2}
sex = {'FEMALE': 0, 'MALE': 1}
species = {'Adeline': 0, 'Adelie': 0, 'Chinstrap': 1, 'Gentoo': 2}

dados['island'] = dados['island'].replace(island)
dados['sex'] = dados['sex'].replace(sex)
dados['species'] = dados['species'].replace(species)

dados = dados.reindex(columns=['island', 'sex', 'culmen_length_mm', 'culmen_depth_mm', 'flipper_length_mm', 'body_mass_g', 'species'])
dados.to_csv("AG2\dados\palmerpenguins.csv", index=False)

X = dados.drop(columns=['species'])  # Recursos (features)
y = dados['species']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = DecisionTreeClassifier(random_state=42)
modelo.fit(X_train, y_train)

acuracia = modelo.score(X_test, y_test)
print(f"Acurácia do modelo: {acuracia:.2f}")

predict = modelo.predict(X_test)

relatorio_classificacao = classification_report(y_test, predict, target_names=['Adelie', 'Chinstrap', 'Gentoo'])
print("Relatório de Classificação:\n", relatorio_classificacao)

def classificar_novos_dados(modelo):

    print("Insira os seguintes dados para classificação:")
    island = int(input("Ilha (0 para Biscoe, 1 para Dream, 2 para Torgersen): "))
    sex = int(input("Sexo (0 para FEMALE, 1 para MALE): "))
    culmen_length_mm = float(input("Comprimento do culmen (mm): "))
    culmen_depth_mm = float(input("Profundidade do culmen (mm): "))
    flipper_length_mm = float(input("Comprimento da nadadeira (mm): "))
    body_mass_g = float(input("Massa corporal (g): "))
    
    # Criar um DataFrame com os dados inseridos
    novos_dados = pd.DataFrame([[island, sex, culmen_length_mm, culmen_depth_mm, flipper_length_mm, body_mass_g]],
                               columns=['island', 'sex', 'culmen_length_mm', 'culmen_depth_mm', 'flipper_length_mm', 'body_mass_g'])
    
    predicao = modelo.predict(novos_dados)
    especies = {0: 'Adelie', 1: 'Chinstrap', 2: 'Gentoo'}

    print(f"A previsão do modelo é que o pinguim pertence à espécie: {especies[predicao[0]]}")

classificar_novos_dados(modelo)
