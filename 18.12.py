

# def find_longest_word(words):
#     words = words.split()
#     biggest = len(words[0])
#     longest_word = words[0]
#     # for i in range(1, len(words)):
#     for i in words:
#         if len(words[i]) > biggest:
#             longest_word = words[i]
#     return longest_word


# result = find_longest_word("salome gio nia")
# print(result)


def abbreviate(word):
  return ''.join([word[0] for word in word.split()])

print(abbreviate("Caucasus University"))