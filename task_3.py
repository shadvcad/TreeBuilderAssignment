from additionalModule import HTMLTreeBuilder
from collections import defaultdict


# The function converts a HTMLTreeBuilder object into a dictionary;
# if the tags have the same names, the function will add numbers to the tag name
def html_tree_to_dict(tree: HTMLTreeBuilder) -> dict:
    # Type checking
    if not isinstance(tree, HTMLTreeBuilder):
        raise TypeError("The node must be a HTMLTreeBuilder type")

    def recursion_func(node, tag=None) -> dict:
        result_data = defaultdict(dict)

        if node:
            if tag is None:
                tag = node.tag

            if node.children:
                for child in node.children:
                    existing_tags = result_data[tag].get(child.tag)
                    if existing_tags is None:
                        result_data[tag].update(recursion_func(child, None))
                    else:
                        new_tag = f'{child.tag}_{len(result_data.get(node.tag) or existing_tags)}'
                        result_data[tag].update(recursion_func(child, new_tag))
            if node.data:
                result_data[tag]['data'] = node.data.strip()

        return result_data
    return recursion_func(tree.tree)


# Create an instance of the HTMLTreeBuilder
parser = HTMLTreeBuilder()


# Test cases
def test_empty_html():
    # Sample HTML content
    html_content = """
    """
    parser.feed(html_content)
    result = html_tree_to_dict(parser)
    assert result == dict(), f'Expected empty dictionary, received {result}'


def test_different_structures():
    # Test 1
    # Sample HTML content
    html_content = """
    <html>
      <head>
        <title>Sample Page<h2>Welcome to the Sample Page<p1>This is a sample HTML page.</p1></h2></title>
      </head>
      <body>
        <h1>Welcome to the Sample Page</h1>
        <p>This is a sample HTML page.</p>
      </body>
    </html>
    """
    parser.feed(html_content)
    dct = {
        "html": {
            "head": {
                "title": {
                    "data": "Sample Page",
                    "h2": {
                        "data": "Welcome to the Sample Page",
                        "p1": {
                            "data": "This is a sample HTML page."
                        }
                    }
                }
            },
            "body": {
                "h1": {
                    "data": "Welcome to the Sample Page"
                },
                "p": {
                    "data": "This is a sample HTML page."
                }
            }
        }
    }

    result = html_tree_to_dict(parser)
    assert result == dct, f'Expected True, received False # Test 1'

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
    dct = {
        "div": {
            "h2": {
                "data": "Main Header"
            },
            "ul": {
                "li": {
                    "data": "List Item 1"
                },
                "li_1": {
                    "data": "List Item 2"
                }
            }
        }
    }

    result = html_tree_to_dict(parser)
    assert result == dct, f'Expected True, received False # Test 2'

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
    dct = {
        "table": {
            "tr": {
                "th": {
                    "data": "Name"
                },
                "th_1": {
                    "data": "Age"
                }
            },
            "tr_1": {
                "td": {
                    "data": "John"
                },
                "td_1": {
                    "data": "30"
                }
            }
        }
    }

    result = html_tree_to_dict(parser)
    assert result == dct, f'Expected True, received False # Test 3'

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
    dct = {
        "html": {
            "head": {
                "title": {
                    "data": "Sample Page"
                }
            },
            "body": {
                "header": {
                    "h1": {
                        "data": "Welcome to the Sample Page"
                    }
                },
                "section": {
                    "div": {
                        "p": {
                            "data": "This is a sample HTML page."
                        },
                        "ul": {
                            "li": {
                                "data": "Item 1"
                            },
                            "li_1": {
                                "data": "Item 2"
                            }
                        }
                    },
                    "footer": {
                        "p": {
                            "data": "Any content"
                        }
                    }
                }
            }
        }
    }

    result = html_tree_to_dict(parser)
    assert result == dct, f'Expected True, received False # Test 4'

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
    dct = {
        "div": {
            "h2": {
                "data": "Main Header"
            },
            "ul": {
                "li": {
                    "data": "List Item 1"
                },
                "li_1": {
                    "data": "List Item 2"
                }
            },
            "nav": {
                "ul": {
                    "li": {
                        "a": {
                            "data": "Home"
                        }
                    },
                    "li_1": {
                        "a": {
                            "data": "About"
                        }
                    },
                    "li_2": {
                        "a": {
                            "data": "Contact"
                        }
                    }
                }
            }
        }
    }

    result = html_tree_to_dict(parser)
    assert result == dct, f'Expected True, received False # Test 5'

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
          <p>Some content.</p>
        </footer>
      </body>
    </html>
    """
    parser.feed(html_content)
    dct = {
        "html": {
            "head": {
                "title": {
                    "data": "Extended Table"
                },
                "style": {
                    "data": "Some content"
                }
            },
            "body": {
                "header": {
                    "h1": {
                        "data": "Employee Information"
                    }
                },
                "section": {
                    "table": {
                        "thead": {
                            "tr": {
                                "th": {
                                    "data": "Name"
                                },
                                "th_1": {
                                    "data": "Age"
                                }
                            }
                        },
                        "tbody": {
                            "tr": {
                                "td": {
                                    "data": "John"
                                },
                                "td_1": {
                                    "data": "30"
                                }
                            },
                            "tr_1": {
                                "td": {
                                    "data": "Jane"
                                },
                                "td_1": {
                                    "data": "25"
                                }
                            },
                            "tr_2": {
                                "td": {
                                    "data": "Dmitriy"
                                },
                                "td_1": {
                                    "data": "32"
                                }
                            }
                        }
                    }
                },
                "footer": {
                    "p": {
                        "data": "Some content."
                    }
                }
            }
        }
    }

    result = html_tree_to_dict(parser)
    assert result == dct, f'Expected True, received False # Test 6'


test_empty_html()
test_different_structures()