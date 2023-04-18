import os

try: 
    log_path = r"C:\Users\calvi\3D Objects\git_sync\log.txt"
    paths = [
        r"C:\Users\calvi\3D Objects\my_files",
        r"C:\Users\calvi\3D Objects\firebase-app\public",
        r"C:\Users\calvi\3D Objects\git_sync",
    ]

    for path in paths:
        cmd = 'cd "'+ path + '" & git pull > "'+log_path+'"'
        os.system(cmd)

except Exception as e:
    print("Something happened: "+e)
    raise