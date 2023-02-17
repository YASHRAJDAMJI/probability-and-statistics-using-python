'''
Name:- Yashrah Damji
Roll:- 221071
quatuion :-
A volunteer is selected at random, meaning that each one has an equal
chance of being chosen. Find the probability that:
1. his specialty is medicine and he speaks two or more languages;
2. either his specialty is medicine or he speaks two or more
languages;
3. his specialty is something other than medicine.

'''

# total input
cs = int(input("Enter No. Volunteers whose Speciality is CONSTRUCTION and Speaks SINGLE Language : "))
ct = int(input("Enter No. Volunteers whose Speciality is CONSTRUCTION and Speaks TWO OR MORE Languages : "))

es = int(input("Enter No. Volunteers whose Speciality is EDUCATION and Speaks SINGLE Language : "))
et = int(input("Enter No. Volunteers whose Speciality is EDUCATION and Speaks TWO OR MORE Languages : "))

ms = int(input("Enter No. Volunteers whose Speciality is MEDICINE and Speaks SINGLE Language : "))
mt = int(input("Enter No. Volunteers whose Speciality is MEDICINE and Speaks TWO OR MORE Languages : "))

tot_vol = cs+ct+es+et+ms+mt

# 1st ans
print("Probability of Volunteers whose specility is MEDICINE and Speaks TWO OR MORE Languages : ",mt/tot_vol)

#2nd ans
m=ms+mt
pm=m/tot_vol
t=ct+et+mt
pt=t/tot_vol
dif=(m-t)/tot_vol
print("Probability of Volunteers whose specility is either MEDICINE or Speaks TWO OR MORE Languages : ",pm+pt-dif)

#3rd ans
pc = (cs+ct)/tot_vol
pe = (es+et)/tot_vol
print("Probability of Volunteers whose specility is other than MEDICINE : ",pc+pe)