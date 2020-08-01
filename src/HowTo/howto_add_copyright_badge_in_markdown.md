# Adding Copyright Information as a Badge in Your Markdown Document

A typical copyright statement, often located at the bottom of web-pages looks as follows:

- Copyright &copy; Sugato Ray | 2020
- Copyright &copy; Sugato Ray | 2018-2020
- Copyright &copy; Sugato Ray. All Rights Reserved. 2020-2021. 

The problem is that you would manually have to update the latest date (the current year - `2020`, in this case). This brings the question then, *how to dynamically update the copyright year?*

In a regular HTML page you could paste in the following script and be done with it.

**HTML script for generating dynamic copyright information.**

```html
<p style="text-align: left"> Copyright &copy; 2014-<script>document.write(new Date().getFullYear())</script> Sugato Ray. All Rights Reserved.</p>
```

However, if you try using the script above in *GitHub* or *GitLab*, it will not work there. So, is there any way such that we could get the current year from a web-service and embed the result in GitHub? Well, that's actually what various badges do on GitHub and GitLab, or even on various websites. 

What is a badge? 
A badge is essentially an image generated with some information from either a static source or a dynamic server-output. You often see them on GitHub repositories.

Typically a copyright badge would have the following format.

```markdown
[![copyright-logo][#copyright-badge]][#copyright-badge]

[#copyright-badge]: your/copyright/badge-url
```

Now the key ingredients are:

1. Badge Generating Services
   
   - `Shields.io`: https://shields.io/
   - `Badgen.net`: https://badgen.net/
     - GitHub repo: https://github.com/badgen/badgen.net
  
2. Dynamic information producing web-service
   
   - `RunKit.com`: https://runkit.com/home
     - Copyright Badge Project: https://runkit.com/sugatoray/copyright-badge 

We will later see below, how we use this `copyright-project` to generate the copyright badge that we could use on any markdown and website seamlessly.

## The **Copyright Badge** Project at RunKit.com

The `Copyright Badge` project: https://runkit.com/sugatoray/copyright-badge

## **Static Badge**

**Static badge:** *shields.io*

[![copyright-logo][#copyright-badge-static-shields-io]][#copyright-badge-static-shields-io]

[#copyright-badge-static-shields-io]: https://img.shields.io/badge/Copyright%20%C2%A9%20sugatoray-2020--2021-green?style=flat

**Static badge:** *badgen.net*

[![copyright-logo][#copyright-badge-static-badgen-net]][#copyright-badge-static-badgen-net]

[#copyright-badge-static-badgen-net]: https://badgen.net/badge/Copyright%20%C2%A9%20sugatoray/2018-2020/green

## `Shields.io` Syntax Summary

- Main site: https://shields.io/

```bash
# Using dash "-" separator
https://img.shields.io/badge/<LABEL>-<MESSAGE>-<COLOR>

## Conversion Logic for 
#    Dash(es)
#    Underscore(s)
#    Space(s)
# Dashes -- → - Dash
# Underscores __ → _ Underscore
# _ or Space  →  Space

# Using query string parameters
https://img.shields.io/static/v1?label=<LABEL>&message=<MESSAGE>&color=<COLOR>
```

## `Badgen.net` Syntax Summary

- Classic style: https://badgen.net/
- Flat style: https://flat.badgen.net/

```bash
https://badgen.net/badge/:subject/:status/:color?icon=github
                   ──┬──  ───┬───  ──┬───  ──┬── ────┬──────
                     │       │       │       │       └─ Options (label, list, icon, color)
                     │       │       │       │
                     │      TEXT    TEXT    RGB / COLOR_NAME ( optional )
                     │
                  "badge" - default (static) badge generator
```

## **Dynamic Badge**

The problem with a static badge is that it does not update the current year of copyright. This is why I used a runkit.com notebook to create an ndpoint and provide necessary information (current year, etc.) as a `JSON` and feed that to badgen.net service. The following is an example of what parameters could be specified by the user to generate the JSON.

```python
dict(
    name = 'yourname', # default: ''
    start_year = 2018, # default: current year (auto evaluated at the time of call)
    color = 'green', # default: green
    message = 'Copyright ©', # default: 'Copyright ©'
    num_spaces = 1, # number of spaces between <message> and <name>
)
```

**Dynamic badge:** *badgen.net* + *runkit-endpoint*

Here is an example using `name=sugatoray, start_year=2018, color=green`

Using: *RUNKIT-endpoint* in badgen.net

[![copyright-logo][#copyright-badge-dynamic]][#copyright-badge-dynamic] 

[#copyright-badge-dynamic]: https://badgen.net/runkit/copyright-badge-rbydof6akjgg/America/Chicago+++name=sugatoray&color=green&start_year=2018

**`URL`**

```bash
## Note: A temporary HACK
# the +++ sign separates the key-value pairs from the rest of the url
# this is a temporary hack
https://badgen.net/runkit/copyright-badge-rbydof6akjgg/America/Chicago+++name=sugatoray&color=green&start_year=2018
```

Using: *HTTP-endpoint* in badgen.net

[![copyright-logo][#copyright-badge-dynamic]][#copyright-badge-dynamic] 

[#copyright-badge-dynamic]: https://badgen.net/https/copyright-badge-rbydof6akjgg.runkit.sh/America/Chicago+++name=sugatoray&color=green&start_year=2018

**`URL`**

```bash
## Note: A temporary HACK
# the +++ sign separates the key-value pairs from the rest of the url
# this is a temporary hack
https://badgen.net/https/copyright-badge-rbydof6akjgg.runkit.sh/America/Chicago+++name=sugatoray&color=green&start_year=2018
```

---

## References

Answer the following question on stackoverflow later:

https://stackoverflow.com/questions/54563526/is-there-markdown-syntax-that-will-allow-my-copyright-date-to-automatically-upda
