#importing modules
import functions

#Variable Declaration
score=[0,0,0,0,0]
index=0

#Dictionary is added into inside a list
players=[{"name":"Virat Kohli","role":"Bat","runs":112,"four":10,"six":0,"balls":119,"field":0},
   {"name":"Du Plessis","role":"Bat","runs":120,"four":11,"six":2,"balls":112,"field":0},
   {"name":"Bhuvneshwar Kumar","role":"Bowl","wkts":1,"overs":10,"runs":71,"field":1},
   {"name":"Yuzvendra Chahal","role":"Bowl","wkts":2,"overs":10,"runs":45,"field":0},
   {"name":"Kuldeep Yadav","role":"Bowl","wkts":3,"overs":10,"runs":34,"field":0}]

#Score Calculation and Printing of Score
for x in range(5):
    if players[x]["role"]=="Bat":
        score.insert(x,functions.batting(players[x]["runs"],players[x]["balls"],players[x]["four"],players[x]["six"]))
        print("Name:'{}', Batscore:'{}'".format(players[x]["name"], score[x]))
    else:
        score.insert(x,functions.bowling(players[x]["wkts"],players[x]["overs"],players[x]["runs"],players[x]["field"]))
        print("Name:'{}', Bowlscore:'{}'".format(players[x]["name"], score[x]))

#Finding the top players index
index=score.index(max(score))

#Displaying the Man of the Match
print()
print("The Man of the Match is {} with score {}.".format(players[index]["name"],score[index]))

