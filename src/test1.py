from enum import Enum

class Shake(Enum):
    vanilla = 7
    chocolate = 4
    cookies = 9
    mint = 3
    
for s in Shake:
    print(s.value)