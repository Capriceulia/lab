```python
with open("file.txt", "r") as file:
    bad_words = [line.strip() for line in file]
    input_sentence = input("Введите предложение: ")

    input_sentence = input_sentence.lower()
    bad_words = [word.lower() for word in bad_words]

    words = input_sentence.split()

    censored_words = []
    for word in words:
        if word in bad_words:
            censored_word = '*' * len(word)
            censored_words.append(censored_word)
        else:
            censored_words.append(word)

    censored_sentence = ' '.join(censored_words)

    print(f"Готовое предложение:{censored_sentence}"
```
