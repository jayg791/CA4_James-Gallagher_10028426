# -*- coding: utf-8 -*-
"""
Created on Thu May 04 20:19:36 2017

@author: EliteBook
"""

# code to open the file and read in lower case
fhandle = open('Github Data.txt', 'r')
data = fhandle.readlines()

# a variable to handle text separator 
sep = 72*'-'

class Commit(object):
    #class for commit
    
    def __init__(self, revision = None, author = None, date = None, line_count = None, changes = None, comment = None):
        
        self.revision = revision
        self.author = author
        self.date = date
        self.line_count = line_count
        self.changes = changes
        self.comment = comment
    

commits = []
current_commit = None
index = 0

    
# parse each of the list and create a list
        
current_commit = Commit()
            
commits.append(current_commit)
            
details = data[index + 1].split('|')
#index = data.index(sep, index + 1)
 
      
current_commit.revision = details[0].strip()
current_commit.author = details[1].strip()
current_commit.date = details[2].strip()
current_commit.comment_line_count = int(details[3].strip().split(' ')[0]) 
current_commit.changes = data[index + 2:' ']
print current_commit.changes 

current_commit.comment = data[index(0): sep(-1)]



index = data.index(sep, index + 1)
print current_commit.comment_line_count
            
commits.append(current_commit)
''' 
        

    
#print len(commits)
#print commits[0].author
'''