class LeftParagraph:

    def __init__(self, length):
        self.d = list()
        self.length = length

    def add_word(self, word):
        if self.d and len(' '.join(self.d[-1])) + len(word) < self.length:
            self.d[-1].append(word)
        else:
            self.d.append([word])

    def end(self):
        for i in range(len(self.d)):
            self.d[i] = ' '.join(self.d[i])
        print(*self.d, sep='\n')
        self.d = list()


class RightParagraph:

    def __init__(self, length):
        self.d = list()
        self.length = length

    def add_word(self, word):
        if self.d and len(' '.join(self.d[-1])) + len(word) < self.length:
            self.d[-1].append(word)
        else:
            self.d.append([word])

    def end(self):
        for i in range(len(self.d)):
            self.d[i] = ' ' * (self.length - len(' '.join(self.d[i]))) + ' '.join(self.d[i])
        print(*self.d, sep='\n')
        self.d = list()
