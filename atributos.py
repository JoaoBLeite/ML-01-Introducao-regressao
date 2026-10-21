"""Funções de engenharia de atributos do projeto California Housing.

Estas são as mesmas funções criadas nos notebooks 03 a 06. Elas ficam neste
arquivo (um "módulo" Python) para que possam ser IMPORTADAS por qualquer
notebook ou script com:

    from atributos import criar_derivados, criar_dist_cidade

Isso é necessário para salvar e carregar o modelo com joblib (veja o notebook
07): o arquivo salvo guarda apenas o NOME das funções usadas no pipeline, e
não o código delas. Ao carregar, o Python procura as funções por esse nome, e
precisa encontrá-las num módulo importável como este.
"""

import numpy as np

# Coordenadas aproximadas (latitude, longitude) dos dois grandes centros.
SAO_FRANCISCO = (37.77, -122.42)
LOS_ANGELES = (34.05, -118.24)


def criar_derivados(X):
    """Adiciona proporções: quartos por cômodo e cômodos por morador."""
    X = X.copy()   # copia para não alterar a tabela original
    X["BedrmsPerRoom"] = X["AveBedrms"] / X["AveRooms"]
    X["RoomsPerPerson"] = X["AveRooms"] / X["AveOccup"]
    return X


def distancia(X, cidade):
    """Distância aproximada (em graus) de cada bloco até uma cidade."""
    lat, lon = cidade
    return np.sqrt((X["Latitude"] - lat) ** 2 + (X["Longitude"] - lon) ** 2)


def criar_dist_cidade(X):
    """Adiciona a distância até a cidade grande mais próxima (SF ou LA)."""
    X = X.copy()
    X["DistCidade"] = np.minimum(distancia(X, SAO_FRANCISCO), distancia(X, LOS_ANGELES))
    return X
