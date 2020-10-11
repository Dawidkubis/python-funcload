# python-funcload
Load function variables directly into python interactive mode
(not very useful)
## Usage
```python
def test(a, b)
  x = 64
  print(a+b)
```
```python
>>> from fcld import load
>>> cache = load('test', (2, 3))
 5
>>> cache.x
 64
>>> cache.a
 2
```
