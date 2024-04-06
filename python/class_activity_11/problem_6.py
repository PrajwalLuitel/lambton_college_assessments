import random

# creating a class Time
class Time:
    # Initializing the class instance with hour, minute and second
    def __init__(self, hour=0, minute=0, second = 0):
        self.hour = hour
        self.minute = minute
        self.second = second

        if self.hour >=24 or self.minute >= 60 or self.second >= 60:
            raise Exception("Hour must be between 0 to 23 and minutes and seconds must be between 0 to 59")
    
    # A method to display the time
    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"


    # A method to add multiple time objects
    def __add__(self, time):
        # Adding the seconds first, so that if it is greater than 60, value can be added to minutes
        added_seconds = int(self.second) + int(time.second)
        # calculating if the seconds carry over to minutes
        to_minute = added_seconds//60
        # If yes, than adjusting the seconds
        if to_minute != 0:
            added_seconds = added_seconds%60
        # Checking if there is carry over in minutes and if yes, adding it over to the hours
        added_minutes = int(self.minute) + int(time.minute)
        to_hour = added_minutes//60
        if to_hour != 0:
            added_minutes = added_minutes%60
        
        # Verifying whether hour exceeds 24 hour format or not and limiting it
        added_hour = int(self.hour) + int(time.hour)
        added_hour = added_hour%24

        # returning the time object
        return Time(added_hour, added_minutes, added_seconds)
    
    # A method to subtract multiple time instances
    def __sub__(self,time):
        # Firstly, performing a plain subtraction of the hours, minutes and seconds
        subtracted_hours = self.hour - time.hour
        subtracted_minutes = self.minute - time.minute
        subtracted_seconds = self.second - time.second

        # If the subtraction results in negative values, adjusting accordingly
        if subtracted_hours < 0:
            subtracted_hours = 24 + subtracted_hours # hours cannot exceed 24
        if subtracted_minutes < 0:
            subtracted_minutes = 60 + subtracted_minutes # minutes cannot exceed 60, so subtracting an hour
            subtracted_hours -=1
        if subtracted_seconds < 0:
            subtracted_seconds = 60 + subtracted_seconds # seconds cannot exceed 60, so subtracting a minute
            subtracted_minutes -= 1
        
        # Returning the Time object
        return Time(subtracted_hours, subtracted_minutes, subtracted_seconds)



def main(h1, m1, s1, h2, m2, s2):
    # Taking 6 inputs as specified and checking them
    try:
        # Creating Time objects
        t1 = Time(h1, m1, s1)
        t2 = Time(h2,m2,s2)

    # Exception handling
    except Exception as e:
        print(f"Error: {e}")

    print(f"\nTime1 is {t1}")
    print(f"Time2 is {t2}")
    # Performing addition and subtraction to verify that they are correct
    print(f"Subtracting {t2} from {t1} we get: {t1-t2}")
    print(f"Adding {t2} to {t1}, we get: {t1 + t2}")



if __name__ == "__main__":
    def h():
        return random.choice(range(24))
    
    def m():
        return random.choice(range(60))
    
    def s():
        return random.choice(range(60))

    for i in range(10):
        print(f"\n\nTry {i+1}:")
        main(h(), m(), s(), h(), m(), s())  
