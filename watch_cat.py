# -*- coding: utf-8 -*-

import os
import time
import shutil

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

BASE_DIR = "C:\\iCloud\\DL"
DEST_DIR = "C:\\GDrive\\icloud\\2017"

def getext(filename):
    return os.path.splitext(filename)[-1].lower()


class WatchHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        if getext(event.src_path) in ('.jpg','.png','.txt'):
            shutil.copy(event.src_path, DEST_DIR)

if __name__ in '__main__':
    while 1:
        event_handler = WatchHandler()
        observer = Observer()
        observer.schedule(event_handler,BASE_DIR,recursive=True)
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
