# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # File Compareing

# %%
import os
from pathlib import Path
import shutil


# %%
base_path = '.'

files = os.listdir(base_path)

dirs = [ name for name in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, name)) ]

dirs


# %%
for d in dirs:
    c_dir = os.path.join(base_path,d)
    print(c_dir)
    subfiles = os.listdir(d)
    print('size of file is', len(subfiles))

    # if single file is inside the directory, move the file.
    if len(subfiles) == 1:
        target_file = c_dir + '/' + subfiles[0]
        ext = os.path.splitext(target_file)
        print(ext)
        move_to = os.path.join(base_path, d +  ext[1])
        print('target file is', target_file)
        print('moving to', move_to)

        shutil.move(target_file, move_to)
        os.rmdir(c_dir)


# %%



