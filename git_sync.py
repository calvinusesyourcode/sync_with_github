import os

paths = [
    r"C:\Users\calvi\3D Objects\my_files",
    r"C:\Users\calvi\3D Objects\firebase-app\public",
    r"C:\Users\calvi\3D Objects\git_sync",
]

for path in paths:
    cmd = 'cd "'+ path + '" & git pull'
    os.system(cmd)
