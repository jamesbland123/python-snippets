""" Date time usage with time delta and string format """
import datetime

# UTC Now
current_time = datetime.datetime.utcnow()
print(current_time)

# time delta
future_time = datetime.timedelta(days=+3)
print(current_time + future_time)

# String to date object
date_string = "2019-01-02 12:16:02"
date_time_obj = datetime.datetime.strptime(date_string, '%Y-%m-%d %H:%M:%S')
print(date_time_obj)

# Format datetime object
print(date_time_obj.strftime('%B %d %A'))
