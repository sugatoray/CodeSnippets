# This is a markdown file

> :bulb: **Objective**: Create a set of markdown snippets for people new to markdown to learn quickly.

<style>
    .custom-paragraph {
        background-color: green;
        color: yellow;
    }
</style>

All right, let's start writing and when I tell you to stop, then you will stop.

Write a markdown walk through to help people learn markdown quickly.[^1]

[^1]: This is a footnote.

- H<sub style="background-color: green; color: yellow;">2</sub>O
- <p style="background-color: green; text-color: yellow;">X<sup>3</sup></p>
- <p style="background-color: green; color: yellow;">X<sup>3</sup></p>
- <p class="custom-paragraph">Test</p>
- This is a ==highlighted text== [^2]
- This is a <mark>highlighted text</mark>
- This is a <mark style="background-color: green">highlighted text</mark>
- This is a <mark style="background-color: rgb(100,200,30);">highlighted text</mark>
- This is a <mark style="background-color: rgb(200,30,100,0.5);">highlighted text</mark>
- This is an <ins>underlined</ins> text.
- This is an <em>italicized</em> text.
- This is a <strong>bold</strong> text.
- This is a <b>bold</b> text.
- This is an <i>italicized</i> text.
- This is an <u>underlined</u> text.

[^2]: This is the 2nd footnote.
      
    <details>
    <summary>Click to expand</summary>
    This is the expanded text.

    <p>

    ```bash
    cat filepath | grep "pattern"
    ```
    
    </p>

    <span class="custom-paragraph">

    This is a highlighted text. Some more text.
    This is a <mark style="background-color: rgb(200,30,100,0.5);">highlighted text</mark>. <font color="green">Some more text</font>.

    </span>

    $$ x = \int{sin(\alpha z + \beta)\frac{y\left(\alpha, z\right)}{\beta e^{z}}}{dz} $$

    </details>

![logo](https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png "Google Logo")

```html
<script>
    console.log('Hello World');
    .custom-paragraph {
        background-color: green;
        color: yellow;
    }
</script>
```

## Simple alerts

Admonitions are simple, predefined, and easy to use. They are a great way to add simple alerts to your documentation. [^3]

[^3]: See the discussion on adding markdown admonitions on [stackoverflow](https://stackoverflow.com/a/72327818/8474894 "Markdown Admonitions").
      
    > [!TIP]
    > 
    > :point_right: <https://stackoverflow.com/questions/50544499>

> [!NOTE]
> This is a note.

> [!TIP]
> This is a tip. (Supported since 14 Nov 2023)

> [!IMPORTANT]
> Crutial information comes here.

> [!CAUTION]
> Negative potential consequences of an action. (Supported since 14 Nov 2023)

> [!WARNING]
> Critical content comes here.

## Reference

- [Markdown Guide](https://www.markdownguide.org/)
- [Using CSS in Markdown](https://stackoverflow.com/questions/27174946/how-to-use-css-in-markdown)
- [Markdown Footnotes](https://www.markdownguide.org/extended-syntax/#footnotes)
