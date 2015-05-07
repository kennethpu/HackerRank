# Lists to map hour and minute digits to text
HOURS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']
MINUTES = ['one minute', \
          'two minutes', \
          'three minutes', \
          'four minutes', \
          'five minutes', \
          'six minutes', \
          'seven minutes', \
          'eight minutes', \
          'nine minutes', \
          'ten minutes', \
          'eleven minutes', \
          'twelve minutes', \
          'thirteen minutes', \
          'fourteen minutes', \
          'quarter', \
          'sixteen minutes', \
          'seventeen minutes', \
          'eighteen minutes', \
          'nineteen minutes', \
          'twenty minutes', \
          'twenty one minutes', \
          'twenty two minutes', \
          'twenty three minutes', \
          'twenty four minutes', \
          'twenty five minutes', \
          'twenty six minutes', \
          'twenty seven minutes', \
          'twenty eight minutes', \
          'twenty nine minutes']

# ENTRY POINT
H = int(raw_input())
M = int(raw_input())

# Different output formats depending on the value of M
if M == 0:
    print HOURS[H-1] + " o' clock" # special case for H:00
elif M == 30:
    print 'half past ' + HOURS[H-1] # special case for H:30
elif M < 30:
    print MINUTES[M-1] + ' past ' + HOURS[H-1] # M minutes past current hour
else:
    print MINUTES[(60-M)-1] + ' to ' + HOURS[H%12] # 60-M minutes to next hour, mod used to handle wrap around (12->1)