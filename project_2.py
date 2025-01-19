def add_time(start, duration, day=''):

    if duration =='0:00':
        return start
    days_list_lower = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    days_list = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    print ('Starting time : ', start)

    # separate the input start time to hours, minutes and indicator
    time_part, indicator = start.split()
    hours, minutes = map(int, time_part.split(':'))
    if indicator == 'PM' :
        hours += 12 
        idicator = 'AM'

    print ('Additional time : ', duration)
    # separate the additional time to additional hours and minutes
    additional_hours, additional_minutes = map(int, duration.split(':'))

    # calculate the resulting time 
    resulting_hours = hours + additional_hours
    resulting_minutes = minutes + additional_minutes

    print ('Resulting time : ', str(resulting_hours)+':'+str(resulting_minutes))

    # check if minutes overlap 60 
    extra_hours =  resulting_minutes // 60
    if extra_hours :
        resulting_hours += extra_hours
        resulting_minutes = resulting_minutes % 60
        if len(str(resulting_minutes))==1:
            resulting_minutes = '0'+str(resulting_minutes)
    

    
    day_incrementation = resulting_hours // 24
    while resulting_hours > 24 :
        resulting_hours -=24
    
    if resulting_hours >=12 and resulting_hours!=24 :
        resulting_hours -= 12
        new_indicator = 'PM'
        if resulting_hours == 0:
            resulting_hours = 12
    elif resulting_hours >12 and resulting_hours==24 :
        resulting_hours -= 12
        new_indicator = 'AM'
    else :
        new_indicator = 'AM'
    
    result = str(resulting_hours)+':'+str(resulting_minutes)+' '+ new_indicator

    if day.lower() in days_list_lower:
        index = days_list_lower.index(day.lower())
        new_index = (index + day_incrementation)%7
        new_day = days_list[new_index]
        result = result +', '+new_day

    if day_incrementation ==1 :
        result = result + ' (next day)'
    elif day_incrementation >1 :
        result = result + ' (' + str(day_incrementation) + ' days later)'

    print('Current result : ', result)
    print ('__________')
    return (result)


add_time("11:59 AM", "0:01")
add_time('3:00 PM', '3:10')
# Returns: 6:10 PM

add_time('11:30 AM', '2:32', 'Monday')
# Returns: 2:02 PM, Monday

add_time('11:43 AM', '00:20')
# Returns: 12:03 PM

add_time('10:10 PM', '3:30')
# Returns: 1:40 AM (next day)

add_time('11:43 PM', '24:20', 'tueSday')
# Returns: 12:03 AM, Thursday (2 days later)

add_time('6:30 PM', '205:12')
# Returns: 7:42 AM (9 days later)
