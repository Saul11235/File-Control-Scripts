
try: 
    from class_special_file_content import special_file_content
except:
    from .class_special_file_content import special_file_content



class special_file:

    def __init__(self):
        self.special_file_content=special_file_content()
        


    def __scan(self):
        pass

#test
if __name__=="__main__":
    print("test")
    a=special_file()
    print("test ok")
