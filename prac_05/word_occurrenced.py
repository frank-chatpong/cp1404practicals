"""
Word Occurrences
Estimate: 25 minutes
Actual:  23  minutes
"""

word_to_count = {}
text = input("Text: ").lower()
words = text.split()
for word in words:
    if word in word_to_count:
        word_to_count[word] += 1
    else:
        word_to_count[word] = 1

max_length = max((len(word) for word in word_to_count))

for word in sorted(word_to_count):
    print(f"{word:{max_length}} : {word_to_count[word]}")