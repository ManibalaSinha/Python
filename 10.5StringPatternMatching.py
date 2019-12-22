# re module provides regular expression tools for advanced string processing
import re
#\b: Returns a match where the specified characters are at the beginning or at the end
print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))#\bf search character f
#\1 means first group, r'\1'repeated word will be placed by single word
print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))
print('tea for too'.replace('too', 'two'))