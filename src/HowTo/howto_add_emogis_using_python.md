# How to add emogies using Python

Use library: **emogi** :star: :star: :star: 

Github repo: https://github.com/carpedm20/emoji

## Installation

Via pip.

```bash
pip install emogi --upgrade
```

## Example

> The entire set of Emoji codes as defined by the [unicode consortium][#unicode-consortium] is supported in addition to a bunch of aliases. 
By default only the official list is enabled but doing `emoji.emojize(use_aliases=True)` enables both the full list and aliases.

[#unicode-consortium]: http://www.unicode.org/Public/emoji/1.0/full-emoji-list.html

```python
>> import emoji
>> print(emoji.emojize('Python is :thumbs_up:'))
Python is 👍
>> print(emoji.emojize('Python is :thumbsup:', use_aliases=True))
Python is 👍
>> print(emoji.demojize('Python is 👍'))
Python is :thumbs_up:
>>> print(emoji.emojize("Python is fun :red_heart:"))
Python is fun ❤
>>> print(emoji.emojize("Python is fun :red_heart:",variant="emoji_type"))
Python is fun ❤️ #red heart, not black heart
```
