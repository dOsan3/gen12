# text_reader.py
import os
import io
from pathlib import Path

def read_text_file(file_name, subdirectory='data'):
    file_path = Path(os.getcwd()) / subdirectory / file_name

    with io.open(file_path, 'r', encoding='utf-8') as file:
        file_content = file.read()

    return file_content