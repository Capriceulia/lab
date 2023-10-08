```python
with open("file.txt", "r") as file:
    text = file.read()
    words = text.split()
    words_count = len(words)
    sentences = text.split('\n')
    sentences_count = len(sentences)

    letter_count = sum(1 for char in text if char.isalpha())

    print("Input file contains:")
    print(f"{letter_count} letters")
    print(f"{words_count} words")
    print(f"{sentences_count} lines")
```
