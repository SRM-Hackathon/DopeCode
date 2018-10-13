import pandas as pd
import json

file = 'C:\\Users\\DUWARKESH\\Downloads\\SRM Hackathon\\SRM Hackathon\\final\\FINALTRAINTEST.json'
file1 = ('C:\\Users\\DUWARKESH\\Downloads\\SRM Hackathon\\SRM Hackathon\\final\\FINALFLIGHTTEST.json')
with open(file) as train_file:
    dict_train = json.load(train_file)
# converting json dataset from dictionary to dataframe
train = pd.DataFrame.from_dict(dict_train, orient='columns')
train.reset_index(level=0, inplace=True)
with open(file1) as flight_file:
    dict_flight = json.load(flight_file)
flight = pd.DataFrame.from_dict(dict_flight, orient='columns')
flight.reset_index(level=0, inplace = True)

source_station = train['Source Station Name'].unique()
source_station1 = flight["LOCAL_AIRPORT"].unique()

trainstop1 = []
trainstop2 = []
flightstop1 = []
flightstop2 = []

source = str(input("Enter the start station name:\n ")).upper()
destination = str(input("Enter the drop station name :\n")).upper()

x = source
y = destination
s = []
for i in range(0,train.shape[0]):
    b = []
    if train.iloc[i,12] == source and train.iloc[i,7] == destination:
        print(train.iloc[i,1:])
        print('\n\n\n')
        b.append(train.iloc[i,:])
        s.append(b)
    else:
        if train.iloc[i,12] == source :
            for a in range(0,len(source_station)):
                if train.iloc[i,7] == source_station[a] : 
                    trainstop1.append(train.iloc[i,7])
        if train.iloc[i,7] == destination :
            for b in range(0,len(source_station)):
                if train.iloc[i,12] == source_station[b]:
                    trainstop2.append(train.iloc[i,12])

t = []
q = []
z = []
for j in range(0,len(trainstop1)):
    source = trainstop1[j]
    for k in range(0,len(trainstop2)):
        destination = trainstop2[k]
        for i in range(0,train.shape[0]):
            n = []
            if train.iloc[i,12] == source and train.iloc[i,7] == destination:
                print(train.iloc[i,1:])
                print('\n\n\n')
                n.append(train.iloc[i,:])
                t.append(n)
        start = destination
        for i in range(0,train.shape[0]):
            w = []
            if train.iloc[i,12] == start and train.iloc[i,7] == y:
                print(train.iloc[i,1:])
                print('\n\n\n')
                w.append(train.iloc[i,:])
                q.append(w)
    stop = source
    for i in range(0,train.shape[0]):
        v = []
        if train.iloc[i,12] == x and train.iloc[i,7] == stop:
            print(train.iloc[i,1:])
            print('\n\n\n')
            v.append(train.iloc[i,:])
            z.append(v)

g = []
for i in range(0,flight.shape[0]):
    b = []
    if flight.iloc[i,7] == source and  flight.iloc[i,10] == destination:
        print(flight.iloc[i,1:])
        print('\n\n\n')
        b.append(flight.iloc[i,:])
        g.append(b)
    else:
        if flight.iloc[i,7] == source :
            for c in range(0,len(source_station1)):
                if flight.iloc[i,10] == source_station1[c] : 
                    flightstop1.append(flight.iloc[i,10])
        if flight.iloc[i,10] == destination :
            for d in range(0,len(source_station1)):
                if flight.iloc[i,7] == source_station1[d]:
                    flightstop2.append(flight.iloc[i,7])
f = []
g = []
h = []
for q in range(0,len(flightstop1)):
    source = flightstop1[q]
    for r in range(0,len(flightstop2)):
        destination = flightstop2[r]
        for i in range(0,flight.shape[0]):
            m =[]
            if flight.iloc[i,7] == source and flight.iloc[i,10] == destination:
                print(flight.iloc[i,1:])
                print('\n\n\n')
                m.append(flight.iloc[i,:])
                f.append(m)
        start = destination
        for i in range(0,flight.shape[0]):
            w = []
            if flight.iloc[i,12] == start and flight.iloc[i,7] == y:
                print(flight.iloc[i,1:])
                print('\n\n\n')
                w.append(flight.iloc[i,:])
                g.append(w)
    stop = source
    for i in range(0,train.shape[0]):
        v = []
        if train.iloc[i,12] == x and train.iloc[i,7] == stop:
            print(train.iloc[i,1:])
            print('\n\n\n')
            v.append(train.iloc[i,:])
            h.append(v)