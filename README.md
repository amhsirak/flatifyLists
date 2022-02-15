## flatify-list

Flatten nested Python lists into single-depth lists

### Installation

```
pip install flatify-list
```

### Example

```py
from flatify-list import flatifyList

example = [[[1,2], [3,[4,[5],6],7],8,9]]

print(flatifyList(example))

# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### License

MIT <a href="https://github.com/karishmashuklaa/">Karishma Shukla</a> 
