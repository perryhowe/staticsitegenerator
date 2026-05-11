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