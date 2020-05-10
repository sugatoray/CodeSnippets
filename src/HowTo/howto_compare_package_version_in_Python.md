# Comparing package version nuumbers in Python

Use [`packaging.version.parse`][#package-version-parse] to compare package versions in python.

[#package-version-parse]: https://packaging.pypa.io/en/latest/version/#packaging.version.parse

```python
from packaging import version

# Compare Version Numbers with numeric version
version.parse("2.3.1") < version.parse("10.1.2") # output: True

# Compare Version Numbers with alphanumeric version 
version.parse("1.3.a4") < version.parse("10.1.2") # output: True

# Check Version 
isinstance(version.parse("1.3.a4"), version.Version) # output: True

# Check Legacy Version 
isinstance(version.parse("1.3.xy123"), version.LegacyVersion) # output: True
```

## References

1. [How do I compare version numbers in Python?][#stackoverflow]

[#stackoverflow]: https://stackoverflow.com/questions/11887762/how-do-i-compare-version-numbers-in-python
