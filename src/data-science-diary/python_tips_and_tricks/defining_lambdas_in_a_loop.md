# How to *correctly* define lambdas in a loop? 💡

🎯 [source](https://docs.python.org/3/faq/programming.html#id10)

![image](https://user-images.githubusercontent.com/10201242/129713646-e968dace-b77b-47f0-825a-a4d06650513d.png)

## This will not work 🔴

```python
# method-1
funcs = [lambda x: x**2 for x in range(5)]

# method-2
funcs = []
for x in range(5):
    funcs.append(lambda x: x**2)
```

## This will work 🟢

```python
# method-1
funcs = [lambda n = x: n**2 for x in range(5)]

# method-2
funcs = []
for x in range(5):
    funcs.append(lambda n = x: n**2)
```

## References

- [docs.python.org: *Why do lambdas defined in a loop with different values all return the same result?*][#ref-source]

[#ref-source]: https://docs.python.org/3/faq/programming.html#why-do-lambdas-defined-in-a-loop-with-different-values-all-return-the-same-result
