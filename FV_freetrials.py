import csv
import datetime

with open('Vinview-Free-Trial.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    next(spamreader)

    start_year = int(input("What is the starting year? "))
    start_month = int(input("What is the starting month? "))
    start_day = int(input("What is the starting day? "))
    
    start_date = datetime.datetime(start_year,start_month,start_day)
    today_date = datetime.datetime.now()
    #print(start_date)
    #print(today_date)

    main_list = []
    dealer_list = []

    for row in spamreader:
        #print(' '.join(row))
        new = (' '.join(row))
        split = new.split(",")

        dates = split[0]
        dates = dates[:10]
        year = int(dates[:4])
        month = int(dates[5:7])
        day = int(dates[8:])
        date = datetime.datetime(year,month,day)
        
        if start_date <= date <= today_date:
            new = split[6]
            new = new.replace('"','')
            new = new.replace('[','')
            new = new.replace(']','')
            main_list.append(new)
            #print(split[6])
            if new == "I work at a dealership":
                dealer = split[5]
                dealer = dealer.replace('"','')
                dealer_list.append(dealer)


    freq = {}
    for item in main_list:
        if (item in freq):
            freq[item] += 1
        else:
            freq[item] = 1
    
    print()
    print("Number of free trial requests" , len(main_list))
    print(freq) 
    print(dealer_list)

