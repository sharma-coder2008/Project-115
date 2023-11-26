import os

old_files_names = ["C:/Users/HP/Downloads/Python_Classes/old_files/old_file1.txt","C:/Users/HP/Downloads/Python_Classes/old_files/old_file2.txt","C:/Users/HP/Downloads/Python_Classes/old_files/old_file3.txt"]
new_files_names = ["C:/Users/HP/Downloads/Python_Classes/old_files/new_file1.txt","C:/Users/HP/Downloads/Python_Classes/old_files/new_file2.txt","C:/Users/HP/Downloads/Python_Classes/old_files/new_file3.txt"]
test_files_names = ["C:/Users/HP/Downloads/Python_Classes/test_files/new_file1.txt","C:/Users/HP/Downloads/Python_Classes/test_files/new_file2.txt","C:/Users/HP/Downloads/Python_Classes/test_files/new_file3.txt"]

for i in range(len(old_files_names)) :
    os.rename(new_files_names[i],test_files_names[i])