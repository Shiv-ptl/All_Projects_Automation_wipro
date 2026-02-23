import threading
import time

def download_file(file_name):
    print(f"Downloading the file......{file_name}")
    time.sleep(2)
    print(f"{file_name} Downloaded.")

files = ["file.text","file2.text","file3.text"]

threads = [threading.Thread(target=download_file,args=(file,)) for file in files]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()