'''
Name:- Yashrah Damji
Roll:- 221071
quatuion :- A class in advanced physics is composed of 10 juniors, 30 seniors, and 10 graduate
students. The final grades show that 3 of the juniors, 10 of the seniors, and 5 of the
graduate students received an A for the course. If a student is chosen at random from
this class and is found to have earned an A, what is the probability that he or she is a
senior?

'''
jun=int(input("Enter number of juniors"))
sen=int(input("Enter number of Seniors"))
grad=int(input("Enter number of graduate"))
fjun=int(input("Enter number of Juniors how got A grade"))
fsen=int(input("Enter number of Seniors how got A grade"))
fgrad=int(input("Enter number of Graduate how got A grade"))

total=fjun+fsen+fgrad
srudtotal=jun+sen+grad

prob=total/srudtotal

pro=fsen/srudtotal

finalprobab=pro/prob

print("the probability of selected A garded Senear is ",finalprobab)