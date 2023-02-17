'''
Name:- Yashrah Damji
Roll:- 221071
quatuion :- In a certain assembly plant, three machines, B1, B2, and B3, make 30%, 45%, and
25%, respectively, of the products. It is known from past experience that 2%, 3%,
and 2% of the products made by each machine, respectively, are defective. Now,
suppose that a finished product is randomly selected. What is the probability that
it is defective?
'''

b1=int(input("Assembly plant made by machine b1 "))
b2=int(input("Assembly plant made by machine b2 "))
b3=int(input("Assembly plant made by machine b3 "))
b1d=int(input("Assembly plant made Defective by machine b1 "))
b2d=int(input("Assembly plant made Defective by machine b2 "))
b3d=int(input("Assembly plant made Defective by machine b3 "))

defctb1=(b1/100)*(b1d/100)
defctb2=(b2/100)*(b2d/100)
defctb3=(b3/100)*(b2d/100)

print("The Finished prducts Devective Probability is ",defctb1+defctb2+defctb3)
