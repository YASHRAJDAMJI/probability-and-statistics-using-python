'''
Name:- Yashrah Damji
Roll:- 221071
quatuion :- Suppose that we have a fuse box containing 20 fuses, of which 5 are defective. If
2 fuses are selected at random and removed from the box in succession without
replacing the first, what is the probability that both fuses are defective?
'''

box=int(input("enter number of fuses "))
dfuse=int(input("enter number Defective fuses "))
fuseselected=int(input("enter number of defective fuses selected "))
ans=[]

a=1

for i in range(0,fuseselected):
    ans.append(dfuse/box)
    box=box-1
    dfuse=dfuse-1
    

for i in ans:
    a=a*i

print(a)


