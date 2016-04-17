#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: omi
# @Date:   2016-04-17 14:23:23
# @Last Modified by:   omi
# @Last Modified time: 2016-04-17 14:26:32

import os 
def Start(rootDir, level=1): 
    if level==1: print rootDir 
    for lists in os.listdir(rootDir): 
        path = os.path.join(rootDir, lists) 
        if lists[len(lists)-1] is 's' and lists[len(lists)-2] is 'j' and lists[len(lists)-3] is '.':
            print '│  '+ path + ' --find'
            command = 'uglifyjs ' + path + ' -m -o ' + path
            os.system(command)
            pass
        if os.path.isdir(path): 
            Start(path, level+1) 


if __name__ == '__main__':
    Start("./")