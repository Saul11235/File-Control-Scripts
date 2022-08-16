#
# file actions
#

from os     import remove
from shutil import copy


def delete_folder(folder):
    print("folder "+str(folder)+" eliminado")



def delete_file(filepath):
    try:
        remove(filepath)
        print("  deleted   : "+filepath)
    except:
        print("  ERROR del : "+filepath)



def copy_file(path_origin_file,destination):
    try:
        copy(path_origin_file,destination)
        print("  copy file : "+path_origin_file)
    except:
        print("  ERROR copy:"+path_origin_file)



