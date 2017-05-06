# -*- coding: utf-8 -*-
"""
Created on Fri May 05 16:57:05 2017

@author: EliteBook
"""

# Github_Commit Changes_Script.py

# code to open the file, read the lines and strip the spaces
fhandle = open('Github Data.txt', 'r')
data = [line.strip() for line in open('Github Data.txt', 'r')]

# a variable to handle the txt separater
sep = 72*'-'

#create a 'Commit Class' that will hold all of elements of interest in the data
class Commit(object):
    #class for commit
    
    def __init__(self, revision = None, author = None, date = None, line_count = None, changes = None, comment = None):
        
        self.revision = revision
        self.author = author
        self.date = date
        self.line_count = line_count
        self.changes = changes
        self.comment = comment
        
    def get_commit_day(self):
        day = self.date.split()
        return day[3].strip('(').strip(',')
        
        
    
    def get_author_names(self):
        return self.author
    
        
    
commits = []
current_commit = None
index = 0
authors = []

# start a loop to parse the information and retrurn it to the class
while True:
    try:
        current_commit = Commit()
        details = data[index + 1].split('|')
        current_commit.revision = int(details[0].strip().strip('r'))
        current_commit.author = details[1].strip()
        current_commit.date = details[2].strip()
        current_commit.comment_line_count = int(details[3].strip().split(' ')[0])
        current_commit.changes = data[index+2:data.index('',index+1)]
        index = data.index(sep, index + 1)
        current_commit.comment = data[index-current_commit.comment_line_count:index]
        commits.append(current_commit)
        
        author = data[index+1].split('|')[1].strip()
        if author not in authors:
            authors.append(author)
        
    except IndexError:
        break



print authors

for index, commit in enumerate(commits):
    print commit.get_commit_day() 






