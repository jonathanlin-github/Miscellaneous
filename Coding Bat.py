def sleep_in(weekday, vacation):
  if weekday == False or vacation == True:
    return True
  return False

def monkey_trouble(a_smile, b_smile):
  if a_smile == b_smile:
    return True
  return False

def sum_double(a, b):
  if a == b:
    return (a+b)*2
  else:
    return a + b

def diff21(n):
  if n <= 21:
    return 21 -n
  out = n - 21
  return out * 2

def parrot_trouble(talking, hour):
  if talking == False:
    return False
  else:
    if hour < 7 or hour > 20:
      return True
  return False

def makes10(a, b):
  if a == 10 or b == 10:
    return True
  if a + b == 10:
    return True
  return False

def near_hundred(n):
  if abs(100-n) <= 10 or abs(200-n) <= 10:
    return True
  return False

def pos_neg(a, b, negative):
  if negative == True:
    if a < 0 and b < 0:
      return True
  if negative == False:
    if a < 0 and b >= 0:
      return True
    if a >= 0 and b < 0:
      return True
  return False

def not_string(str):
  if 'not' in str:
    if str.index('not') == 0:
      return str
  return 'not ' + str

def missing_char(str, n):
  front = str[0:n]
  back = str[n+1:len(str)]
  return front+back

def front_back(str):
  if len(str) == 1:
    return str
  front = str[0:1]
  back = str[len(str)-1:len(str)]
  return back + str[1:len(str)-1] + front

def front3(str):
  if len(str) < 3:
    return str + str + str
  front = str[0:3]
  return front + front + front
