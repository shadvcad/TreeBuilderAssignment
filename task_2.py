from additionalModule import HTMLTreeBuilder


# The function searches for a given tag and all its children, returns a list with all tags
def find_elements_by_tag(tree: HTMLTreeBuilder, tag: str) -> list:
    # Type checking
    if not isinstance(tree, HTMLTreeBuilder):
        raise TypeError("The node must be a HTMLTreeBuilder type")
    if not isinstance(tag, str):
        raise TypeError("The tag must be a string type.")

    def recursion_func(node, tag_to_find: str, result=None) -> list:
        if result is None:
            result = []

        if node:
            if node.tag == tag_to_find:
                result.append(node.tag)
                for child in node.children:
                    recursion_func(child, child.tag, result)
            for child in node.children:
                recursion_func(child, tag_to_find, result)

        return result

    return recursion_func(tree.tree, tag)


# Create an instance of the HTMLTreeBuilder
parser = HTMLTreeBuilder()


# Test cases
def test_empty_html():
    # Sample HTML content
    html_content = """
    """
    parser.feed(html_content)
    result = find_elements_by_tag(parser, 'html')
    assert result == [], f"Expected [], received {result}"


def test_different_structures():
    # Test 1
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
    result = find_elements_by_tag(parser, 'html')
    assert result == ['html', 'head', 'title', 'body', 'h1', 'p'], \
        f"Expected ['html', 'head', 'title', 'body', 'h1', 'p'], received {result}"

    # Test 2
    # Sample HTML content
    html_content = """
    <div id="container">
      <h2 class="header">Main Header</h2>
      <ul>
        <li>List Item 1</li>
        <li>List Item 2</li>
      </ul>
    </div>
    """
    parser.feed(html_content)
    result = find_elements_by_tag(parser, 'div')
    assert result == ['div', 'h2', 'ul', 'li', 'li'], \
        f"Expected ['div', 'h2', 'ul', 'li', 'li'], received {result}"

    # Test 3
    # Sample HTML content
    html_content = """
    <table>
      <tr>
        <th>Name</th>
        <th>Age</th>
      </tr>
      <tr>
        <td>John</td>
        <td>30</td>
      </tr>
    </table>
    """
    parser.feed(html_content)
    result = find_elements_by_tag(parser, 'table')
    assert result == ['table', 'tr', 'th', 'th', 'tr', 'td', 'td'], \
        f"Expected ['table', 'tr', 'th', 'th', 'tr', 'td', 'td'], received {result}"

    # Test 4
    # Sample HTML content
    html_content = """
    <html>
     <head>
       <title>Sample Page</title>
     </head>
     <body>
       <header>
         <h1>Welcome to the Sample Page</h1>
       </header>
       <section>
         <div>
           <p>This is a sample HTML page.</p>
           <ul>
             <li>Item 1</li>
             <li>Item 2</li>
           </ul>
         </div>
         <footer>
           <p>Any content</p>
         </footer>
       </section>
     </body>
    </html>
    """
    parser.feed(html_content)
    result = find_elements_by_tag(parser, 'body')
    assert result == ['body', 'header', 'h1', 'section', 'div', 'p', 'ul', 'li', 'li', 'footer', 'p'], \
        f"Expected ['body', 'header', 'h1', 'section', 'div', 'p', 'ul', 'li', 'li', 'footer', 'p'], received {result}"

    # Test 5
    # Sample HTML content
    html_content = """
    <div id="container">
      <h2 class="header">Main Header</h2>
      <ul>
        <li>List Item 1</li>
        <li>List Item 2</li>
      </ul>
      <nav>
        <ul>
          <li><a href="#">Home</a></li>
          <li><a href="#">About</a></li>
          <li><a href="#">Contact</a></li>
        </ul>
      </nav>
    </div>
    """
    parser.feed(html_content)
    result = find_elements_by_tag(parser, 'ul')
    assert result == ['ul', 'li', 'li', 'ul', 'li', 'a', 'li', 'a', 'li', 'a'], \
        f"Expected ['ul', 'li', 'li', 'ul', 'li', 'a', 'li', 'a', 'li', 'a'], received {result}"

    # Test 6
    # Sample HTML content
    html_content = """
    <html lang="en">
      <head>
        <title>Extended Table</title>
        <style>
          Some content
        </style>
      </head>
      <body>
        <header>
          <h1>Employee Information</h1>
        </header>
        <section>
          <table>
            <thead>
              <tr>
                <th>Name</th>
                <th>Age</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>John</td>
                <td>30</td>
              </tr>
              <tr>
                <td>Jane</td>
                <td>25</td>
              </tr>
              <tr>
                <td>Dmitriy</td>
                <td>32</td>
              </tr>
            </tbody>
          </table>
        </section>
        <footer>
          <p>&copy; Some content.</p>
        </footer>
      </body>
    </html>
    """
    parser.feed(html_content)
    result = find_elements_by_tag(parser, 'tr')
    assert result == ['tr', 'th', 'th', 'tr', 'td', 'td', 'tr', 'td', 'td', 'tr', 'td', 'td'], \
        f"Expected ['tr', 'th', 'th', 'tr', 'td', 'td', 'tr', 'td', 'td', 'tr', 'td', 'td'], received {result}"


test_empty_html()
test_different_structures()
