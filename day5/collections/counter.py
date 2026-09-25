# counter counts how many times an value occured in an list
from collections import Counter
lists=["python","sql","python","java","python","sql"]
counter=Counter(lists)
print(counter["python"])
print(counter)
print(counter.most_common(2))

