#
# path actions
#

from os.path import isdir, isfile
from os import listdir

try:
    from __slash import slash
except:
    from .__slash import slash


def list_subdirs(path):
    subdirs=[]
    for x in listdir(path):
        full_path=path+slash+x
        if isdir(full_path):
            subdirs.append(full_path)
    return subdirs


def list_special_subdirs(path,special_file):
    especial_subdirs=[]
    for x in list_subdirs(path):
        if is_special_path(x,special_file):
            especial_subdirs.append(x)
    return especial_subdirs    


def list_no_special_subdirs(path,special_file):
    normal_subdirs=[]
    for x in list_subdirs(path):
        if  not(is_special_path(x,special_file)):
            normal_subdirs.append(x)
    return normal_subdirs


def list_files(path):
    subfiles=[]
    for x in listdir(path):
        full_path=path+slash+x
        if isfile(full_path):
            if x==".filepush" or x==".filepull":
                pass
            else:
                subfiles.append(full_path)
    return subfiles


def is_special_path(path,special_file):
    path_file=path+slash+special_file
    if isfile(path_file):
        return True 
    else:
        return False


if __name__=="__main__":
    from os import getcwd
    #print(list_subdirs(".."))
    #print(list_special_subdirs("..",".filepush"))
    #print(list_no_special_subdirs("..",".filepush"))
    #print(list_files(".."))
    #print(is_special_path("..",".filepush"))


    pass

