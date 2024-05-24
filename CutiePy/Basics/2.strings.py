print("Input your name and age to create a story line:")
name = input()
age = int (input()) #python scans strings by default

template = ("I am %s the king of CutiePy, I am ruling for %d years.")
story = template % (name,age)

print(story)

#finding length
l = len(story)
print("Length of this story: ", l)

#how to replace
r = story.replace("CutiePy", "World")
print("Replaced sentence:\n",r)