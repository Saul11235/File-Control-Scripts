
from os.path import isfile
from os import getcwd


try: 
    from class_directory_explorer import directory_explorer
except:
    from .class_directory_explorer import directory_explorer


def pull(path):
    print("pull on "+str(path))



text_default="""
# filepull -  by Edwin Saul - @Saul11235
# use # for comment
# use ##  for set destination path
# write bellow extensions, file names or folder names to pull

"""

if __name__=="__main__":

    if isfile(".filepull"):
        pull((getcwd()))
    else: 
        f=open(".filepull","w")
        f.write(text_default)
        f.close()
        print(".filepull created!")

