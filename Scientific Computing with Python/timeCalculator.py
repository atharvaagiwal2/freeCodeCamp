def add_time(start_time,duration,day=''):
    week_days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
    hr = int(start_time.split()[0].split(':')[0])
    min = int(start_time.split()[0].split(':')[1])
    AM_or_PM = start_time.split()[1]

    if AM_or_PM == 'PM':
        hr += 12

    dur_hr = int(duration.split(':')[0])
    dur_min = int(duration.split(':')[1])

    day_added = (hr+dur_hr + (min+dur_min)//60)//24
    hr_added = (hr+dur_hr)%24 + (min+dur_min)//60
    min_added = (min+dur_min)%60

    if hr_added/12 > 0:
        if AM_or_PM == 'PM' and hr_added>24:
            AM_or_PM = 'AM'
        else:
            AM_or_PM = 'PM'
        hr_added = hr_added%12
    else:
        hr_added = hr_added%12

    bracket_string = ''
    if day_added:
        if day_added==1:
            bracket_string = '(next day)'
        else:
            bracket_string = f'({day_added} days later)'
    if hr_added == 0:
        hr_added += 12
    if len(str(min_added))==1:
        min_added = '0'+str(min_added)
    day = day.capitalize()
    if day:
        day_idx = (week_days.index(day)+day_added)%7
        return ( f'{hr_added}:{min_added} {AM_or_PM}, {week_days[day_idx]} {bracket_string}')
    else:
        return (f'{hr_added}:{min_added} {AM_or_PM} {bracket_string}')
