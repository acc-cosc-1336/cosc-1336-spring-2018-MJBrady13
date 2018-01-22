#This program converts the seconds past midnight into hours, minutes and seconds

#Finds the number of hours
def get_hours_since_midnight(total_seconds):
    hours = int(total_seconds // 3600)
    return hours

#Finds the number of minutes
def get_minutes(total_seconds): 
    seconds_remaining = int(total_seconds % 3600)
    minutes = int(seconds_remaining // 60)
    return minutes

#Finds the number of seconds
def get_seconds(total_seconds): 
    seconds_remaining = int(total_seconds % 3600)
    seconds = int(seconds_remaining % 60)
    return seconds

total_seconds = int(input('Enter number of seconds: '))
final_hours = int(get_hours_since_midnight(total_seconds))
final_minutes = int(get_minutes(total_seconds))
final_seconds = int(get_seconds(total_seconds))
print ('The formatted time is: ', final_hours, ':', final_minutes,
           ':', final_seconds)
