import os

paths = [
    r"C:\Users\calvi\3D Objects\my_files",
    r"C:\Users\calvi\3D Objects\firebase-app\public",
]

for item in paths:
    cmd = 'cd "'+ item + '" & git pull'
    os.system(cmd)