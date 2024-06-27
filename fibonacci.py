
### `fibonacci.py`
```python
import sys

def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python fibonacci.py <number>")
    else:
        number = int(sys.argv[1])
        print(fibonacci(number))
