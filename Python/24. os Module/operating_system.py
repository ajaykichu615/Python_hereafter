import os
print(os.getcwd())
print(os.listdir(r"E:\Lumiar\Python\20. Modules"))
#os.makedirs('new/new1', exist_ok=True)
# .os() methods
    # os.listdir() - to obtain file names in the current directory as a list.
    # os.mkdir() - to create a new directory in the current directory.
    # os.rmdir() - to remove a directory. Also, only removes if the directory is empty.
    # os.makedirs() - to create directories and subdirectories recursively. exist_true parameter acts as error handling.
    # os.getcwd() - get current working directory. Returns as string.
    # os.chdir() - change working directory.
    # os.rename() - rename a directory. Provide source directory name or path and new name or path.
    # os.remove() - to remove a file in cwd.
    # os.path.exists('file_name') - to check if a file exists in a directory. Provide file name or file path.










