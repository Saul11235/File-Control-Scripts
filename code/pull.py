
from os.path import isfile
from os import getcwd

try:
    from __function_pull import pull
except:
    from .__function_pull import pull


text_default="""# filepull -  by Edwin Saul - @Saul11235
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

