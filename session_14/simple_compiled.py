import re

# Precompile the patterns
regexes = [ re.compile(p) for p in ['  Hello'] ]

text = 'Hello Python folks, How are you doing today?'

print('Text: {!r}\n'.format(text))

for regex in regexes:
    print (type(regex))
    print('Seeking "{}" ->'.format(regex.pattern), end=' ')

    if regex.search(text):
        print('Matching!')
    else:
        print('No, I am not matching')
