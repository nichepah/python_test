import urllib.request

if __name__ == "__main__":
    """ Count number of links in a webpage.

    """
    page = urllib.request.urlopen('https://en.wikipedia.org/wiki/Richard_Stallman')
    page_src = page.read()
    # print(page_src)
    src_words = [l.decode('utf-8') for l in page_src.split()]
    # print(src_words)
    result = list()
    for word in src_words:
        # print(type(word), word)
        if word.startswith('href=\"http://'):
            result.append(word)

    print(len(result), result)
