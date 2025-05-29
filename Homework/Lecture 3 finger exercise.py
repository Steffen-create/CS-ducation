
#Exercise 1
where = input("Go left or right? ")
count = 0
while where == "right":
    count += 1
    if count > 1:
        print(":( maybe try the other way)")
    where = input("Go left or right? ")
print("You got out!")


