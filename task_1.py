from additionalModule import HTMLTreeBuilder
from collections import defaultdict

# Create an instance of the HTMLTreeBuilder
parser = HTMLTreeBuilder()


# Test cases
def test_empty_html():
    # Sample HTML content
    html_content = """
    """
    parser.feed(html_content)
    assert parser.tree is None, f"Expected None, received {parser.tree} # Empty html"


def test_wrong_tags():
    # Sample HTML content
    html_content = """
    </div></p>
    """
    parser.feed(html_content)
    assert parser.tree is None, f"Expected None, received {parser.tree} # Only closed tags"

    # Sample HTML content
    html_content = """
    <div><p>Some content</div>
    """
    parser.feed(html_content)
    assert parser.tree is None, f"Expected None, received {parser.tree} # Incorrectly nested tags"


def test_different_structures():

    def tree_traversal(node):
        if node:
            result.append(node.tag)
            for child in node.children:
                tree_traversal(child)

    def recursion_func(node):
        result_data = defaultdict(dict)
        if node:
            if node.children:
                for child in node.children:
                    result_data[node.tag].update(recursion_func(child))
            else:
                result_data[node.tag] = node.data.strip()
        return result_data

    # Test 1 - correct data
    # Sample HTML content
    html_content = """
    <title>Sample Page</title>
    """
    parser.feed(html_content)
    data = parser.tree.data
    assert data == 'Sample Page', f"Expected 'Sample Page', received {data} # Test 1"

    # Test 2 - all tags
    # Sample HTML content
    html_content = """
    <html>
      <head>
        <title>Sample Page</title>
      </head>
      <body>
        <ul>
          <li>List Item 1</li>
          <li>List Item 2</li>
        </ul>
      </body>
    </html>
    """
    parser.feed(html_content)

    result = []
    tree_traversal(parser.tree)
    assert result == ['html', 'head', 'title', 'body', 'ul', 'li', 'li'], \
        f"Expected ['html', 'head', 'title', 'body', 'ul', 'li', 'li'], received {result} # Test 2"

    # Test 3 - correct hierarchy
    # Sample HTML content
    html_content = """
    <html>
      <head>
        <title>Sample Page</title>
      </head>
      <body>
        <h1>Welcome to the Sample Page</h1>
        <p>This is a sample HTML page.</p>
      </body>
    </html>
    """
    parser.feed(html_content)

    result = recursion_func(parser.tree)
    dct = {
        'html': {
            'head': {
                'title': 'Sample Page'
            },
            'body': {
                'h1': 'Welcome to the Sample Page',
                'p': 'This is a sample HTML page.'
            }
        }
    }
    assert result == dct, f'Expected True, received False # Test 3'


test_empty_html()
test_wrong_tags()
test_different_structures()
