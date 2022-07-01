file_name = "english-common-words.txt"

file = open(file_name)

words = file.read().splitlines()
file.close()

print(words[:3])
