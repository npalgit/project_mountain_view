#!/usr/bin/python
"""
Stream the HTML content given the representation below.
    input (represented by graph below):
        None
        |
        HTML
        |
     --BODY --------
    |   |  \   \    \
    |   A   |  DIV  |
    |   |   |   |   |
    |   B   |   |   |
    |   |   |   |   |
    1   2   3   4   5   6

    output:
    <HTML>
        <BODY> text1
            <A><B>text2</B></A>text3
            <DIV>text4</DIV>text5
        </BODY>
    </HTML>
Microsoft onsite last round probably 30 min to solve the problem.
didn't end up writing code. Very little hints are given.
"""
class HTMLNode:
    def __init__(self, tag):
        self.parent = None
        self.tag = tag

class NodeListElement:
    def __init__(self, node, text):
        self.node = node
        self.text = text

def streamHTML(node_list):
    visited = set([None])
    stck = [None]

    for element in node_list:
        dfs(element.node, stck, visited)
        print(element.text)

def dfs(node, stck, visited):
    if node in visited:
        while node != stck[-1]:
            print(close_tag(stck.pop().tag))
    else:
        dfs(node.parent, stck, visited)
        print(open_tag(node.tag))
        stck.append(node)
        visited.add(node)

def open_tag(tag):
    return "<{}>".format(tag)

def close_tag(tag):
    return "</{}>".format(tag)

def test1():
    """
    input (represented by graph below):
        None
        |
        HTML
        |
     --BODY --------
    |   |  \   \    \
    |   A   |  DIV  |
    |   |   |   |   |
    |   B   |   |   |
    |   |   |   |   |
    1   2   3   4   5   6

    output:
    <HTML>
        <BODY> text1
            <A><B>text2</B></A>text3
            <DIV>text4</DIV>text5
        </BODY>
    </HTML>
    """
    HTML = HTMLNode('HTML')
    BODY = HTMLNode('BODY')
    A    = HTMLNode('A')
    B    = HTMLNode('B')
    DIV  = HTMLNode('DIV')

    BODY.parent = HTML
    A.parent = BODY
    B.parent = A
    DIV.parent = BODY
    node_list = []
    node_list.append(NodeListElement(BODY, 'text1'))
    node_list.append(NodeListElement(B, 'text2'))
    node_list.append(NodeListElement(BODY, 'text3'))
    node_list.append(NodeListElement(DIV, 'text4'))
    node_list.append(NodeListElement(BODY, 'text5'))
    node_list.append(NodeListElement(None, ''))
    streamHTML(node_list)

if __name__ == '__main__':
    test1()
