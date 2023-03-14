import sys

import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = r"C:\Users\ASHUTOSH ARYAN\Downloads"
to_dir = r"C:\Users\ASHUTOSH ARYAN\OneDrive\Desktop\coding\module 3\project\C---103[WATCH FILE SYSTEM EVENTS]"


dir_collection = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f"hey {event.src_path} created!")

        name, ext = os.path.splitext(event.src_path)
        for key,value in dir_collection.items():
            if ext in value:
                doc_name=os.path.basename(event.src_path)
                print(doc_name)

                source=from_dir + r"\\" + doc_name
                destination=to_dir + r"\\" + key

                if not os.path.exists(destination):
                    os.mkdir(destination)
                    destination_folder=to_dir + r"\\" + doc_name

                    shutil.move(source,destination_folder)
                    print("moved!!")

    def on_deleted(self, event):
        print(f"oops! something went wrong {event.src_path} !")


handler = FileEventHandler()

observer = Observer()

observer.schedule(handler,from_dir,recursive=True)

observer.start()

try:
    while True:
        time.sleep(4)
        print("running...")
except KeyboardInterrupt:
    print("Stopped!")
    observer.stop()