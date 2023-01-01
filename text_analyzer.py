# Put the desired text you want to analyze, when the input is asked for.
text = input()

# This will print the number count of the words that are present in your text.
print(len(text.split()))

# Creating a dictionary.
word_count = {}

# We have created a dictionary. This will allow the counting of the repeated words and all the unique words will be displayed seperately.
# We have converted all the letters into a lowercase so that 'the' and 'The' is counted as the same.
for word in text.lower().split():
# We check here if the word is already present in the dictionary or not.
  if word in word_count:
    word_count[word] = word_count[word] + 1
  else:
    word_count[word] = 1

# This prints our dictionary.
print(word_count)
