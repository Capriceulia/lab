```python
text = str(input("Введите предложение:"))
print(len(text))
print(text.lower())
x = "aeiou"
i = 0
for a in text:
    if a in x:
        i +=1
print(i)
new_text = text.replace("ugly", "beauty")
print(new_text)
if text.startswith("The") and text.endswith("end"):
    print("Предложение построенно правильно")
else:
    print("Начните предложение с 'The'' и закончите 'end")
```
