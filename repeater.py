# -*- coding: utf-8 -*-
import json
f = open('./data/data.json', 'r')
data = json.load(f)
f.close()


def duang(_input):
    _output = ''
    for char in _input:
        if char in data:
            _output += data.get(char)
        else:
            _output += char
    return _output


if __name__ == '__main__':
    input = '不，应邀帮人搞事'
    print(input)
    print(duang(input))

