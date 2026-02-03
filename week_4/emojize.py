import emoji
import sys


x = input("Input: ").casefold()


if 'hello' in x:
    print('Output: hello', emoji.emojize(x, language='alias'))
else:
    print('Output:', emoji.emojize(x, language='alias'))


