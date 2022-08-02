from typing import List, Tuple
from sortedcontainers import SortedList

status1 = SortedList([])
status1.add(1)
status1.add(-1)
status1.add(-5)

print(status1.bisect_left(-5))
print(status1)
