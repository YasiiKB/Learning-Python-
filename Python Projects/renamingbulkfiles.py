import os

def rename():
    i = 0

    # get user's inputs
    path = str(input("Where are your files?")).lower().replace('\\','/')+'/'
    img = str(input("What do you want to name your files?"))
    filesort = str(input("What type of a file are they?(.jpg , .doc, .txt, .etc): "))

    # make a list of all the files in the path and rename them 
    for filename in os.listdir(path): 
        newname = img + str(i) + filesort
        my_source = path + filename
        my_dest = path + newname
        os.rename(my_source, my_dest)
        i += 1

    print('All Done!')

if __name__ == '__main__': 
    rename()