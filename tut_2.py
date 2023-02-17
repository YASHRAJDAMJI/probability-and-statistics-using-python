'''
Name:- Yashrah Damji
Roll:- 221071
quatuion :- A pair of fair dice is tossed. Find the probability of getting
(a) a total of 8;
(b) at most a total of 5
'''
#total dice
dice = []
n=1
j=0
count=1
while j<6:
    for i in range(1,7):
        l = []
        l.append(i)
        l.append(n)
        dice.append(l)
        if count==6:
            n=6
        elif n==6:
            n=0
    count=count+1
    n = n + 1
    j=j+1

#Function to find sum is num
count = 0
def sum(num):
    global count
    i=0
    while i<36:
        if (dice[i][0] + dice[i][1]) == num:
            #print(dice[i])
            count=count+1
        i=i+1
sum(8)
print("Count of 8 : ",count)
print("Probability of A TOTAL OF 8 : ",count/len(dice))

#Function to find sum is at most num
count=0
def at_most_sum(num):
    global count
    i=0
    while i<36:
        if (dice[i][0] + dice[i][1]) <= num:
            #print(dice[i])
            count=count+1
        i=i+1
at_most_sum(5)
print("\nCount of AT MOST 5 : ",count)
print("Probability of AT MOST OF 5 : ",count/len(dice))


