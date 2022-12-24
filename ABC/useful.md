# keyが整数の辞書
{1: False, 2: False, 3: False, 4: False, 5: False, 6: False}
```
n = 100
d = {key: False for key in range(1,n+1)}
```

# keyがアルファベットの辞書
## 小文字
{'a': False, 'b': False, 'c': False, 'd': False, ...}
d = {chr(i): False for i in range(97,123)}

## 大文字
{'A': False, 'B': False, 'C': False, 'D': False, ...}
d = {chr(i): False for i in range(65,91)}