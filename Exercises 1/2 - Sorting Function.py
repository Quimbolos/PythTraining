import math
import array

from typing import List

def sorting(Order,List):
  if Order == str("asc"):

    List.sort(reverse=False)
    print(List)

  if Order == str("desc"):
    List.sort(reverse=True)
    print(List)

  if Order == str("none"):
    print(List)


Order = str(input("Enter your sorting preference: "))
List = [2,1,3,6,4,5,9,7,8]

#List = list(input("Enter list of numbers: ")) - does not work well 

sorting(Order,List)


