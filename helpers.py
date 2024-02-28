
TONE8 = ['\uF068', '\uF048', '\uF072', '\uF04E']

def is_sublist(test_list, sublist):
   res = False
   for idx in range(len(test_list) - len(sublist) + 1):
      if test_list[idx: idx + len(sublist)] == sublist:
         res = True
         break
   return res
