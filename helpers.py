
TONE1 = ['\uF068', '\uF071', '\uF054']
TONE2 = ['\uF068', '\uF057']
TONE3 = ['\uF068', '\uF064']
TONE8 = ['\uF068', '\uF048', '\uF072']


OLIGON = ['U',1,'','']
KENTEMATA = ['U',1,'U','']
APOSTROPHOS = ['D',1,'','']
ELAPHRON = ['D',2,'','']

def is_sublist(test_list, sublist):
   res = False
   for idx in range(len(test_list) - len(sublist) + 1):
      if test_list[idx: idx + len(sublist)] == sublist:
         res = True
         break
   return res

def get_tone_marks(raw_chars):
   target_char = '\uF068'
   if target_char in raw_chars:
      index = raw_chars.index(target_char)
      # Ensure the slice does not go out of bounds
      return raw_chars[index:index+5]
   else:
      return []

def get_tone(raw_chars):
   tone = 0
   start_pitch = "C4"
   tone_marks = get_tone_marks(raw_chars)
   if '\uF064' in tone_marks:
      tone = 3
      start_pitch = "F4"
      return [start_pitch, tone]
   else:
      return []