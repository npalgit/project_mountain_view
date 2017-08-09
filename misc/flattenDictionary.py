#!/usr/bin/python
"""
flatten:
{
    'a': 'app',
    'b': {
        'b': 'bbb',
        'c': 'ccc'
    }
}

to
'{a:app, b:{b:bbb,c:ccc}}'
Atlassian phone interview where I screwed up
"""
def flatten(dic_content):
    if type(dic_content) is str:
        return dic_content

    res = []
    for key, content in dic_content.iteritems():
        res.append(key + ':' + flatten(content))

    return '{' + ','.join(res) + '}'

def test1():
    input = {'a': 'app', 'b': {'b': 'bbb','c': 'ccc'}}
    print(flatten(input))

if __name__ == '__main__':
    test1()
