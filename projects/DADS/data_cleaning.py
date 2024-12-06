from data_analysis import df

'''
Este arquivo conta com funções de exploração e limpeza de dados
Como verificação de valores nulos em cada célula de cada coluna do DataFrame
Verificação de Outliers, um loop que aplica isso em todas as colunas
Uma função de mapeamento para valores "Yes" e "No"
'''

# Tratando valores nulos
# Verificação de Outliers
# Funções de exemplo para mapeamento

lista_colunas = df.columns


def verifica_valores_nulos():
    # Verificar se existem valores nulos em cada coluna do DataFrame
    nulos = df.isnull().sum()
    
    # Exibir as colunas com valores nulos
    if nulos.any():  # Se houver alguma coluna com valores nulos
        print("Colunas com valores nulos:")
        print(nulos[nulos > 0])  # Exibe as colunas com valores nulos e a quantidade de nulos
    else:
        print("Não há valores nulos no DataFrame.")


def verifica_outliers(coluna):
    # Tentar identificar se a coluna é numérica antes de calcular outliers
    if df[coluna].dtype in ['float64', 'int64']:  # Verifica se a coluna é numérica
        Q1 = df[coluna].quantile(0.25)
        Q3 = df[coluna].quantile(0.75)
        IQR = Q3 - Q1

        limite_inferior = Q1 - 1.5 * IQR
        limite_superior = Q3 + 1.5 * IQR

        # Identificar outliers
        outliers = df[(df[coluna] < limite_inferior) | (df[coluna] > limite_superior)]
        
        if not outliers.empty:  # Exibir apenas se houver outliers
            print(f'Outliers na coluna {coluna}:')
            print(outliers)
        else:
            print(f'Nenhum outlier encontrado na coluna {coluna}.')
    else:
        print(f'A coluna {coluna} não contém dados numéricos válidos para calcular outliers.')


def loop_verifica_outliers():
    for coluna in lista_colunas:
        verifica_outliers(coluna)


def mapeia_respostas(coluna):
    # Verifica se a coluna é de tipo categórico
    if df[coluna].dtype == 'object':  # Verifica se a coluna é do tipo string
        # Mapeia "Yes" para 1 e "No" para 0. Outros valores serão mantidos inalterados
        df[coluna] = df[coluna].map({'Yes': 1, 'No': 0}).fillna(df[coluna])