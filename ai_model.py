
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def calculate_priority(df):
    df['sales_score'] = MinMaxScaler().fit_transform(df[['sales']])
    df['stock_score'] = 1 - MinMaxScaler().fit_transform(df[['stock']])
    df['new_score'] = df['new_arrival'].map({'yes': 1, 'no': 0})
    df['priority'] = 0.5 * df['sales_score'] + 0.3 * df['stock_score'] + 0.2 * df['new_score']
    return df.sort_values(by='priority', ascending=False)
