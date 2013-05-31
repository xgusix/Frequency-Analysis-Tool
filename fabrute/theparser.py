#The Parser by xgusix
import string

#This function divides lines of a file based on a given divider symbol and stores them in a dictionary
def dividerDict(file,divider=','):
        dic={}
        fd=open(file)
        for line in fd:
                dic[line[:string.find(line,divider)]]=line[string.find(line,divider)+len(divider):-1]
        return dic


#This function divides lines of a file and stores them in two lists
def dividerLists(file,divider=','):
        list1=[]
        list2=[]
        fd=open(file)
        for line in fd:
                list1.append(line[:string.find(line,divider)])
                list2.append(line[string.find(line,divider)+len(divider):-1])
        return list1,list2
