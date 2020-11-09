# How to add emoji using Python

Use library: **emoji** :star: :star: :star: 

Github repo: https://github.com/carpedm20/emoji

## Trivia

- The word `emoji` is used both as a _singular_ and _plural_ noun. However, _emojis_ is also plural of `emoji`. [Source][#emoji-dictionary]
  
  [#emoji-dictionary]: https://www.merriam-webster.com/dictionary/emoji#:~:text=noun,plural%20emoji%20or%20emojis
  
- Know what an emoji stands for: 
📙 [Emojipedia][#emojipedia] — 😃 Home of Emoji Meanings 💁👌🎍😍

  [#emojipedia]: https://emojipedia.org/


## Installation

Via pip.

```bash
pip install emoji --upgrade
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

---

[![copyright-logo][#copyright-badge]][#copyright-badge] 

:bulb: :zap: :star2: [**How to add a copyright badge**][#howto-add-copyright-badge]

[#copyright-badge]: https://badgen.net/runkit/copyright-badge-rbydof6akjgg/America/Chicago+++name=sugatoray&color=green&start_year=2020
[#howto-add-copyright-badge]: https://github.com/sugatoray/CodeSnippets/blob/master/src/HowTo/howto_add_copyright_badge_in_markdown/howto_add_copyright_badge_in_markdown.md
