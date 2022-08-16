
try:
    from .__slash import slash
except:
    from __slash import slash


from platform import system

class special_file:

    def __init__(self,path,name_file):
        f=open(path+slash+name_file,"r")
        for x in f.readlines():
            print(x)
        pass


