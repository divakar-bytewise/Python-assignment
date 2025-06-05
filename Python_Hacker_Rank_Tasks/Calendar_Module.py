import calendar

def finding_day(m,d,y):
    w=calendar.weekday(y,m,d)
    
    if w==0:
        print("MONDAY")
    elif w==1:
        print("TUESDAY")
    elif w==2:
        print("WEDNESDAY")
    elif w==3:
        print("THURSDAY")
    elif w==4:
        print("FRIDAY")
    elif w==5:
        print("SATURDAY")
    else:
        print("SUNDAY")
    
if __name__=='__main__':
    m,d,y=map(int,input().split())
    r=finding_day(m,d,y)

