import os
def fcount(path):
    #Counts the number of files in a directory
    count = 0
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            count += 1

    return count
path = r"C:\Users\User\Desktop\Git\test_git_lab" #Read files in folder
print (fcount(path))