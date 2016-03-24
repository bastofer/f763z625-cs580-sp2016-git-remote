#   Robin Jacobs  F763Z625
#   Program: pgm812.py
#   Description of program - This program calculates the number of heating/cooling degree-days in an observed time period of daily average temperatures.
#                            the program takes a .CSV file of daily average temperatures as its input to calculate the number of degree-days.
#
#   Psuedo Code
#   Algorthim readTemps
#       Read in a sequence of average daily temperatures from file 
#   Pre - None
#   Post - Returns a list of average daily temperatures
#
#   Ask user for location and name of a CSV file that contains the average daily temperatures.
#   Open this file (if found. If not, inform user that path/name is not valid and ask until
#   a vaild name and path are entered) and read the temperatures out of it and copy them into
#   a list. Return this list.
#
#   import re
#
#   filePath = ''
#   avgTemps = ''
#   fileFound = False
#
#   while(fileFound == False)
#       try:
#           filePath = get filepath and name of CSV file from user that contains average daily temperatures
#           tempFile = open(filePath,'r')
#           avgTemps = tempFile.readline()
#           avgTemps = avgTemps.split(',')
#           return avgTemps
#
#       except:
#           print("Error: specified file not found")
#
#   Algorthim degreeDays
#       Determine whether a daily average temperature is a heating or cooling degree-day
#       and if it is, determine if it is a heating degree-day or a cooling degree-day and
#       add it to a running total of heating/cooling degree-days.
#   Pre - A list of daily average temperatures for any number of days (avgTemps
#   Post - Returns number of cooling degree-days and heating degree-days for the
#          time period covered by the list of average daily temperatures
#
#   coolingDays, heatingDays = 0,0
#
#   for temp in avgTemps:
#       temp = float(temp)
#       if(temp < 60):
#           heatingDays++
#       elif(temp > 80):
#           coolingDays++
#   return coolingDays, heatingDays#      
#       
#   Algorthim main
#      Calls readTemps to get the average daily temperatures to process for finding number of degree-days.
#      Then, calls degreeDays to process the temperatures and determine how many cooling/heating degree-days
#      respectively are in the given set of daily average temperatures. Finally, prints the number of heating
#      and cooling degree-days returned by degreeDays.
#
#   Pre - None
#   Post - Prints number of heating degree-days and cooling degree-days for the given set of average daily temperatures
#
#   print-intro to program exaplaining what it does and how to use it
#
#   avgTemps = readTemps()
#   coolingingDays, heatingDays = degreeDays(avgTemps)
#
#   print("Number of heating degree-days: ", heatingDays)
#   print("Number of cooling degree-days: ", coolingDays)

import re

def readTemps():

    filePath = ""
    fileValid = False
    enterNewFile = ""

    print(filePath)

    while(fileValid == False):
        filePath = input("Enter location and name of the CSV file that holds the daily average\ntemperatures to be processed (Example: C:\\avgTemps.csv): ")
            
        if(re.search(".csv", filePath)):
            try:
                tempFile = open(filePath, 'r')
                fileValid = True

            except:
                print("\nERROR: No CSV file could not be found at the location " + "'" + filePath + "'" + ".\nPlease enter another file name and/or location.\n")
            
            if(fileValid == True):
                avgTemps = tempFile.readline()
                avgTemps = avgTemps.split(',')
                tempFile.close()
                fileValid = validData(avgTemps)

                if(fileValid == False):
                    while((enterNewFile != 'N') and (enterNewFile != 'n') and (enterNewFile != 'Y') and (enterNewFile != 'y')):
                        enterNewFile = input("Would you like to specify a different file? (Y= Yes N= No): ")

                        if((enterNewFile != 'N') and (enterNewFile != 'n') and (enterNewFile != 'Y') and (enterNewFile != 'y')):
                            print("\nThat is not a valid choice. Please enter either 'Y' to specify a new .CSV file or 'N' to exit the program.\n")
                    if(enterNewFile == 'N' or enterNewFile == 'n'):
                        return -1
        else:
            print("\nERROR: The file specified is not a .CSV file. Please enter the file path and name of a\nComma Seperated Values (.CSV) file.\n")

    return avgTemps

def validData(csvData):
    for temp in csvData:
        try:
            temp = float(temp)
        except:
            print("\nERROR: CSV file contains improperly formatted or non-temperature data. Please check\nspecified file's contents to ensure it contains only temperatures formatted\nas decimal numbers without any special characters.\n")
            return False

    return True

def degreeDays(avgTemps):

    coolingDays, heatingDays = 0, 0

    for temp in avgTemps:
        temp = float(temp)
        if(temp < 60.00):
            heatingDays = heatingDays + 1
        elif(temp > 80.00):
            coolingDays = coolingDays + 1
            
    return heatingDays, coolingDays
       
def main():
    
    print("=============================Degree-Days Calculator===================================\n")
    print("This program calculates the number of cooling degree-days (days where the temperature\nis greater than 80) and the number of heating degree-days (days where the temperature\nis less than 60) given a set of daily average temperatures. To begin, enter the\nfilepath and name of a Comma Seperate Value file (.CSV) that contains a set of daily\naverage temperatures for any number of days")
    print("\n======================================================================================")

    avgTemps = readTemps()

    if(avgTemps == -1):
        return
    
    coolingDays, heatingDays = degreeDays(avgTemps)
    enterNewFile = ""
    
    print("\nNumber of Heating Degree-Days in the observed time frame: ", heatingDays)
    print("Number of Cooling Degree-Days in the observed time frame: ", coolingDays)    

    return

main()
