#!/bin/python3

import math
import os
import random
import re
import sys


nn=input()
n=int(nn)

if n/2 == 1:
    print("Weird")
elif (n/2==0 | 2<n<5) :
    print("Not weird ")
elif (n/2==0 | 6<n<20) :
    print("weird ")
elif (n/2==0 | 20<n) :
    print("Not weird ")
