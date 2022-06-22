#Write a function called middle that takes a list and returns a new list that
#contains all but the first and last elements.
def middle(t):
    del t[0]
    del t[3]
i=0
t= list()
while i<5:
    sth = input ('Enter something: ')
    t.append (sth)
    i+=1
print('The original list had',len(t), 'elements')
print(middle(t))
newlenth = len(t)
print('The new List is',t,'\n''and it has',newlenth,'elements now')
