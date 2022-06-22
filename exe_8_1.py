#Write a function called chop that takes a list and modifies
#it, removing the first and last elements, and returns None.
def chop(t):
    del t[0]
    del t[3]
i=0
t= list()
while i<5:
    sth = input ('Enter something: ')
    t.append (sth)
    i+=1
#print('The original list had',len(t), 'elements')
print(chop(t))
#newlenth = len(t)
#print('The new List is',t,'\n''and it has',newlenth,'elements now')
#WITHOUT THESE PRINT THINGS, IT'LL ONLY PRINT "NONE"
