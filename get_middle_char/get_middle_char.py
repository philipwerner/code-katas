"""Kata: Get Middle Character - Find the middle character(s) from a word
#1 Best Practices Solution by hiasen & others

Side note, I completed this kata in JS and wanted to do it with python
for myself to see differences

def get_middle(s):
   return s[(len(s)-1)/2:len(s)/2+1]
"""

def get_middle(s):
    # your code here
    return s[(len(s)-1)/2:len(s)/2+1]
