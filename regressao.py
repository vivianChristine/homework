
import pandas as pd
import numpy as np

def calcular_regressao(arquivo):

    
    df = pd.read_csv(arquivo)

  
    X = np.column_stack([
        np.ones(len(df)),
        df["area_util_m2"],
        df["quantidade_quartos"]
    ])

    y = df["preco_venda"].to_numpy()
    beta = np.linalg.lstsq(X, y, rcond=None)[0]
    return beta.tolist()

resultado = calcular_regressao("imoveis_lar_perfeito.csv")

print(resultado)
