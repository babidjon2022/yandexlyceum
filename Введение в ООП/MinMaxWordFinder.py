class MinMaxWordFinder():

    def __init__(self):
        self.s = str()

    def add_sentence(self, s):
        self.s += s + ' '

    def shortest_words(self):
        if not self.s.strip():
            return ''
        d = dict()
        for i in self.s.split():
            if len(i) not in d:
                d[len(i)] = [i]
            else:
                d[len(i)].append(i)
        return sorted(d[min(d.keys())])

    def longest_words(self):
        if not self.s.strip():
            return ''
        d = dict()
        for i in self.s.split():
            if len(i) not in d:
                d[len(i)] = {i}
            else:
                d[len(i)].add(i)
        return sorted(d[max(d.keys())])
