
#print("Hello " + "Angela")

#print("Hello " + input("What is your name?\n") )

#print(len(input("What is your name?")))

#name = input("Name? ")
#print("nama nya : " + name)

#subscript
#print("Hello"[0])
print("Hello"[len("Hello")-1])

#Integer
print(1+2)

#Float
print(2.5)

print(True)

#convert

num_char = 5
print(type(num_char))
new_num_char = str(num_char)
print(type(new_num_char))

print("your name has " + new_num_char + " characters")

#to float
print(type(float("20.5")))

print(round(2.66, 2))
print(8/3)
print(8//3)

score = 0
score += 1
print("Score : " + str(score))

#f-String
print(f"you score is {score}")


#if else
tinggi = int(input("Tinggi : "))
if tinggi > 60:
    print("wow tinggi ya")
elif tinggi > 50:
    print("lumayan")
else:
    print("ga tinggi")