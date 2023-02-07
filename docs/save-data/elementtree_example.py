import xml.etree.cElementTree as ET


def parseXML(xml_file):
    """
    Parse XML with ElementTree
    """
    tree = ET.ElementTree(file=xml_file)
    print(tree.getroot())
    root = tree.getroot()
    print(f"tag={root.tag}, attrib={root.attrib}")

    for child in root:
        print(child.tag, child.attrib)
        if child.tag == "book":
            for step_child in child:
                print(step_child.tag)

    # get the information via the children!
    print("-" * 20)
    print("Iterating using iter")
    print("-" * 20)
    books = root.iter()
    for book in books:
        book_children = book.iter()
        for book_child in book_children:
            print(f"{book_child.tag}={book_child.text}")


if __name__ == "__main__":
    parseXML("books.xml")
