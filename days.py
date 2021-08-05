from datetime import date
from datetime import time
from datetime import datetime

def main():
  today = date.today()  
  afd = date(today.year, 4, 1)  
  if afd < today:
    print ("April Fool's day already went by %d days ago" % ((today-afd).days))
    afd = afd.replace(year=today.year + 1) 
    
    time_to_afd = afd - today
    print ("It's just", time_to_afd.days, "days until next April Fools' Day!")


if __name__ == "__main__":
  main()