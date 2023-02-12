# A compilation of various functions and aliases

```sh
# A function to print a numeric value with a given number of leading digits
padnum() { VALUE=$1; NUMDIGITS=$2; $(which python3) -c "print(f'{${VALUE}:0${NUMDIGITS:-5}}')"; unset VALUE NUMDIGITS; }
```
