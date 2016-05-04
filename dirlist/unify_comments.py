'''
Created on 2016. máj. 4.

@author: danie
'''

import sys, fnmatch, os, re, logging

if __name__ == '__main__':
    l = len(sys.argv)
    grep_pattern = sys.argv[1] if l > 1 else u'¤¤4ˇ˘5˘°2°ˇ3ˇ^2^ˇ4^˘5˘°3°^5^°°Đ]4˘˘' #default: No match only print filenames.
    doc_root = sys.argv[2] if l > 2 else '.'
    file_filter = sys.argv[3] if l > 3 else '*'
    
    
    dir_list = []
    
    for root, dirs, files in os.walk(doc_root):
        for name in files:
            dir_list.append(os.path.join(root, name))
        for name in dirs:
            dir_list.append(os.path.join(root, name))
            
    for f in fnmatch.filter(dir_list, file_filter):
        if not os.path.isdir(f):
            print(f[41:]) #TODO remove [41:]
            
            with open( f ,'r+', encoding="utf8") as finout:
                try:
                    lines = finout.readlines()
                    finout.seek(0)
                    finout.truncate()
                    for line in lines:
                        if re.search(grep_pattern, line):
                            print(line)
                            line = re.sub("!--", "% *" , line)
                            line = re.sub("% \* % \*", "% *" , line)
                            print(line)
                        finout.write(line)
                except:
                    logging.exception("message" + "\nFile: " + f)
    