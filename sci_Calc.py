def add_time(start, duration, day=None):
    # Parse start time
    start_time, period = start.split()
    period = period.upper()
    start_h, start_m = map(int, start_time.split(':'))
    
    # Convert start time to 24-hour format minutes
    if period == 'PM' and start_h != 12:
        start_h += 12
    elif period == 'AM' and start_h == 12:
        start_h = 0
    total_start_minutes = start_h * 60 + start_m
    
    # Parse duration
    dur_h, dur_m = map(int, duration.split(':'))
    total_dur_minutes = dur_h * 60 + dur_m
    
    # Calculate total minutes and days passed
    total_minutes = total_start_minutes + total_dur_minutes
    days_passed = total_minutes // 1440
    remaining_minutes = total_minutes % 1440
    
    # Convert remaining minutes to 12-hour format
    new_hh = remaining_minutes // 60
    new_mm = remaining_minutes % 60
    

# setting conditions..........

    if new_hh == 0:
        new_period = 'AM'
        new_h = 12
    elif 1 <= new_hh < 12:
        new_period = 'AM'
        new_h = new_hh
    elif new_hh == 12:
        new_period = 'PM'
        new_h = 12
    else:
        new_period = 'PM'
        new_h = new_hh - 12
    
    time_str = f"{new_h}:{new_mm:02d} {new_period}"

    # .......................................
    
    # Handle day of the week if provided
    day_str = ''
    if day:
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        original_day = day.lower().capitalize()
        original_index = days.index(original_day)
        new_index = (original_index + days_passed) % 7
        new_day = days[new_index]
        day_str = f", {new_day}"
    
    # Handle days later suffix
    days_later_str = ''
    if days_passed == 1:
        days_later_str = " (next day)"
    elif days_passed > 1:
        days_later_str = f" ({days_passed} days later)"
    
    new_time = time_str + day_str + days_later_str
    
    return new_time