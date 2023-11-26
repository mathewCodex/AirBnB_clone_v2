#!/usr/bin/python3
"""This module instantiates an object of class FileStorage
    create a unique FS instance for your app
"""
import os

from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

storage = DBStorage() if os.getenv(
    'HBNB_TYPE_STORAGE') == 'db' else FileStorage()
"""unique filestorage insta"""
storage.reload()
