#
# class path_obj
#
import __actions_path as ap

class path_obj:

    # for origin  location for .filepush 
    # for origin  location for .filepull
     
    def __init__(self,path,special_file):
        self.path=path
        self.special=special_file

    def special_subdirs(self):
        return ap.list_special_subdirs(self.path,self.special)

    def no_special_dirs(self):
        l=ap.list_no_special_subdirs(self.path,self.special)
        return l

    def all_folders(self):
        return ap.list_subdirs(self.path)

    def all_files(self):
        return ap.list_files(self.path)

    



        
