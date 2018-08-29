# tembo challenge
# all try blocks catch ValueError and SyntaxError
# printing 0 at any point leads to the main menu

# to print the details in intervals
import time
# given data
parents = {
    'Henry': {'childName': 'Calvin', 'age': 1},
    'Ada': {'childName': 'Lily', 'age': 4},
    'Emilia': {'childName': 'Petra', 'age': 2},
    'Biff': {'childName': 'Biff Jr', 'age': 3},
    'Milo': {}
}

activities = [
    {
        'age': 1,
        'activity': [
            'Go outside and feel surfaces.',
            'Try singing a song together.',
            'Point and name objects.'
            ]
    },
    {
        'age': 2,
        'activity': [
            'Draw with crayons.',
            'Play with soundmaking toys or instruments.',
            'Look at family pictures together.'
            ]
    },
    {
        'age': 3,
        'activity': [
            'Build with blocks.',
            'Try a simple puzzle.',
            'Read a story together.'
            ]
    }
]

# main method: starting of the program
def main():
    print('Hi user')
    makeChoice()

# method where the user makes his/her choice to either print data or add data
def makeChoice():
    print('\nPlease choose an option (Enter the number matching the option)\n1) Print Data\n2) Add Data\nTo Exit menu enter 0')
    try:
        user_choice = int(input('Choice: '))
        choice(user_choice)
    except ValueError:
        print('\nError: Not a number, please try again')
        makeChoice()
    except SyntaxError:
        print('\n Please enter a value')
        makeChoice()

# method that calls respective methods based on user's choice in main
def choice(user_choice):
    if (user_choice in [0,1,2]) == False :
        print('\nError: Wrong Choice! Please try again')
        makeChoice()
    elif(user_choice == 1):
        printActivities()
    elif(user_choice == 2):
        add()
    elif(user_choice == 0):
        print("Thanks! Bye!")

# If user chooses print: printActivities
def printActivities():
    for parent in parents: #For each parent
        age = parents[parent].get('age')
        print()
        print("Hi " + parent + "!")
        time.sleep(1) # All time statements print whateer follows after specified seconds
        if(age):
            check = True # to check if the loop completes
            for n_activities in range(0,len(activities)): # to go through each activity in an age group in activities
                if(activities[n_activities].get('age') and activities[n_activities].get('age')==age): # if age matches
                    print("Your child of age "+str(age)+" has " + str(len(activities[n_activities])+1) + " activities:")
                    printActivitiesFromList(activities[n_activities].get('activity'))# printing Activities
                    time.sleep(1)
                    print("Curriculum complete!")
                    check = False
            if (check): # if no activities are there for the age group
                print("Sorry! Your child of age " + str(age) + " doesn't have any activities.")
            time.sleep(2)
        else: # if no age is found (meaning child not present)
            time.sleep(1)
            print('Sorry! You do not have a child')
            time.sleep(2)
    makeChoice() # return to menu

# printing activities tabbed and in a new line
def printActivitiesFromList(activities_list):
    for a in range(0,len(activities_list)):
        to_print = "\t" + str(a+1) + ") "+ activities_list[a]
        time.sleep(1)
        print(to_print)

# If user chose add more activities
def add():
    print('\nPlease choose an option (Enter the number given alongside the option)\n1) Add Parent\n2) Add Activities\nEnter 0 to go to menu')
    try:
        user_add = int(input('Choice: '))
        add_choice(user_add)
    except ValueError:
        print('\nError: Not a number, please try again')
        add()
    except SyntaxError:
        print('\n Please enter a value')
        add()

# method that calls respective methods based on user's choice in add
def add_choice(user_add):
    if (user_add in [0,1,2]) == False :
        print('\nError: Wrong Choice! Please try again')
        add()
    elif(user_add == 1):
        addParent()
    elif(user_add == 2):
        addActivities()
    elif(user_add == 0):
        makeChoice()

# allows users to add a parent
def addParent():
    print('\nEnter 0 at any point to exit adding and return back to menu. Your data, however, would not be added.')
    try:
        key = str(input('Enter name of parent: '))
        if(key == '0'):
            return makeChoice()
        childName = str(input('Enter name of child: '))
        if(childName == '0'):
            return makeChoice()
        age = int(input('Enter age of child: '))
        if(age == 0):
            return makeChoice()
        addTo_Parent(key, childName, age)
    except ValueError:
        print('\nError:Age is not a number, please try again')
        addParent()
    except SyntaxError:
        print('\n Please enter a value')
        addParent()

# adding parent to the parent object
def addTo_Parent(key, childName, age):
    toAdd = {}
    toAdd['childName'] = childName
    toAdd['age'] = age
    parents[key] = toAdd
    addMore_Parent()

# method to check if user wants to add more parents
def addMore_Parent():
    choice = str(input('Add more? (yes/no). Enter 0 to return to menu: '))
    if(choice == '0'):
        makeChoice()
    elif(choice.lower() == 'yes'):
        addParent()
    elif(choice.lower() == 'no'):
        print('Thanks! Bye!')
    else:
        print('Wrong Input. Please try again.')
        addMore_Parent()

# allows user to add activities
def addActivities():
    print('\nEnter 0 at any point to exit adding and return back to menu. Your data, however, would not be added.')
    try:
        age = int(input('Enter age of child: '))
        if(age == 0):
            return makeChoice()
        for n_activities in range(0,len(activities)):
            if(activities[n_activities].get('age') and activities[n_activities].get('age')==age):
                print('Activities for that age have already been added.')
                return addMore_Activities()
        n_activities = int(input('Enter Number of Activities: '))
        if(n_activities == 0):
            return makeChoice()
        add_activity = []
        for a in range(0, n_activities):
            user_activity = str(input('Enter activity: '))
            add_activity.append(user_activity)
        addTo_Activities(age,add_activity)
    except ValueError:
        print('\nError: not a number, please try again')
        addParent()
    except SyntaxError:
        print('\n Please enter a value')
        addParent()

# adds activities to activities array
def addTo_Activities(age,add_activity):
    toAdd = {}
    toAdd['age'] = age
    toAdd['activity'] = add_activity
    activities.append(toAdd)
    addMore_Activities()

# method to check if the user wants to add more activities
def addMore_Activities():
    choice = str(input('Add more? (yes/no). Enter 0 to return to menu: '))
    if(choice == '0'):
        makeChoice()
    elif(choice.lower() == 'yes'):
        addActivities()
    elif(choice.lower() == 'no'):
        print('Thanks! Bye!')
    else:
        print('Wrong Input. Please try again.')
        addMore_Activities()

# script starts with this
if __name__ == '__main__':
    main()
