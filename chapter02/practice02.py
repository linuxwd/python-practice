#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      Administrator
#
# Created:     06-01-2013
# Copyright:   (c) Administrator 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------


movies=["The Holy Grail",1975,"Terry Jones & Terry Gilliam",91,["Graham Chapman",["Michael Plain","John Cleese","Terry Gilliam","Eric Idle","Terry Jones"]]]



def print_lol(the_list,indent=False,level=0):
    for each_item in the_list:
        if isinstance(each_item,list):
           print_lol(each_item,indent,level+1)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t",end="")
            print(each_item)


print_lol(movies,indent=True,level=0)