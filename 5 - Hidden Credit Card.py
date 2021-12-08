import math
import re

def HiddenCreditCard(CardNumber):

   lastdigits = 4

   c1 = len(re.sub("[^0-9]", "", CardNumber)) - lastdigits

   # re.sub(sub-string to replace, sub-string to replace with , string) is a command that substitutes specific characters from a string

   print("Hidden credit card number: " + re.sub('\d', '*', CardNumber, c1))

   print(re.sub('\d', '*', CardNumber, c1))

CardNumber = str(input("Enter credit card number:"))

HiddenCreditCard(CardNumber)


