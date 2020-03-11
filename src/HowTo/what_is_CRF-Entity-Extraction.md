# Conditional Random Field (CRF) Entity Extraction

The goal of this document is to

1. Gather relevant sources.
1. Glean and explain _What CRF Entity Extraction is_.

The quest to look-up for CRF started from [<kbd>rasa-nlu-entity-extraction</kbd>][#rasa-nlu-entity-extraction]. 
There are a few [videos-links][#videos] provided as well.

https://github.com/sugatoray/CodeSnippets/new/master/src/HowTo#videos

---
## CRF Explanation:

**Conditional Random Fields** (CRFs) 
[[Lafferty 01][#Lafferty-01]] 
[[Sha 03][#Sha-03]] 
[[Sutton][#Sutton]] 
are used for labeling sequential data. There are various implementations of CRFs; see [here][#crfsuite] for more details.

According to wikipedia,
<!-------- wikipedia content asis --------->
>**Conditional random fields** (**CRFs**) are a class of [statistical modeling method](https://en.wikipedia.org/wiki/Statistical_model "Statistical model") often applied in [pattern recognition](https://en.wikipedia.org/wiki/Pattern_recognition "Pattern recognition") and [machine learning](https://en.wikipedia.org/wiki/Machine_learning "Machine learning") and used for [structured prediction](https://en.wikipedia.org/wiki/Structured_prediction "Structured prediction"). Whereas a [classifier](https://en.wikipedia.org/wiki/Statistical_classification "Statistical classification") predicts a label for a single sample without considering "neighboring" samples, a CRF can take context into account. To do so, the prediction is modeled as a [graphical model](https://en.wikipedia.org/wiki/Graphical_model "Graphical model"), which implements dependencies between the predictions. What kind of graph is used depends on the application. For example, in [natural language processing](https://en.wikipedia.org/wiki/Natural_language_processing "Natural language processing"), linear chain CRFs are popular, which implement sequential dependencies in the predictions. In image processing the graph typically connects locations to nearby and/or similar locations to enforce that they receive similar predictions.
>
>Other examples where CRFs are used are: [labeling](https://en.wikipedia.org/wiki/Sequence_labeling "Sequence labeling") or [parsing](https://en.wikipedia.org/wiki/Parsing "Parsing") of sequential data for [natural language processing](https://en.wikipedia.org/wiki/Natural_language_processing "Natural language processing") or [biological sequences](https://en.wikipedia.org/wiki/Bioinformatics "Bioinformatics")
<sup>[[1]](https://en.wikipedia.org/wiki/Conditional_random_field#cite_note-Laf:McC:Per01-1)</sup>
, [POS tagging](https://en.wikipedia.org/wiki/POS_tagging "POS tagging"), 
[shallow parsing](https://en.wikipedia.org/wiki/Shallow_parsing "Shallow parsing"),
<sup>[[2]](https://en.wikipedia.org/wiki/Conditional_random_field#cite_note-2)</sup> 
[named entity recognition](https://en.wikipedia.org/wiki/Named_entity_recognition "Named entity recognition"),
<sup>[[3]](https://en.wikipedia.org/wiki/Conditional_random_field#cite_note-3)</sup> 
[gene finding](https://en.wikipedia.org/wiki/Gene_prediction "Gene prediction"), peptide critical functional region finding
<sup>[[4]](https://en.wikipedia.org/wiki/Conditional_random_field#cite_note-4)</sup>
, and object recognition
<sup>[[5]](https://en.wikipedia.org/wiki/Conditional_random_field#cite_note-Rui:Gal:Gon15-5)</sup> 
and [image segmentation](https://en.wikipedia.org/wiki/Image_segmentation "Image segmentation") in [computer vision](https://en.wikipedia.org/wiki/Computer_vision "Computer vision")
<sup>[[6]](https://en.wikipedia.org/wiki/Conditional_random_field#cite_note-6)</sup>.

<!------- end of wikipedia content -------->

## Useful Sources

1. [Wikipedia - Conditional Random Field (CRF)][#crf-wikipedia]
1. [nlp-guide-conditional-random-fields-text-classification][#crf-analyticsvidhya]
1. [sklearn_crfsuite: docs][#sklearn-crfsuite-docs]
1. [CRFsuite - _by_ CRFsuite is an implementation of Conditional Random Fields (CRFs)][#crfsuite]

### Videos

1. [Coursera - CRF | <kbd>Length: 24:23</kbd> ](https://www.coursera.org/lecture/language-processing/memms-crfs-and-other-sequential-models-for-named-entity-recognition-Ctjm2)
1. [Stanford University - CRF | <kbd>Length: 11:54</kbd> ](https://www.youtube.com/watch?v=rc3YDj5GiVM)

### Google Search

1. [conditional random field (CRF) entity extractor][#conditional-random-field-(CRF)-entity-extractor]

<!---------- References ------------>

[#rasa-nlu-entity-extraction]: https://rasa.com/docs/rasa/nlu/entity-extraction/#entity-extraction
[#crf-wikipedia]: https://en.wikipedia.org/wiki/Conditional_random_field 
[#crfsuite]: http://www.chokkan.org/software/crfsuite/
[#sklearn-crfsuite-docs]: https://sklearn-crfsuite.readthedocs.io/en/latest/tutorial.html
[#crf-analyticsvidhya]: https://www.analyticsvidhya.com/blog/2018/08/nlp-guide-conditional-random-fields-text-classification/
[#Lafferty-01]: http://www.chokkan.org/software/crfsuite/#idp8853501200
[#Sha-03]: http://www.chokkan.org/software/crfsuite/#idp8854546608
[#Sutton]: http://www.chokkan.org/software/crfsuite/#idp8854560656
[#conditional-random-field-(CRF)-entity-extractor]: https://www.google.com/search?q=conditional+random+field+(CRF)+entity+extractor&safe=off&sxsrf=ALeKk00N1rQ2iDGFZSwQDBeldyangWnlxQ:1583881908000&source=lnms&tbm=vid&sa=X&ved=2ahUKEwiX8Pfzg5HoAhWHPM0KHdlTCRwQ_AUoAnoECA0QBA&biw=1536&bih=722
