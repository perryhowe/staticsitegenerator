from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            new_node = node.text.split(delimiter)
            if len(new_node) % 2 == 0:
                raise Exception("invalid markdown - delimiters don't match")
            for i in range(len(new_node)):
                if i % 2 != 0:
                    new_nodes.append(TextNode(new_node[i], text_type))
                else:
                    new_nodes.append(TextNode(new_node[i], TextType.TEXT))
    return new_nodes