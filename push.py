# file  push - ESaul1135
from os import getcwd
from os.path import isfile,isdir
slash="/"



class filepush_data:

    def __init__(self,ubication_path):
        self.data=[]
        try:
            file=open(location_path+slash+".filepush","r")
            self.data=file.read()
            print(type(self.data))
            file.close()
        except:
            print("error reading .filepush")
            print("error on path: "+location_path)
            exit()


class arguments_push:

    def __init__(self,destination_path):
        a=filepush_data(getcwd())
        self.destination_path=destination_path

def get_arguments_filepush():
    arguments=[]
    file=open(".filepush","r")
    print(file.read())
    input(":::x")
    pass



def push(path):

    get_arguments_filepush()
    print("hello  ")
    print(path)



#--------------------

if __name__=="__main__":

    def  write_filepush():
        f=open(".filepush","w")
        f.write("# filepush -  by Edwin Saul - @ESaul1135\n")
        f.write("# '# '  for comment\n")
        f.write("# '## ' for set  destination path\n")
        f.write("# write bellow extensions, file names or folder names to push")
        f.close()

    if isfile(".filepush"): push(str(getcwd()))
    else: write_filepush(); print(".filepush created!")

