from phue import Bridge
from phue import Light
import random

b = Bridge('192.168.86.22')
print(b.get_api())