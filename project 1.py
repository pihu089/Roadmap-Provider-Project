#roadmap provider project
print('Roadmap provide project')

status = input('enter 1-for fresher, 2-for experienced = ') #string 

if status == '1': #integer
    print('Hi! fresher pick any 1 option for roadmap')
    user = input('enter 1) web dev, 2)app dev, 3) DS/AI/ML=')
    if user == '1':
        print('Learn HTML,CSS, JS, Python, Django')

    elif user == '2':
        print('Learn Java +DSA + Build Projects') 

    elif user == '3':
        print('Learn Python, Maths, R')  

    else:
        print('In valid input')    

elif status =='2':
    print('Hi! experienced pick any 1 option for roadmap') 
    user = input('enter 1) DataAnalytics, 2)cloud computing, 3) frontend=')
    if user == '1':  
        print('Learn Python,Excel PowerBI')  
    
    elif user =='2':
        print('Learn DevOps and Python for Automation')  

    elif user =='3':
        print('Learn Python and Django for Backend') 

    else:
        print('In valid input')

else:
    print('In valid input')     


