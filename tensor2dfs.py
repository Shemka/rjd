import pandas as pd

def tensor2dfs(tensor):
    '''tensor is a list of matrixes. returns list of '''
    dfs = []
    for matrix in tensor:
        df = pd.DataFrame(matrix, columns='м Отст Ст Откл Дл Кол'.split())
        dfs.append(df.copy())
    return dfs
