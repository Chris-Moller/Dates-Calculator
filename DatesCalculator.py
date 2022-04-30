class Date:

    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year

    def __repr__(self):

        s = "{:02d}/{:02d}/{:04d}".format(self.month, self.day, self.year)
        return s

    def isLeapYear(self):
        """Returns True if the calling object is
           in a leap year; False otherwise."""
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False
    
    def copy(self):
        """Returns a new object with the same month, day, year
           as the calling object (self).
        """
        dnew = Date(self.month, self.day, self.year)
        return dnew
    
    def equals(self, d2):
        """Decides if self and d2 represent the same calendar date,
           whether or not they are the in the same place in memory.
        """
        if self.year == d2.year and self.month == d2.month \
          and self.day == d2.day:
            return True
        else:
            return False

    def __eq__(self, d2):
        """Overrides the == operator so that it declares two of the same dates
            in history as ==."""
        if self.year == d2.year and self.month == d2.month \
          and self.day == d2.day:
            return True
        else:
            return False

    def isBefore(self, d2):
        if self.year < d2.year:
                return True
        elif self.year == d2.year and self.month < d2.month:
                return True
        elif self.year == d2.year and self.month == d2.month and self.day < d2.day:
                return True
        else:
            return False 
    
    def isAfter(self,d2):
        if self.year > d2.year:
            return True
        elif self.year == d2.year and self.month > d2.month:
            return True
        elif self.year == d2.year and self.month == d2.month and self.day > d2.day:
            return True
        else:
            return False 

    def tomorrow(self):
        fdays = 28 + self.isLeapYear()
        DIM = [0, 31, fdays, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        numOfDays = DIM[self.month] 
        if self.month == 12 and self.day == 31:
            self.year = self.year + 1
            self.month = 1
            self.day = 1
        elif numOfDays == self.day:
            self.month = self.month + 1
            self.day = 1
        else:
            self.day = self.day + 1
    def yesterday(self):
        fdays = 28 + self.isLeapYear()
        DIM = [0, 31, fdays, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        numOfDays = DIM[self.month-1] 
        if self.month == 1 and self.day == 1:
            self.year = self.year -1
            self.month = 12
            self.day = 31
        elif self.day == 1:
            self.month = self.month -1
            self.day = numOfDays
        else:
            self.day = self.day - 1

    def addNDays(self, N):
        if N < 0:
            print("Invalid input")
        for numberofdays in range(N):
            self.tomorrow()
            print(self)

    def subNDays(self, N):
        if N < 0:
            print("Invalid input")
        for numberofdays in range(N):
            self.yesterday()
            print(self)

    def diff(self, d2):
        self_copy = self.copy()
        d2_copy = d2.copy()
        counter = 0
        while self_copy.isBefore(d2_copy):
            counter = counter + 1
            self_copy.tomorrow()
        while self_copy.isAfter(d2_copy):
            counter = counter - 1
            self_copy.yesterday()
        while self_copy == d2_copy:
            return counter
    def dow(self):
        refdate = Date(10,10,2010)
        var1 = self.diff(refdate)
        daysAfterSunday = var1 % 7
        if daysAfterSunday == 6:
            dayOfWeek = 'Monday'
        if daysAfterSunday == 5:
            dayOfWeek = 'Tuesday'
        if daysAfterSunday == 4:
            dayOfWeek = 'Wednesday'
        if daysAfterSunday == 3:
            dayOfWeek = 'Thursday'
        if daysAfterSunday == 2:
            dayOfWeek = 'Friday'
        if daysAfterSunday == 1:
            dayOfWeek = 'Saturday'
        if daysAfterSunday == 0:
            dayOfWeek = 'Sunday'
        return dayOfWeek

def nycounter(year1,year2):

        dowd = {}
        dowd["Sunday"] = 0     
        dowd["Monday"] = 0     
        dowd["Tuesday"] = 0
        dowd["Wednesday"] = 0
        dowd["Thursday"] = 0
        dowd["Friday"] = 0
        dowd["Saturday"] = 0

        for year in range(year1, year2):
            d = Date(1, 1, year)
            print('Current date is', d)
            s = d.dow()     
            dowd[s] += 1

        print('totals are', dowd)

def bDayCounter(year1,year2,bday):

        dowd = {}
        dowd["Sunday"] = 0
        dowd["Monday"] = 0
        dowd["Tuesday"] = 0
        dowd["Wednesday"] = 0
        dowd["Thursday"] = 0
        dowd["Friday"] = 0
        dowd["Saturday"] = 0

        for year in range(year1, year2):
            m = int(bday[:2])
            d1 = int(bday[3:5])
            d = Date(m, d1, year)
            print('Current date is', d)
            s = d.dow()
            dowd[s] += 1

        print('totals are', dowd)


def main():
    print("Welcome to Dates Calculator!")
    print( "Type one of the following letters to select a feature" )
    print( "A: What will the date be in 'N' days?" )
    print( "B: What was the date 'N' days ago?" )
    print( "C: How many days between 'day_input_1' and 'day_input_2'?" )
    print( "D: What day of the week is 'day_input'?" )
    print( "E: What days of the week will New Years be between 'year_input_1' and 'year_input_2'? " )
    print( "F: What days of the week will your Birthday be between 'year_input_1' and 'year_input_2'? " )
    print( "G: Do nothing" )

    feature_letter = input()
    feature_letter = toUpper( feature_letter )
    if feature_letter == "A":
        a1 = input("Enter initial day (MM,DD,YYYY): ")
        m = int(a1[:2])
        d = int(a1[3:5])
        y = int(a1[6:])
        r1 = Date(m, d, y)
        a2 = input("Enter number of days to add: ")
        r1.addNDays(int(a2))
    elif feature_letter == "B":
        a1 = input("Enter initial day (MM,DD,YYYY): ")
        m = int(a1[:2])
        d = int(a1[3:5])
        y = int(a1[6:])
        r1 = Date(m, d, y)
        a2 = input("Enter number of days to subtract: ")
        r1.subNDays(int(a2))
    elif feature_letter == "C":
        a1 = input("Enter initial day (MM,D,YYYY): ")
        m = int(a1[:2])
        d = int(a1[3:5])
        y = int(a1[6:])
        r1 = Date(m, d, y)
        a2 = input("Enter second day (MM,D,YYYY): ")
        m2 = int(a2[:2])
        d2 = int(a2[3:5])
        y2 = int(a2[6:])
        r2 = Date(m2, d2, y2)
        print("There are",r1.diff(r2),"days between",r1,"and",r2)
    elif feature_letter == "D":
        a1 = input("Enter day (MM,DD,YYYY): ")
        m = int(a1[:2])
        d = int(a1[3:5])
        y = int(a1[6:])
        r1 = Date(m, d, y)
        print(r1,"is a",r1.dow())
    elif feature_letter == "E":
        a1 = input("Enter initial year (YYYY): ")
        a2 = input("Enter second year (YYYY): ")
        print(nycounter(int(a1),int(a2)))
    elif feature_letter == "F":
        a1 = input("Enter Birthday (MM,DD): ")
        a2 = input("Enter initial year or birth year (YYYY): ")
        a3 = input("Enter second year (YYYY): ")
        print(bDayCounter(int(a2),int(a3),a1))
    elif feature_letter == "G":
        print( "Have a nice day" )
    else:
        print( "Sorry, I don't understand: %s" % feature_letter )

def toUpper(s):
    return s.upper()

if __name__ == "__main__":
    main()