#Q3
from abc import ABC, abstractmethod


class Document(ABC):
    def __init__(self, file_name, file_size, content):
        self.file_name = file_name
        self.file_size = file_size
        self.content = content

  