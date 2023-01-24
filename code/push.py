
from os.path import isfile
from os import getcwd


def push(path): #reads and evaluate
    print("path push  "+str(path))
    pass

def cicle_push():
    pass



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

