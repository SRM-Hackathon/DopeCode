import pandas as pd
data = pd.DataFrame()
data = pd.read_csv("/home/pavan/Downloads/SRM Hackathon (1)/final/traintestfinal.csv", low_memory = False)

####### STEP 1  FOR TICKET GENERATION(OVERALL PROGRAM)  #####

start = str(input("enter the start station name\n"))
start = start.upper()
drop = str(input("enter the drop station name\n"))
drop = drop.upper()
for i in range(0,data.shape[0]):
    if data.iloc[i,7] == start and data.iloc[i,9] == drop:
            break
        
####### STEP 2 FOR DAY GENERATION ##########
import datetime
x=int(input("enter the date of journey"))
y=int(input("enter the month of journey"))
z=int(input("enter the year of journey"))
mydate = datetime.date(z,y,x)  #year, month, day
t=mydate.strftime("%A")

########### STEP 3 FOR ACCESSING THE DAY COLUMN IN THE FILE FOR CHECKING THE AVAILABILITY OF THE TRAIN ON THAT DAY    ###########
days = {
      "Monday": 1,
     "Tuesday": 2,
     "Wednesday": 3,
      "Thursday": 4,
       "Friday": 5,
      "Saturday": 6,
       "sunday": 7
       }
s=days[t]

############ STEP 4   (INCOMPLETE) TO CHECK THE S VALUE IN THE DATA FILE FOR AVAILABILITY OF THE TRAIN ON THE DATE USER SPECIFIED (INCOMPLETE) ##########
print("\n\n\n\n#########YOUR TICKET###########\n\n\n\n")
o=str(data.iloc[i,10])
test = 0
for l in o.split():
    print(data.iloc[i,:])
    test = 1
if test == 0:
    print("There is no transport available")