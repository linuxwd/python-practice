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

def main():
    pass

if __name__ == '__main__':
    main()
import nester
print(dir(nester))
print(nester.__file__)
cast=['Palin','Cleese','idle','Jones','Gilliam','Chapman']
nester.print_lol(cast)
print("####################################################")
from nester import print_lol
##print(dir(nester))
##print(nester.__file__)
cast=['Palin','Cleese','idle','Jones','Gilliam','Chapman']
print_lol(cast)
print("####################################################")
from nester import *
##print(dir(nester))
##print(nester.__file__)
cast=['Palin','Cleese','idle','Jones','Gilliam','Chapman']
print_lol(cast)
print("####################################################")



for num in range(4):
    print(num)

def print_lol(the_list,level):
    for each_item in the_list:
        if isinstance(each_item,list):
           print_lol(each_item)
        else:
            for tab_stop in range(level):
                print("\t",end="")
            print(each_item)
print_lol(cast,0)