from additionalModule import HTMLTreeBuilder

# Example Usage
if __name__ == "__main__":
    # Create an instance of the HTMLTreeBuilder
    parser = HTMLTreeBuilder()

    # Sample HTML content
    html_content = """
    <html>
      <body>
        <h1>Main Header</h1>
        <p>Sample paragraph.</p>
      </body>
    </html>
    """

    # Manually call the feed method
    parser.feed(html_content)

    # Get the resulting tree
    tree = parser.tree

    # Function to print the tree structure
    def print_tree(node, indent=""):
        if node:
            print(indent + node.tag)
            if node.data:
                print(indent + "  Data: " + node.data)
            for child in node.children:
                print_tree(child, indent + "  ")

    # Print the HTML tree structure
    print_tree(tree)
