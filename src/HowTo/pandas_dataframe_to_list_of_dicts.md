# Pandas DataFrame to list of dicts

You can do this with `df.to_dict(orient='records')`.

```python
df.to_dict(orient='records')

# [{'ID': 'T001', 'PKID': '58306, 57011', 'Subject': 'ABC', 'yr': 2017},
#  {'ID': 'T002', 'PKID': '1234,54321', 'Subject': 'XYZ', 'yr': 2018}]
```

## Dummy Data

```python
d = {"0":{"yr":2017,"PKID":"58306, 57011","Subject":"ABC","ID":"T001"},
     "1":{"yr":2018,"PKID":"1234,54321","Subject":"XYZ","ID":"T002"}}
df = pd.DataFrame(d).T
print(df)

## Output:
#      yr          PKID Subject    ID
# 0  2017  58306, 57011     ABC  T001
# 1  2018    1234,54321     XYZ  T002
```
