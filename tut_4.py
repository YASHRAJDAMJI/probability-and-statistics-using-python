'''
Name:- Yashrah Damji
Roll:- 221071
quatuion :- One bag contains 4 white balls and 3 black balls, and a second bag contains 3 white
balls and 5 black balls. One ball is drawn from the first bag and placed unseen in
the second bag. What is the probability that a ball now drawn from the second
bag is black?

'''
bw1 = int(input("Enter Number of White Balls in Bag1 : "))
bb1 = int(input("Enter Number of Black Balls in Bag1 : "))
bw2 = int(input("Enter Number of White Balls in Bag2 : "))
bb2 = int(input("Enter Number of Black Balls in Bag2 : "))

tot_b1 = bw1 + bb1

tot_b2 = bw2 + bb2

prob_w1= bw1 / tot_b1
prob_b2 = bb2 / (tot_b2+1)
p1 = prob_b2 * prob_w1

prob_b1 = bb1 / tot_b1
prob_b2 = (bb2+1) / (tot_b2+1)
p2 = prob_b2 * prob_b1

print("Total Probability of Black Ball is : ",p1 + p2)
