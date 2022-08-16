#
# class path_obj
#

import __actions_path as ap

class path_obj:

    def __init__(self,path,special_file):
        self.path=path
        self.special=special_file


    def special_subdirs(self):
        return ap.list_special_subdirs(self.path,self.special)
        
