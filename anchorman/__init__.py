#!/usr/bin/env python
# encoding: utf-8

from .anchorman import *


"""
anchorman library
~~~~~~~~~~~~~~~~~~~~~
Anchorman is a library, written in Python.

   >>> import anchorman
   >>> links = [('Fox', 'http://www.wikipedia.en/fox')]
   >>> text = "<p>The quick brown fox jumps over the lazy dog.</p>"
   >>> anchorman.add(text, links)
   <p>The quick brown <a class="anchorman" href="http://www.wikipedia.en/fox">Fox</a> jumps over the lazy dog.</p>


:copyright: (c) 2015 by Tarn Barford.
:license: Apache 2.0, see LICENSE for more details.
"""
