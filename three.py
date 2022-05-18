listArr = [1, 2, 1, 3, 2, 2]
set = {1, 1, 3, 4, 5, 5}
set2 = {1, 1, 9, 0}
print(listArr)
print(set)
print(set | set2)

teSet1 = {"A", "B", "C"}
teSet2 = {"F", "Z", "V", "V", "Z", "C"}
orr = teSet1 | teSet2
andd = teSet1 & teSet2
minus = teSet1 - teSet2
plus = teSet1 - teSet2
print(f"or =  {orr}")
print(f"and = {andd}")
print(f"minus = {minus}")
print(f"plus = {plus}")
