class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        new_str = ''
        if self.props is None or self.props == {}:
            return new_str
        for i in self.props:
            new_str += f' {i}="{self.props[i]}"'
        return new_str
    
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError('value is missing')
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f'LeafNode({self.tag}, {self.value}, {self.props})'
    

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        new_str = ''
        if self.tag is None:
            raise ValueError('tag is missing')    
        if self.children is None:
            raise ValueError('children is missing')
        for child in self.children:
            new_str += child.to_html()
        return f'<{self.tag}{self.props_to_html()}>{new_str}</{self.tag}>'