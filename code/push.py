
from os.path import isfile
from os import getcwd

try: 
    from class_directory_explorer import directory_explorer
except:
    from .class_directory_explorer import directory_explorer


def push(path):
    print("pathh push  "+str(path))


text_default="""
# filepush -  by Edwin Saul - @Saul11235
# use # for comment
# use ##  for set destination path
# write bellow extensions, file names or folder names to push

"""

if __name__=="__main__":
    if isfile(".filepush"):
        push((getcwd()))
    else: 
        f=open(".filepush","w")
        f.write(text_default)
        f.close()
        print(".filepush created!")

