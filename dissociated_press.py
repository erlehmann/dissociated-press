#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import choice
from sys import stdin
from time import sleep

class word:
    def __init__(self, value=""):
        self.nextWordsDict = {}
        self.positionsDict = {}
        self.value = value

    def __repr__(self):
        self.repr = ""
        self.repr += self.value + " -> "
        for w in self.getNextWords():
            self.repr +=  str(w) + " "
        self.repr += str(self.positionsDict.keys()) + "\n"
        return self.repr

    def __str__(self):
        return self.value

    def addNextWord(self, nextWord):
        """Adds to this word a possible successor."""
        if nextWord not in self.nextWordsDict:
            self.nextWordsDict[nextWord] = 1
        else:
            self.nextWordsDict[nextWord] += 1

    def getNextWords(self):
        """Gets all possible successors to this word."""
        return self.nextWordsDict.keys()

    def getNextWordsDict(self):
        """Gets a dictionary with all possible successors to this word and how often they occured as such."""
        return self.nextWordsDict

    def addPosition(self, position):
        """Adds to this word a possible position inside a sentence."""
        if position not in self.positionsDict:
            self.positionsDict[position] = 1
        else:
            self.positionsDict[position] += 1

    def getPositions(self):
        """Gets all possible positions of this Word inside a sentence."""
        return self.positionsDict.keys()

    def getPositionsDict(self):
        """Gets a dictionary with all possible positions of this Word inside a sentence and how often they occured."""
        return self.positionsDict

    def getPopularity(self):
        """Gets how popular this word is used based on popularity of positions inside a sentence."""
        popularity = 0
        for v in self.getPositionsDict().values():
            popularity += v
        return popularity

    def getValue(self):
        return self.value

class dictionary:
    def __init__(self):
        self.wordList = []

    def __repr__(self):
        self.repr = ""
        for w in self.wordList:
            self.repr += str(w).ljust(15) + " -> "
            self.repr += str(w.getPositions()).ljust(15) + " -> "
            for x in w.getNextWords():
                self.repr += str(x) + " "
            self.repr += "\n"
        return self.repr

    def __contains__(self, word):
        for w in self.wordList:
            if w.getValue() == word:
                return True
        return False

    def __getitem__(self, index):
        return self.wordList[index]

    def addWord(self, word, position=None):
        """Adds a word to the dictionary, optionally with position inside a sentence."""
        # if word is not in dictionary, add it
        if not str(word) in self:
            self.wordList.append(word)
        # if a position is given, add it
        if position != None:
            self.getWord(str(word)).addPosition(position)

    def addWordPair(self, word, nextWord, position=None):
        """Adds a word pair to the dictionary, optionally with position of the first word inside a sentence."""
        self.addWord(word, position)
        self.addWord(nextWord, position+1)
        # add nextWord to the appropriate list of word if it is not there yet
        for k in self.getWord(str(word)).getNextWords():
            if str(k) == str(nextWord):
                return
        self.getWord(str(word)).addNextWord(nextWord)

    def getWord(self, word):
        for w in self.wordList:
            if w.getValue() == word:
                return w
        return None

    def getWordList(self):
        return self.wordList

    def associate(self):
        """Create a sentence from this Dissociated Press dictionary."""
        # get a word that can stand at the beginning.
        self.startWords = []
        for w in self.wordList:
            if 0 in w.getPositions():
                self.startWords.append(w)
        self.currentWord = choice(self.startWords)
        self.sentence = str(self.currentWord)

        # add more words
        # FIXME: does not work as intended
        for i in range(self.getMaxSentenceLength())[1:]: # cut off the zeroest element
            self.addWords = []
            for w in self.getWordList():
                if w in self.currentWord.getNextWords():
                    if i in w.getPositions():
                        self.addWords.append(w)
            try:
                self.currentWord = choice(self.addWords)                
                self.sentence += " " + str(self.currentWord)
            except IndexError: # list empty, sentence ends naturally
                return self.sentence
        # longest sentence possible
        return self.sentence

    def getMaxSentenceLength(self):
        l = 0
        for w in self.wordList:
            if max(w.getPositions()) > l:
                l = max(w.getPositions())
        return l + 1

class sentence:
    def __init__(self, string):
        self.value = string.lstrip()
        self.tokenList = self.value.split(" ")

    def __repr__(self):
        repr = ""
        for t in self.tokenList:
            repr += t + " "
        return repr

    def __str__(self):
        return self.value

    def dissociate(self, dictionary):
        """Feed this sentence to a target Dissociated Press dictionary."""
        for i,t in enumerate(self.tokenList):
            try:
                currentWord = word(self.tokenList[i])
                currentNextWord = word(self.tokenList[i+1])
                dictionary.addWordPair(currentWord, currentNextWord, position=i)
            except IndexError:
                dictionary.addWord(currentWord, position=i)
                print "Sentence dissociated."
                pass

    def isWellFormed(self):
        s = self.value
        if s.count("(") == s.count(")"):
            return True
        return False
    

if __name__ == '__main__':
    dict = dictionary()
    while 1:
        s = stdin.readline()
        if s == "": break
        s = s[:-1] + " " # cut of the last char "\n", insert space
        for t in s.split(". "): # ugly hack
            sentence(t).dissociate(dict)
        #p = sentence(s[:-1]) # cut of the last char "\n"
        #p.dissociate(dict)
    print "=== Dissociated Press ==="
    try:
        while 1:
            print dict.associate()
            sleep(1)
    except KeyboardInterrupt:
        print "=== Enough! ==="
