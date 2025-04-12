import textnode

def main():
    obj = textnode.TextNode("Hello world", textnode.TextType.LINK, "https://www.static.site")
    print(obj)

main()