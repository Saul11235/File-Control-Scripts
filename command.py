# file  command - ESaul1135

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



def command(path):

    get_arguments_filepush()
    print("hello command")
    print(path)



#--------------------

if __name__=="__main__":

    def  write_filecommand():
        f=open(".filecommand","w")
        f.write("# filecommand  -  by Edwin Saul - @ESaul1135\n")
        f.write("# '# '  for comment\n")
        f.write("# '## ' for set command -  command terminal\n")
        f.write("# write bellow code file")
        f.close()

    if isfile(".filecommand"): command(str(getcwd()))
    else: write_filecommand(); print(".filecommand created!")

