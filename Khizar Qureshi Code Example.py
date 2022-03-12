#This program was a small assignment that was assigned by my Intro to Computer Science, 
#Professor David Liben-Nowell, to test us on data processing using for loops to calculate 
#different average situations and total situations in the stock market during the year 2021. 
#In this folder attached is the assignment, which is named 'Code example assignment.'
#In addition, the assignment PDF, I have also attached a datafile
# 'MMM.CSV' Which is used in this assignment. Please make sure you have the CSV file in the same directory
#Otherwise, this program won't function.


#open the file
file = open("MMM.csv", "r")



#declare useful variables and lists to count days and calculate average
dayCount = 0
highList = []
lowList = []
openList = []
closeList = []
prevDay = 0
openCount = 0
boringCount = 0
boringDayList = []
currentStreak = 0
maxStreak = 0

#split the fields & take out all $ signs
for line in file:
    fields = line.split(",")
    date, close, volume, open, high, low = fields[0], fields[1], fields[2], fields[3], fields[4], fields[5]
    closeReplace = close.replace("$", "")
    openReplace = open.replace("$", "")
    highReplace = high.replace("$", "")
    lowReplace = low.replace("$", "")
    #Splitting dates into months, days, and years
    dates = date.split("/")
    months = dates[0]
    days = dates[1]
    years = dates[2]
    #print number of days in 2021 where volume is greater than 5 mil 
    if int(volume) > 5000000 and int(years) == 2021:
            dayCount = dayCount + 1
    #Calculate average high, low, open, and close 
    if int(years) == 2021:
        highList.append(float(highReplace))
        sumHigh = sum(highList)
        averageHigh = sumHigh / 252

        lowList.append(float(lowReplace))
        sumLow = sum(lowList)
        averageLow = sumLow /252

        openList.append(float(openReplace))
        sumOpen = sum(openList)
        averageOpen = sumOpen / 252
        
        closeList.append(float(closeReplace))
        sumClose = sum(closeList)
        averageClose = sumClose / 252
        #calculate the number of days where highReplace was < 1.03*lowReplace and documenting the 
        # longest streak of boring days
        if float(highReplace) <= 1.03 * float(lowReplace):
            boringCount = boringCount + 1
            currentStreak = currentStreak + 1
        else: 
            currentStreak = 0
        if currentStreak > maxStreak:
            maxStreak = currentStreak

#Calculate the number of days where the opening price was at least 
# 1 dollar higher than the previous day's opening price 
for i in range(1, len(openList)):
    if openList[i] - openList[i-1] >= 1.00:
        openCount = openCount + 1

#print results
print("The total amount of days in 2021 where volume was greater than 5 million is", dayCount, "days.")
print("The average high price in 2021 was", averageHigh, "dollars.")
print("The average low price in 2021 was", averageLow,  "dollars.")
print("The average opening price in 2021 was", averageOpen, "dollars.")
print("The average closing price in 2021 was", averageClose, "dollars.")
print("In 2021, the number of days where the opening price was at least 1 dollar higher than the previous day's opening price was", openCount, "days.")
print("There where", boringCount, "boring days in 2021.")
print("The length of longest sequence of boring days in 2021 was",maxStreak, "days.")
