import pandas as pd
import matplotlib.pyplot as plt

'''
Este arquivo conta com uma função simples para a análise de dados
de uma coluna qualquer em relação à coluna de depressão.
Para a exibição da quantidade de registros foram usados prints
e para visualização dos dados foi usada a lib matplotlib
'''

# Carrega o dataset
df = pd.read_csv('/home/biel/Downloads/depressao.zip', compression='zip')


def analyze_depression(column, value):
    """
    Função genérica para analisar a relação entre uma coluna do DataFrame e a depressão.

    Parâmetros:
        column (str): Nome da coluna que será analisada junto com depressão.
        value: Valor na coluna a ser filtrado.
    """

    # Cria a máscara booleana para a condição
    condition = (df[column] == value) & (df['Depression'] == 'Yes')

    # Conta o número de pessoas que satisfazem a condição
    num_pessoas = condition.sum()
    print(f"Número de pessoas com 'Depression' = 'Yes' e '{column}' = {value}: {num_pessoas}")

    # Cria uma figura com 2 subgráficos (1 linha e 2 colunas)
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    # Histograma para a coluna analisada
    df[condition][column].hist(ax=axes[0])
    axes[0].set_title(f'Histograma de {column}')

    # Histograma para 'Depression'
    df[condition]['Depression'].map({'Yes': 1, 'No': 0}).hist(ax=axes[1])
    axes[1].set_title('Histograma de Depression')

    # Exibe o gráfico
    plt.tight_layout()
    plt.show()



# Exemplo de Análise facilitada com loop
if __name__ == '__main__':
    for i in range(1, 6):
        analyze_depression('Financial Stress', i)