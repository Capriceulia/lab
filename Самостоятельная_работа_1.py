```python
with open("file.txt", "r") as file:
    text = file.read()

words = text.lower().split()
words= [word.strip('.,!?()[]{}":;') for word in words]

word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

often = max(word_count, key=word_count.get)
count = word_count[often]

print(f"Всего слов: {len(words)}")
print(f"Часто встречающиеся слово: '{often}'")
print(f"Сколько раз встречается: {count}")
```
