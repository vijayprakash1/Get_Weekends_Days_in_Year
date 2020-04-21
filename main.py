import datetime as dt  # Get date time
import calendar
import numpy as np
#-------------------------------------------------------------------------------------------------------------------------------------------


YearList = {2017,2018,2019,2020}  # Enter the year you want to get weekends
file_name = "Weekend_List5.txt"
start_date = dt.date(2017,1,2)
end_date = dt.date(2020,12,31)
count = 0

#------------------------------------------------------------------------------------------------------------------------------------------

def get_weekends():  # function to get all the Saturday and Sunday in Years
   
    cldr = calendar.TextCalendar()
    global count
    for Year in YearList:

        for month in range(1, 13):
            for days in cldr.itermonthdays(Year, month):
                if days != 0:
                    day = dt.date(Year, month, days)
                    if day.weekday() == 6:
                        print("%s,%d-%d-%d" %(calendar.day_name[6], month, days, Year))
                        file1 = open(file_name, "a+")
                        file1.write("Sunday, ")
                        file1.write(day.strftime("%m/%d/%Y""\r\n"))
                        count += 1
                    elif day.weekday() == 5:
                        print("%s,%d-%d-%d" %(calendar.day_name[5], month, days, Year))
                        file1 = open(file_name, "a+")
                        file1.write("Saturday, ")
                        file1.write(day.strftime("%m/%d/%Y""\r\n"))
                        count += 1
    file1.close()
    print("Total Weekend Days", count)

#---------------------------------------------------------------------------------------------------------------------------------------------


def get_numberof_days():  # This function is used to get total number of days between 2 dates, it can include between two different yeasr

    print("Total Days", (end_date - start_date).days)


#----------------------------------------------------------------------------------------------------------------------------------------------

def get_working_days():   # This function is to get total working days between 2 dates it can be between years too

    dayss = np.busday_count(start_date, end_date)
    print("Total Week Days", dayss)

def main():
    get_weekends()
    get_numberof_days()
    get_working_days()
    




if __name__ == '__main__':
    main()
