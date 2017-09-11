import pandas as pd
import numpy as np
import csv

small_press = pd.read_csv('/Users/rdubnic2/Desktop/smallpress_allnovels_2.csv', sep=None)
# small_press.head()

small_press_titles = pd.Series.tolist(small_press['TITLE'])
print(len(small_press_titles))

rh = pd.read_csv('/Users/rdubnic2/Desktop/RH_NOVELS_FINAL.csv')
# rh.head()

rh_titles = pd.Series.tolist(rh['TITLE'])
print(len(rh_titles))

ht_all = pd.read_csv('/Users/rdubnic2/Desktop/hathi_1950_2000_all_texts_2.csv', sep=None)
# ht_all.head()

ht_all_titles = pd.Series.tolist(ht_all['TITLE'])
print(len(ht_all_titles))

all_titles = small_press_titles + rh_titles

print(len(all_titles))
# all_titles

ht_all_copy = ht_all

print('Shape of DF before winnow ', ht_all_copy.shape)

for i in ht_all_copy.index:
    title = ht_all_copy['TITLE'][i]
    if title not in all_titles:
        ht_all_copy.drop([i])

print('Shape of DF after winnow ', ht_all_copy.shape)
