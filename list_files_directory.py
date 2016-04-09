import os

# Get all files in designated path
def get_files(path):
    filepath = os.listdir(path)
    files = []
    for fp in filepath:
        fppath = path + '/' + fp
        if(os.path.isfile(fppath)):
            files.append(fppath)
        elif(os.path.isdir(fppath)):
            files += get_files(fppath)
    return files

list1 = get_files(".")

for i in list1:
	print i
