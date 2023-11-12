class Node:
    def __init__(self, tag):
        self.tag = tag
        self.children = []
        self.data = None

    def add_child(self, child_node):
        self.children.append(child_node)


class HTMLTreeBuilder:
    def __init__(self):
        self.tree = None
        self.current_node = None
        self.stack = []

    def handle_starttag(self, tag, attrs):
        new_node = Node(tag)
        if self.current_node is None:
            self.tree = new_node
        else:
            self.current_node.add_child(new_node)
        self.stack.append(self.current_node)
        self.current_node = new_node

    def handle_endtag(self, tag):
        if self.stack:
            self.current_node = self.stack.pop()

    def handle_data(self, data):
        if data:
            if self.current_node:
                # self.current_node.data = data # I fixed it, because the data was not calculated correctly
                if self.current_node.data:
                    self.current_node.data += data
                else:
                    self.current_node.data = data.strip()

    def feed(self, html_content):
        is_tag = False
        tag = ''
        attr_start = False
        attr = ''
        in_quotes = False

        for char in html_content:
            if char == '<':
                is_tag = True
                tag = ''
                attr_start = False
                attr = ''
                in_quotes = False
            elif char == '>':
                is_tag = False
                if tag.startswith('/'):  # Closing tag
                    self.handle_endtag(tag[1:])
                else:
                    self.handle_starttag(tag, self.parse_attributes(attr))
            elif is_tag:
                if char.isspace() and not attr_start:
                    attr_start = True
                elif char == '=' and attr_start:
                    in_quotes = True
                elif char.isspace() and in_quotes:
                    pass
                elif char in ('"', "'") and in_quotes:
                    in_quotes = False
                else:
                    if attr_start:
                        attr += char
                    else:
                        tag += char
            else:
                self.handle_data(char)

    def parse_attributes(self, attr_str):
        # Simple attribute parsing
        attrs = []
        parts = attr_str.split('=')
        for i in range(0, len(parts), 2):
            if i + 1 < len(parts):
                name = parts[i].strip()
                value = parts[i + 1].strip('"\'')

                attrs.append((name, value))
        return attrs
