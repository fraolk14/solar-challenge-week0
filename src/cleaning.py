# src/cleaning.py
import pandas as pd
import numpy as np
from scipy import stats

def load_standard(path, timestamp_col='Timestamp'):
    df = pd.read_csv(path)
    df.columns = [c.strip() for c in df.columns]
    if timestamp_col in df.columns:
        df[timestamp_col] = pd.to_datetime(df[timestamp_col], errors='coerce')
    else:
        for cand in ['timestamp','time','DateTime']:
            if cand in df.columns:
                df[timestamp_col] = pd.to_datetime(df[cand], errors='coerce'); break
    df = df.sort_values(timestamp_col).reset_index(drop=True)
    return df

def basic_profile(df):
    return {
        'rows': len(df),
        'dtypes': df.dtypes.to_dict(),
        'missing_counts': df.isna().sum().to_dict(),
        'describe': df.describe().to_dict()
    }

def impute_median(df, cols=None):
    if cols is None:
        cols = ['GHI','DNI','DHI','ModA','ModB','WS','WSgust','Tamb','RH','BP','Precipitation']
    imputed = []
    for c in cols:
        if c in df.columns:
            n_missing = int(df[c].isna().sum())
            if n_missing>0:
                median = df[c].median()
                df[c] = df[c].fillna(median)
                imputed.append((c, n_missing, float(median) if not pd.isna(median) else None))
    return df, imputed

def flag_outliers_z(df, cols=None, z_thresh=3.0):
    if cols is None:
        cols = ['GHI','DNI','DHI','ModA','ModB','WS','WSgust']
    flags = pd.DataFrame(index=df.index)
    for c in cols:
        if c in df.columns:
            vals = df[c].astype(float)
            if vals.nunique() <= 1:
                flags[c+'_z'] = np.nan
                flags[c+'_outlier'] = False
                continue
            z = np.abs(stats.zscore(vals.dropna()))
            s = pd.Series(index=vals.dropna().index, data=z)
            flags[c+'_z'] = s.reindex(df.index)
            flags[c+'_outlier'] = flags[c+'_z'] > z_thresh
        else:
            flags[c+'_z'] = np.nan
            flags[c+'_outlier'] = False
    return flags

def daytime_mask(df, ghi_col='GHI', threshold=10):
    if ghi_col in df.columns:
        return df[ghi_col] > threshold
    return pd.Series(True, index=df.index)
