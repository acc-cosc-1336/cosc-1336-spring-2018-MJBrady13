#This program converts the seconds past midnight into hours, minutes and seconds

def main():    
  total_seconds = int(input('Enter number of seconds: '))    
  final_hours = get_hours_since_midnight(total_seconds)    
  final_minutes = get_minutes(total_seconds)    
  final_seconds = get_seconds(total_seconds)    
  print ('The formatted time is: ', final_hours, ':', final_minutes,           
         ':', final_seconds)
  
#Finds the number of hours
def get_hours_since_midnight(total_seconds):
  hours = total_seconds // 3600
  return hours

#Finds the number of minutes
def get_minutes(total_seconds):
  seconds_remaining = total_seconds % 3600
  minutes = seconds_remaining // 60
  return minutes

#Finds the number of seconds
def get_seconds(total_seconds):
  seconds_remaining = total_seconds % 3600
  seconds = seconds_remaining % 60
  return seconds

main()
