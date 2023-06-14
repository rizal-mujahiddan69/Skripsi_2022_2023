import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
sns.set()
tahun  = []
dataku = []
for i in range(1997,2022):
    name_df = "df_" + str(i)
    globals()[name_df]  = pd.read_excel("Produksi Tanaman Buah-buahan_"+str(i)+".xlsx",skiprows=1)
    globals()[name_df].drop(0,inplace=True)
    # print(globals()[name_df].head())
    globals()[name_df] = globals()[name_df][:35].copy()
    kolom_df= list(globals()[name_df])
    kolom_df[0] = 'Provinsi'
    globals()[name_df].columns = kolom_df
    globals()[name_df].replace(r'^-$',0,regex=True,inplace=True)
    globals()[name_df].replace(np.nan,0,inplace=True)

    for kol in kolom_df[1:]:
        globals()[name_df][kol] = globals()[name_df][kol].astype('float64')
    dataku.append(globals()[name_df]['Manggis (Ton)'].sum())
    tahun.append(i)
df_manggis = pd.DataFrame({"tahun":tahun,"berat_manggis":dataku})
gg = sns.pointplot(data=df_manggis,x='tahun',y='berat_manggis')

gg.set(title="grafik garis banyaknya produksi manggis (ton) berdasarkan tahun")
gg.set_xticklabels(gg.get_xticklabels(),rotation=300)
# gg.set_xticklabels(rotation=30)
plt.show()