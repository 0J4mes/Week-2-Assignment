# Data Structures Demo: Set Comprehensions and `zip()` Function

This project demonstrates two Python concepts:
1. **Set Comprehensions**
2. **The `zip()` Function**

---

## **Set Comprehensions**
Set comprehensions provide a concise way to create sets. They are similar to list comprehensions but produce sets, which are unordered collections of unique elements.

### Example 1: Creating a Set of Squares
```python
squares_set = {x ** 2 for x in range(1, 11)}
