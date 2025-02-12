# YOU ONLY HAVE TO SUBMIT FUNCTIONS FOR WHICH
# YOU ARE THE DRIVER IN PAIR PROGRAMMING


# Here are some history variables to test your code on. Feel free to create your own.
hist1 = []
hist2 = [("split","steal")]
hist3 = [("split","split"),("steal","split"),("split","steal"),("split","split"),("steal","split")]
hist4 = [("split","steal"),("steal","steal"),("split","steal"),("steal","split"),("split","split"),("steal","split")]

# Your team's 1st strategy (leave blank if you are not the driver)
# Explanation of Strategy:
# 


# Your team's 2nd strategy (leave blank if you are not the driver)
# Explanation of Strategy:
# 


# Your team's 3rd strategy (leave blank if you are not the driver)
# Explanation of Strategy:
#There will be a half chance of split at the start but every time the opponent steals, the percent chance of us stealing gets higher but if they split we get more likely to split as well

import random

def MarathonMavericks3(history):
    stealchance=50
    for i in history:
        if i[0]=="steal":
            stealchance+=5
        elif i[0]=="split":
            stealchance-=5
    choice=random.randint(1,100)
    if choice>=stealchance:
        return "split"
    else:
        return "steal"
    
print(MarathonMavericks3(hist2))
    
#Excuse the program if it doesnt work. Look at zia's code and mine will be there too just in case. We were having some technical difficulties so this was our solution! ty for bearing with us
