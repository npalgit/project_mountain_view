import java.util.*;
/*
Stream the HTML content given the representation below.
    input (represented by graph below):
        None
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
Same is implemented in python.
*/
class StreamingHTML {

    public void streamHTML(ArrayList<NodeListElement> node_list) {
        HashSet<HTMLNode> visited = new HashSet<HTMLNode>();
        Stack<HTMLNode> stck = new Stack<HTMLNode>();
        visited.add(null);
        stck.push(null);

        for (NodeListElement element : node_list) {
           dfs(element.getNode(), stck, visited);
           System.out.println(element.getText());
        }
    }

    public void dfs(HTMLNode node,
            Stack<HTMLNode> stck, HashSet<HTMLNode> visited) {
        if (visited.contains(node)) {
            while (node != stck.peek()) {
                HTMLNode top_node = stck.pop();
                System.out.println(close_tag(top_node.getTag()));
            }
        } else {
            dfs(node.getParent(), stck, visited);
            System.out.println(open_tag(node.getTag()));
            stck.push(node);
            visited.add(node);
        }
    }
    
    public String close_tag(String tag) {
        return "</" + tag + ">";
    }

    public String open_tag(String tag) {
        return "<" + tag + ">";
    }

    public static void main(String[] args) {
        HTMLNode HTML = new HTMLNode("HTML"); 
        HTMLNode BODY = new HTMLNode("BODY"); 
        HTMLNode A    = new HTMLNode("A"); 
        HTMLNode B    = new HTMLNode("B");
        HTMLNode DIV  = new HTMLNode("DIV");

        BODY.setParent(HTML);
        A.setParent(BODY);
        B.setParent(A);
        DIV.setParent(BODY);
        ArrayList<NodeListElement> node_list = new ArrayList<NodeListElement>();
        node_list.add(new NodeListElement(BODY, "text1"));
        node_list.add(new NodeListElement(B, "text2"));
        node_list.add(new NodeListElement(BODY, "text3"));
        node_list.add(new NodeListElement(DIV, "text4"));
        node_list.add(new NodeListElement(BODY, "text5"));
        node_list.add(new NodeListElement(null, ""));
        
        StreamingHTML sHTML = new StreamingHTML();
        sHTML.streamHTML(node_list);
    }
}

class HTMLNode {
    private String tag;
    private HTMLNode parent;

    public HTMLNode(String tag) {
        this.tag = tag;
        this.parent = null;
    }

    public String getTag() {
        return this.tag;
    }

    public HTMLNode getParent() {
        return this.parent;
    }

    public void setParent(HTMLNode parent) {
        this.parent = parent;
    }
}

class NodeListElement {
    private HTMLNode node;
    private String text;

    public NodeListElement(HTMLNode node, String text) {
        this.node = node;
        this.text = text;
    }

    public HTMLNode getNode() {
        return this.node;
    }

    public String getText() {
        return this.text;
    }
}
