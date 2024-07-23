
def seconds_since_midnight(hours, minutes, seconds):
	hour_in_seconds = 3600
	minute_in_seconds = 60
	total_seconds = hours * 3600 + minutes * 60 + seconds

	if  (0 <= hours < 24) or  (0 <= minutes < 60):
		return total_seconds
print(seconds_since_midnight(13, 30, 45))
	