import os
import subprocess
import fnmatch
import fileinput
import re

f = fileinput.input(files='/home/psxas/.zsh_history')

def find_history():
     result = []
     for line in f:
         regex = fnmatch.translate('cd *')
         m = re.search(regex,line)
         if m != None:
             result.append(m.group(0))
     return result


#for file in os.listdir('.'):                                 │~                                                               
#    if fnmatch.fnmatch(file, '*'):                           │~                                                               
#        print(file)


def get_last():
    history  = find_history()
    last_pos = len(history)-1
    last_cd  = history[last_pos]
    last_cd  = last_cd[3:]
    return last_cd

if __name__ == "__main__":
     print(get_last())
