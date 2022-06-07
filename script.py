# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %%
get_ipython().system('pip3 install pandas')
get_ipython().system('pip3 install openpyxl')


# %%
import pandas as pd


# %%
df = pd.read_excel('エラーコード一覧.xlsx', engine='openpyxl', header=1, index_col=0)


# %%
df


# %%
write_target = open('messages.properties', 'w')
for i, row in df.iterrows():
    write_target.write(row['エラーコード'].replace('-', '_')+'='+row['メッセージ'] + '\n')
write_target.close()


# %%



# %%



# %%



# %%



