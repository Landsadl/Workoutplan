import random 
import json



#Pulling Lists of Exercises From JSON file
with open("workouts.json") as f:
    workouts= json.load(f)
with open("sets.json") as s:
    how_many_sets= json.load(s)




#Prompting User for input for what to workout
workoutday=(input("What do you want to workout today (Back, Chest, Shoulder, Biceps, Abs, Legs)\t")).lower()    


#Ensuring the workout is in the available lists
while workoutday not in workouts:
    print("Not a Valid Option try again ")
    workoutday=(input("what do you want to workout today? (Chest, Back, Biceps, Shoulders, Abs, Legs)\t")).lower()
    
#Prompting the number of exercises to randomize workout plan
how_many_exercises=int(input("how many workouts tonight? (No more then 6)\t"))

#Ensuring the number of exercises is valid
while how_many_exercises <= 1 or how_many_exercises >= 6:
        print("Invalid amount. Please enter a number between (1 and 6)")
        how_many_exercises=int(input("How many exercises tonight (1 through 6)\t"))
        
try:
    selected_workout= random.sample(workouts[workoutday], k=how_many_exercises)
    
except:
    ValueError("There isn't enough exercises in the list to choose that many. Please try again. ")

#Getting the amount of sets from user
sets=int(input("How many sets? (3 or 5)\t"))

#Ensuring a valid amount of sets were input
while str(sets) not in how_many_sets:
    print("Invalid amount of sets try again.")
    sets=int(input("How many sets? (3 or 5)\t"))

#Displaying appropriate number of sets
print(selected_workout)
print(how_many_sets[str(sets)])
