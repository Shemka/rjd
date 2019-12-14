import pandas as pd

def tensor2dfs(tensor):
    '''tensor is a list of matrixes. returns list of '''
    dfs = []
    for matrix in tensor:
        df = pd.DataFrame(matrix)
        dfs.append(df.copy())
    return dfs
