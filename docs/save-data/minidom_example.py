import xml.dom.minidom as minidom


def getTitles(xml):
    """
    Print all titles found in books.xml
    """
    doc = minidom.parse(xml)
    node = doc.documentElement
    books = doc.getElementsByTagName("book")

    titles = []
    for book in books:
        titleObj = book.getElementsByTagName("title")[0]
        titles.append(titleObj)

    for title in titles:
        nodes = title.childNodes
        for node in nodes:
            if node.nodeType == node.TEXT_NODE:
                print(node.data)


if __name__ == "__main__":
    document = "books.xml"
    getTitles(document)
