import reprlib #for abbreviated displays
print(reprlib.repr(set('supercalifragilisticexpialidocious')))
import pprint #control over printing when the result is longer than one line 
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]
print(t)
import textwrap # fit a given screen width
doc = """The wrap() method is just like fill() except that it returns
... a list of strings instead of one big string with newlines to separate
... the wrapped lines."""
print(textwrap.fill(doc, width=60))