#
# list - actions
#


def intersection(list1,list2):
    response=[] 
    for x in list1:
        try: list2.index(x);response.append(x)
        except:pass
    return response


def diference(list1,list2):
    response=[]
    for x in list1:
        try: list2.index(x)
        except: response.append(x)
    return response



if __name__=="__main__":
    # test
    l1=[1,2,3,4,5,6,10]
    l2=[2,3,1000,5,4]
    print(intersection(l1,l2))
    print(diference(l1,l2))

