
# TONE1 = ['\uF068', '\uF071', '\uF054']
# TONE1 = []
# TONE2 = ['\uF068', '\uF057']
# TONE3 = ['\uF068', '\uF064']
# TONE8 = ['\uF068', '\uF048', '\uF072']

BYZSCALE = ["Ni","Pa","Vou","Ga","Dhi","Ke","Zo"]

TONE1SCALED = ['C', 'D', 'E', 'F', 'G', 'A', 'B-']
TONE2SCALED = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
TONE2SCALEG = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
TONE3SCALEF = ['C', 'D', 'E', 'F', 'G', 'A', 'B-']
TONE4SCALEE = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
TONE5SCALED = ['C', 'D', 'E', 'F', 'G', 'A', 'B-']
TONE5SCALEKE = ['C', 'D', 'E', 'F', 'G', 'A', 'B-']
TONE6SCALEG = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
TONE7SCALEF = ['C', 'D', 'E', 'F', 'G', 'A', 'B-']
TONE8SCALEC = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
TONE8SCALEF = ['C', 'D', 'E', 'F', 'G', 'A', 'B-']

OLIGON = ['U',1,'',1]
KENTEMATA = ['U',1,'U',1]
APOSTROPHOS = ['D',1,'',1]
ELAPHRON = ['D',2,'',1]
CELAPHRON = ['D',1,'',0.5]

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
      # print("tone chars: " + raw_chars[index:index+6])
      # Ensure the slice does not go out of bounds
      return raw_chars[index:index+6]
   else:
      return []

def get_tone(tone_marks):
   tone = 0
   start_pitch = "C4"

   if '\uF064' in tone_marks:
      tone = 3
      start_pitch = "F4"
      return [start_pitch, tone]
   elif '\uf048' in tone_marks and '\uf056' in tone_marks:
      tone = 5
      start_pitch = "D4"
      return [start_pitch, tone]
   elif '\uf048' in tone_marks and '\uf071' in tone_marks: # and '\uf03C' in tone_marks and '
      tone = 5
      start_pitch = "A5"
      return [start_pitch, tone]
   elif '\uf048' in tone_marks and '\uf072' in tone_marks:
      tone = 8
      start_pitch = "C4"
      return [start_pitch, tone]
   elif '\uf054' in tone_marks and '\uf056' in tone_marks:
      tone = 1
      start_pitch = "D4"
      return [start_pitch, tone]
   elif '\uf057' in tone_marks:
      if '\uf04d' in tone_marks:
         tone = 2
         start_pitch = "G4"
         return [start_pitch, tone]
   elif '\uf054' in tone_marks:
      if '\uf04d' in tone_marks:
         tone = 4
         start_pitch = "G4"
         return [start_pitch, tone]
   else:
      print(tone_marks)
      return []


   
def safe_cast(val, to_type, default=None):
   try:
      return to_type(val)
   except (ValueError, TypeError):
      return default