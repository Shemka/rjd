import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from sklearn.linear_model import LinearRegression
import os
import subprocess

ROOT_DIR = os.path.dirname(os.path.abspath('plots'))
DIR_PLOTS = ROOT_DIR + '/plots/'

def process_df(df):
    df.columns = ['m', 'otst', 'st', 'deviation', 'len']
    df = df.sort_values(by='m').reset_index(drop=True)
    return df

# df2batch2df function !!!U DO NOT NEED THIS!!!
# Convert None to lowest possible number or leave number if there it is
def nn(n):
    return -1 if n is None else n

# Export 100m batches and convert it into DF
# GO DOWN
def df2batch2df(df):
    ush = None
    p = None
    prp = None
    prl = None
    r = None
    rows = []
    from_ = df['m'][0] - (df['m'][0] % 100)
    to = from_ + 100
    
    for j, i in enumerate(df['m']):
        if i is None:
            continue
        if i >= to:
            from_ += 100
            to += 100
            rows.append([len(rows), ush, p, prp, prl, r])
            ush = None
            p = None
            prp = None
            prl = None
            r = None

        if df.loc[j]['otst'] == 'Уш':
            ush = max([nn(ush), nn(df.iloc[j]['deviation'])])

        elif df.loc[j]['otst'] == 'П':
            p = max([nn(p), nn(df.iloc[j]['deviation'])])

        elif df.loc[j]['otst'] == 'Пр.п':
            prp = max([nn(prp), nn(df.iloc[j]['deviation'])])

        elif df.loc[j]['otst'] == 'Пр.л':
            prl = max([nn(prl), nn(df.iloc[j]['deviation'])])

        elif df.loc[j]['otst'] == 'Р':
            r = max([nn(p), nn(df.iloc[j]['deviation'])])

    rows.append([len(rows), ush, p, prp, prl, r])

    return pd.DataFrame(rows, columns=['id', 'уш', 'п', 'пр.п', 'пр.л', 'р'])

# Return False if x is not None or np.nan
def condition(x):
    if x is None:
        return False
    else:
        return not math.isnan(x)

# Calculate intersection with critical maximum/minimum
def inters(coefs, brd):
    x = (brd - coefs[1])/coefs[0]
    return x

# Plot approximated trend and save its plot into an image format
def plot_approx(id, col_n, dfs, save=False):
    plt.figure(figsize=(15, 5))
    plt.grid(True)
    
    # Collect Data
    x = [i for i in range(len(dfs))]
    y = []
    for i in x:
        val = dfs[i].values[id][col_n]
        y.append(val)
    x = list(filter(lambda x: condition(y[x]), x))
    y = list(filter(lambda x: condition(x), y))
    
    # Fit model
    clf = LinearRegression()
    clf.fit(np.array(x).reshape(-1, 1), y)
    cf = [clf.coef_[0], clf.intercept_]
    
    # Specify borders
    if col_n == 1:
        y_border = 1548
        brd_dwn = 1512
    elif col_n == 2:
        y_border = 50
        brd_dwn = 0
    elif col_n in [3, 4]:
        y_border = 45
        brd_dwn = 0
        
    x_u = inters(cf, y_border)
    x_d = inters(cf, brd_dwn)
    nx = max(x_u, x_d)
    ny = y_border if nx == x_u else brd_dwn
    
    plt.plot(x+[nx+10], [y_border for _ in x+[nx]], 'b--', label='Максимум/минимум')
    plt.plot(x+[nx+10], [brd_dwn for _ in x+[nx]], 'b--')
    plt.plot(x, clf.predict(np.array(x).reshape(-1,1)), 'g-', label='тренд')
    plt.plot([x[-1]]+[nx], [clf.predict(np.array(x).reshape(-1, 1))[-1]]+[ny], 'g--', label='предсказанный тренд')
    plt.scatter(x, y, label='измерения')
    plt.scatter([nx], [ny], label='критическая точка ~'+str(int(nx))+'\nмесяц с начала отсчета')
    plt.xlabel('ID месяца')
    plt.legend()
    
    # Plot saving
    if save:
        plt.savefig(save)

# Looking for closest "die date" for exact 100-meter
# Can save 
def closest_die_date(id, dfs, start_year=2019, start_month=2, img=True):
    mx = 999999999999
    с = 0
    for i in range(1, 5):
        x = [i for i in range(len(dfs))]
        y = []
        for j in x:
            val = dfs[j].values[id][i]
            y.append(val)
            
        x = list(filter(lambda x: condition(y[x]), x))
        y = list(filter(lambda x: condition(x), y))

        # Fit model
        clf = LinearRegression()
        try:
            clf.fit(np.array(x).reshape(-1, 1), y)
        except:
            continue
        cf = [clf.coef_[0], clf.intercept_]

        # Specify borders
        if i == 1:
            y_border = 1548
            brd_dwn = 1512

        elif i == 2:
            y_border = 50
            brd_dwn = 0

        elif i in [3, 4]:
            y_border = 45
            brd_dwn = 0

        x_u = inters(cf, y_border)
        x_d = inters(cf, brd_dwn)
        nx = max(x_u, x_d)
        ny = y_border if nx == x_u else brd_dwn
        if ny == brd_dwn and i in [2, 3, 4]:
            continue
        mx = min(mx, nx)
        if mx == nx:
            c = i
    
    if img:
        cols = list(dfs[0].columns)
        plot_approx(id, c, dfs, str(start_year)+'-'+str(start_month)+'/plots/'+cols[i]+str(id)+'.jpg')
    return int(mx), str(start_year)+'-'+str(start_month)+'/plots/'+cols[i]+str(id)+'.jpg'

# Batches counter
def min_ids(dfs):
    mn = 11
    for i in range(len(dfs)):
        mn = min(dfs[i].shape[0], mn)
    return mn

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!! YOU NEED ONLY THIS ONE !!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# It is return PATH to excel file
def problems_to_excel(dfs, start_year=2019, start_month=2):
    rows = []
    if not str(start_year)+'-'+str(start_month) in os.listdir():
        os.mkdir(str(start_year)+'-'+str(start_month))
        os.mkdir(str(start_year)+'-'+str(start_month)+'/plots')
    for i in range(min_ids(dfs)):
        m, path = closest_die_date(i, dfs, start_year, start_month)
        rows.append([str(i*100)+'-'+str((i+1)*100)+'м', str(start_month+m%12)+'-'+str(start_year+m//12)])
    pd.DataFrame(rows, columns=['промежуток', 'критическая_дата']).to_excel('critical-from-'+str(start_year)+'-'+str(start_month)+'.xlsx')
    return os.path.join(ROOT_DIR, 'critical-from-'+str(start_year)+'-'+str(start_month)+'.xlsx')