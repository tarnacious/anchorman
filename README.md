# Anchorman

Turn your text into a [hypertext](http://en.wikipedia.org/wiki/Hypertext).
Anchorman provides a class to add and remove elements into a text the way
you specify it, as anchors, links, abbreviations or just `highlighting` them.


## Example

```
>>> import anchorman
>>> text = "The quick brown fox jumps over the lazy dog."
>>> links = [{'fox': {'value': '/wiki/fox'}},
             {'dog': {'value': '/wiki/dog'}}]
>>> a = anchorman.add(text, links)
>>> print a
The quick brown <a href="/wiki/fox" class="anchorman">fox</a> jumps over
the lazy <a href="/wiki/dog" class="anchorman">dog</a>.
```

See [more examples](#user-content-more-examples) at bottom.


## Building

    python setup.py develop


## Installing

    python setup.py install


## Testing in a virtualenv

    virtualenv .
    ./bin/pip install -r requirements.txt
    ./bin/py.test test


## Todos

    * return more sophisticated linking info
    * improve case sensitiv replacement option
    * refactor the module interface
    * prepare big data set input, e.g. 4000 abbreviations at once


## <a name="more-examples"></a> More examples

```
>>> import anchorman
>>> text = "The quick brown fox jumps over the lazy dog while the red
fox sleeps."
```


### Parameters

Toplevel params as **kwargs

 Parameter         |      Note
-------------------|-------------
markup_format      | tag, value attribute or highlighting with pre n post
replaces_per_item  | default is replace all occurences


Params on markup_format level

 Parameter     |      Note
---------------|-------------
case-sensitive |  default is True, with **False** replace: Fox, fox and FOX
rm-identifier  |  create identifier to delete specific items


### Links with different attributes

Define general attribute, value pairs on markup_format level and more specific
ones at link level as follows.

```
>>> markup_format = {
        'tag': 'a',
        'value_key': 'href',
        'attributes': [
            ('style', 'color:blue;cursor:pointer;'),
            ('class', 'anchorman')
        ]
     }
>>> links = [{
        'red fox': {
            'value': '/redfox',
            'attributes': [
                ('class', 'animal'),
                ('style', 'font-size:23px;background:red'),
                ('title', 'Fix und Foxi')
            ]
        }
    }]
>>> a = anchorman.add(text, links, markup_format=markup_format)
The quick brown fox jumps over the lazy dog while the <a href="/redfox"
style="color:blue;cursor:pointer; font-size:23px;background:red"
class="anchorman animal" title="Fix und Foxi">red fox</a> sleeps.
```


### Highlighting

Highlighting a term with pre- an postfix, e.g. variables in templates or low level tags.

```
>>> links = [{'fox': {}}]
>>> markup_format = {
        'highlighting': {
            'pre': '${{',
            'post': '}}'
        }
    }
>>> a = anchorman.add(text, links, markup_format=markup_format)
>>> print a
The quick brown ${{fox}} jumps over the lazy dog while the red
${{fox}} sleeps.
```
