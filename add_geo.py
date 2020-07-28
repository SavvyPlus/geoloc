"""
"""

import time

import pandas as pd

import get_geo


IN_PATH = './data/{}/{}'
OUT_PATH = './data/{}/{}'


def add_lat_long(in_csv, out_csv, addr_cols=[], extral_info=''):
    df = pd.read_csv(in_csv, header=None)
    df.fillna('', inplace=True)
    rows = df.values.tolist()
    for row in rows:
        addr = ' '.join([str(row[i]) for i in addr_cols])
        addr = f'{addr} {extral_info}'        
        latitude, longitude = get_geo.get_lat_long(addr)
        row.append(latitude)
        row.append(longitude)
        print(row)
        time.sleep(1)
    df_final = pd.DataFrame(rows)
    df_final.to_csv(out_csv, header=None, index=None)


if __name__ == "__main__":
    source = 'urban'
    file_name = '280720.csv'
    in_csv = IN_PATH.format(source, file_name)
    out_csv = OUT_PATH.format(source, 'getloc_'+file_name)
    add_lat_long(in_csv, out_csv, addr_cols=[0, 1, 2, 3],
                 extral_info='Australia')
