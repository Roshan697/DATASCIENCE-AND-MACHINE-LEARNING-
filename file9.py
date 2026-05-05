##getting an absolute path
import os

relative_path = 'example.txt'
absolute_path = os.path.abspath(relative_path)
print(absolute_path)