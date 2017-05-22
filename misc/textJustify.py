#!/usr/bin/python
"""
Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

#68
"""

def lineJustify(ws, lWidth):
    rslt = []
    w_idx = 0
    while w_idx < len(ws):
        t_char_len = 0
        curr_ln_ws = []
        while w_idx < len(ws) and t_char_len + len(ws[w_idx])+1 <= lWidth+1:
            t_char_len += len(ws[w_idx])+1
            curr_ln_ws.append(ws[w_idx])
            w_idx += 1

        extra_sp = lWidth - (t_char_len-1)
        # distribute space
        line = distr_sp(curr_ln_ws, extra_sp, lWidth,  w_idx==len(ws))

        rslt.append(line)

    return rslt

def distr_sp(curr_ln_ws, extra_sp, lWidth, is_last_ln):
    num_words = len(curr_ln_ws)
    num_slots = num_words - 1
    if num_slots == 0: return curr_ln_ws[0] + ' '*extra_sp

    if is_last_ln:
        line = ''
        for w in curr_ln_ws:
            line = line + w + ' '
        line += ' '*(lWidth-len(line))
        return line

    num_even_distr_extra_sp = extra_sp/num_slots
    num_rem_extra_sp = extra_sp%num_slots
    rem_sp_idx = 0
    line = curr_ln_ws[0]
    for w in curr_ln_ws[1:]:
        rem_sp = ' ' if rem_sp_idx < num_rem_extra_sp else ''
        line += ' '*(num_even_distr_extra_sp+1) + rem_sp + w
        rem_sp_idx += 1

    return line

def test1():
    ws = ["This", "is", "an", "example", "of", "text", "justification."]
    lWidth = 16
    print(lineJustify(ws, lWidth))

def test2():
    ws = ["What","must","be","shall","be."]
    lWidth = 12
    print(lineJustify(ws, lWidth))

def test3():
    ws = ["My","momma","always","said,","\"Life","was","like","a","box","of","chocolates.","You","never","know","what","you're","gonna","get."]
    lWidth = 20
    print(lineJustify(ws, lWidth))

if __name__ == '__main__':
    test1()
    test2()
    test3()
