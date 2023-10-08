```python
def minimum(file):
    with open (file) as f:
        words = f.read().split()
        min_len = len(min(words, key=len))
        for word in words:
            if len(word) == min_len:
                search = word
        if len(search) == 1:
            return search[0]
        return search
print(minimum('file.txt'))
```
