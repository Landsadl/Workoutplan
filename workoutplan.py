import random 


#Defining Lists of Exercises in Plan
back=["rows", "Lat Pulldown", "Rear Delt Flyes","Face Pulls", "Deadlift", "Pull-Ups"]
chest= ["Barbell Bench Press", "Hammer Press", "Chest Flyes", "Incline Bench Press","Push ups","Decline Bench Press","Dips","Cable Crossover"]
biceps= ["Hammer Curls", "E-Z Bar Curls", "Cable Machine Curls", "Dumbbell Curls", "Preacher Curls", "Single Arm Cable Curls"]
shoulders=["Shoulder Press", "Dumbbell Lateral Raises", "Plate Front Raises", "Rear Delt Flyes", "Barbell Military Press", "Dead Hangs"]
triceps= ["French Press", "Pushdowns","Single-Arm Kick-Backs", "Dips", "Cable Overhead Press", "SkullCrushers"]
abs= ["Bicycle Crunches", "Crunches", "Russian Twists", "Leg Raises", "Hanging Knee Raises", "Cable Crunch", "Plank","Side Planks"]
legs=["Back Squats", "Calf Raises", "Leg Presses","Front Squats","Lunges", "Leg Curls", "Leg Extensions","Romanian Deadlifts"]


#Defining stings for number of sets
how_many_sets3="Do three sets of 10-12 reps (If (ABS) selected do three sets of 45 seconds)"
how_many_sets5="Do five sets of 5-8 reps (If (ABS) selected do five sets of 30 seconds)"


#Prompting User for input for what to workout
workoutday= str(input("What do you want to workout today (Back, Chest, Shoulder, Biceps, Abs, Legs)\t")).lower()    


#Ensuring the workout is in the available lists
while workoutday not in ["chest", "back", "biceps", "shoulders", "abs","legs","triceps"]:
    print("Not a Valid Option try again ")
    workoutday=str(input("what do you want to workout today? (Chest, Back, Biceps, Shoulders, Abs, Legs)\t")).lower()
    
#Prompting the number of exercises to randomize workout plan
how_many_exercises=int(input("how many workouts tonight? (No more then 6)\t"))

#Ensuring the number of exercises is valid
while how_many_exercises < 1 or how_many_exercises > 6:
        print("Invalid amount. Please enter a number between (1 and 6)")
        how_many_exercises=int(input("How many exercises tonight (1 through 6)\t"))

#Selecting exercises through random
if workoutday == "back":
    try:
        print(random.sample(back, k=how_many_exercises))
    except ValueError:
        print("There are not enough exercises in the list to choose that many. Please try again.\n")
    
elif workoutday == "biceps":
    try:
        print(random.sample(biceps, k=how_many_exercises))
    except ValueError:
        print("There are not enough exercises in the list to choose that many. Please try again.\n")
elif workoutday == "chest":
    try:
        print(random.sample(chest, k=how_many_exercises))
    except ValueError:
        print("There are not enough exercises in the list to choose that many. Please try again.\n")
elif workoutday == "shoulders":
    try:
        print(random.sample(shoulders,k=how_many_exercises))
    except ValueError:
        print("There are not enough exercises in the list to choose that many. Please try again. \n")
elif workoutday == "triceps":
    try:
        print(random.sample(triceps, k=how_many_exercises))
    except ValueError:
        print("There are not enough exercises in the list to choose that many. Please try again.\n")
elif workoutday == "abs":
    try:
        print(random.sample(abs, k=how_many_exercises))
    except ValueError:
        print("There are not enough exercises in the list to choose that many. Please try again.\n")
elif workoutday == "legs":
    try:
        print(random.sample(legs, k=how_many_exercises))
    except ValueError:
        print("There are not enough exercises in the list to choose that many. Please try again.\n")



#Getting the amount of sets from user
sets=int(input("How many sets? (3 or 5)\t"))

#Ensuring a valid amount of sets were input
while sets not in [3,5]:
    print("Invalid amount of sets try again.")
    sets=int(input("How many sets? (3 or 5)\t"))

#Displaying appropriate number of sets
if sets == 3:
    print(how_many_sets3)
else:
    print(how_many_sets5)
