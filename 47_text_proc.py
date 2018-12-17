class TextProc:
    """ Implements wc and grep for a file

    """
    # No. of file objects
    count_file = 0

    def __init__(self, fname):
        TextProc.count_file += 1
        # name
        self.name = fname
        # handle for the file
        self.fh = open(fname)
        self.line_string = self.fh.readlines()
        self.nlines = len(self.line_string)
        self.nwords = 0  # number of words
        self.wordcount()

    def wordcount(self):
        """ Finds the number of words in the file.

        """
        for line in self.line_string:
            words = line.split()
            self.nwords += len(words)

    def grep(self, target):
        """ Grep the target word

        """
        # print(self.line_string)
        for line in self.line_string:
            # find returns the index where substring is found, -1 if not found
            if line.find(target) != -1:
                print(line)


if __name__ == "__main__":
    """ Create objects of TextProc
    
    """
    my_text_proc = TextProc("19_keyword_args.py")
    print("The number of text files open is", TextProc.count_file, "\n")

    print("Details : name, no. of lines, no. of words \n")
    print(my_text_proc.name, my_text_proc.nlines, my_text_proc.nwords, "\n")

    print("grep 'mode' in file1.txt: \n")
    print(my_text_proc.grep('mode'))

