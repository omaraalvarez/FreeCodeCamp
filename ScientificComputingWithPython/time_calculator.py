def hours_minutes(start, duration):

  start_t, start_dt = start.split(' ')[0], start.split(' ')[1]
  start_h, start_m = int(start_t.split(':')[0]), int(start_t.split(':')[1])

  duration_h, duration_m = int(duration.split(':')[0]), int(
      duration.split(':')[1])

  carry_hours, minutes = divmod(start_m + duration_m, 60)
  carry_days, hours = divmod(start_h + duration_h + carry_hours, 24)

  if hours == 0:

    hours = 12

  return hours, minutes, carry_days, carry_hours, start_dt


def dt_switch(hours, carry_hours, carry_days, start_dt):

  switch = (hours + carry_hours) // 12

  if switch % 2 == 1:

    if start_dt == 'AM':

      return 'PM', carry_days

    else:

      carry_days += 1

      return 'AM', carry_days

  else:

    return start_dt, carry_days


def days_elapsed(carry_days, day):

  days = [
      'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
      'Sunday'
  ]

  if day is not None:

    day_ind = days.index(day)

    day_ind += carry_days

    day_ind %= 7

    day = days[day_ind]

    return day


def time_format(hours, minutes, dt, carry_days, day):

  if hours > 12:

    hours = str(hours - 12)

  else:

    hours = str(hours)

  if minutes < 10:

    minutes = '0' + str(minutes)

  else:

    minutes = str(minutes)

  time = hours + ':' + minutes + ' ' + dt

  if day is not None:

    time += f', {day}'

  if carry_days == 1:

    time += ' (next day)'

  elif carry_days > 1:

    time += f' ({str(carry_days)} days later)'

  return time


def add_time(start, duration, day=None):

  if day is not None:

    day = day.capitalize()

  hours, minutes, carry_days, carry_hours, start_dt = hours_minutes(
      start, duration)

  dt, carry_days = dt_switch(hours, carry_hours, carry_days, start_dt)

  day = days_elapsed(carry_days, day)

  time = time_format(hours, minutes, dt, carry_days, day)

  return time
