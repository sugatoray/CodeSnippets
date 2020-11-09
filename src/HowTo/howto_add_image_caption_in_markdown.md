# How to add caption to an image in `markdown`

This is one of the ways of adding caption to an image in markdown.

```markdown
[![sample-image][#sample-image-url]][#sample-image-url]
<p align="center"><em>Caption: This is a sample image</em></p>

[#sample-image-url]: link-to-your-image
```

[![sample-image][#sample-image-url]][#sample-image-url]
<p align="center">
  <em>Caption: This is a sample image**</em>
  <br/>
  <samll><samll>** Courtesy - Royalty free Adobe stock photos: https://stock.adobe.com/photos</small></samll>
</p>

[#sample-image-url]: https://s.ftcdn.net/v2013/pics/all/curated/c6REvpXnikGKONxgdJZmZfsSSgRkpwtI_hero_1555.jpg

## References

1. [Stackoverflow - *Markdown native text alignment*](https://stackoverflow.com/questions/14051715/markdown-native-text-alignment)
1. [Markdown captions](https://thesynack.com/posts/markdown-captions/)
1. [Using an image caption in Markdown Jekyll](https://stackoverflow.com/questions/19331362/using-an-image-caption-in-markdown-jekyll)
