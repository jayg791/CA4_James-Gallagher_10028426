# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 18:36:27 2017

@author: EliteBook
"""
# code to open the file and read in lower case
fhandle = open('Github Data.txt', 'r')
data = fhandle.lower()
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
        
        
a_commit = Commit('r1551925', 'Thomas', '2015-11-27 16:57:44 +0000 (Fri, 27 Nov 2015)', None, 'Renamed folder to the correct name')

#print a_commit.revision
#print a_commit.author

commits = []
current_commit = None
index = 0

#SEARCH FOR SEPARATOR
#READ LINE FOR REVISION, AUTHOR, DATE, COMMENT, LINE COUNT 
# READ FILE CHANGES
# READ COMMENT
#GET NEXT COMMIT

while True:
    try:
    
        # parse each of the list and create a list
        
        current_commit = Commit()
            
        commits.append(current_commit)
            
        details = data[index + 1].split('|')
        print details
        current_commit.revision = details[0].strip()
        current_commit.author = details[1].strip()
        current_commit.date = details[2].strip()
        current_commit.comment_line_count = int(details[3].strip().split(' ')[1])
        current_commit.changes = data[index + 2:data.index('', index + 1)]
        current_commit.comment = data[index - current_commit.comment_line_count]
        index = data.index(sep, index + 1)
        #print current_commit.comment_line_count
            
        commits.append(current_commit)
        
        
    except IndexError:
        break
    
#print len(commits)
#print commits[0].author
