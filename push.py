# file  push - ESaul1135

from os import getcwd
from os.path import isfile,isdir
from platform import system  as platsys

slash="/"
if platsys()=="Windows":slash="\\"

class filepush_data:

    def __init__(self,location_path):
        self.data=[]
        try:
            file=open(location_path+slash+".filepush","r")
            self.data=file.read().split("\n")
            file.close()
        except:
            print("error reading .filepush")
            print("error on path: "+location_path)
        self.arguments_data=[]
        self.sorting_data()

    def sorting_data(self):

        
        
        pass


class arguments_push:

    def __init__(self,destination_path):
        a=filepush_data(getcwd())
        self.destination_path=destination_path

def get_arguments_filepush():
    arguments=[]
    a=arguments_push(getcwd())
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
        f.write("# write bellow extensions, file names")
        f.write("# or folder names to push")
        f.close()

    if isfile(".filepush"): push(str(getcwd()))
    else: write_filepush(); print(".filepush created!")

