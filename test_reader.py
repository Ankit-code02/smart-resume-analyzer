import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BASE_DIR)

from utils.file_reader import read_resume

print(read_resume("uploads/test_resume.txt"))
