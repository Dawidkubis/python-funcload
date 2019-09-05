# python-funcload
Load function variables directly into python interactive mode
(still work in progress)
## Usage
```python
def test(a, b)
  x = 64
  print(a+b)
```
```
>>> from fcld import load
>>> cache = load('test', (2,3))
 5
>>> cache.x
 64
>>> cache.a
 2
```
