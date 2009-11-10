#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import choice
from sys import stdin
from time import sleep

class word:
    def __init__(self, value=""):
        """
        A word saves what precedes and what follows itself.
        It also knows its position inside a sentence.
        """

        # this list holds sentence fragments occuring after this word
        # imagine the word being before the list
        self.nextFragments = []

        # this list holds sentence fragments occuring before this word
        # imagine the word being after the list
        self.prevFragments = []

        # keys are possible positions in sentences
        # values are how often the word occurred
        self.positions = {}

        self.value = value

    def __repr__(self):
        return self.value + str(self.positions.keys())

    def __str__(self):
        return self.value

    def addNextFragments(self, nextWords=[]):
        """Adds fragments following this word."""
        self.nextFragments.append(nextWords)

    def addPrevFragments(self, prevWords=[]):
        """Adds fragments preceding this word."""
        self.prevFragments.append(prevWords)

    def getNextFragments(self, count=1):
        """Gets Fragments following this word up to a specific depth."""
        fragments = []
        for f in self.nextFragments:
            fragments.append(f[:count])
        return fragments

    def getPrevFragments(self, count=1):
        """Gets Fragments preceding this word up to a specific depth."""
        fragments = []
        for f in self.nextFragments:
            fragments.append(f[-count:])
        return fragments

    def getNextRandomFragment(self, count=1):
        randomFragment = choice(self.nextFragments)
        return randomFragment[:count]

    def getPrevRandomFragment(self, count=1):
        randomFragment = choice(self.prevFragments)
        return randomFragment[-count:]

    def addPosition(self, position):
        try:
            self.positions[position] += 1
        except KeyError:
            self.positions[position] = 1

    def getPositions(self):
        return self.positions

class sentence:
    def __init__(self, string, separator=" "):
        """A sentence is basically a glorified list of tokens."""
        self.value = string
        self.separator = separator
        self.tokens = self.value.split(self.separator)

    def __repr__(self):
        repr = ""
        for t in self.tokens[:-1]:
            repr += t + self.separator
        # the last element does not need to be followed by a separator
        repr += self.tokens[-1]
        return repr

    def __str__(self):
        return self.value

    # sentences are iterable
    def __getitem__(self, index):
        return self.tokens[index]

    def __len__(self):
        return len(self.tokens)

class dictionary:
    def __init__(self):
        """
        A Dissociated Press dictionary contains a python dictionary of words.
        Sentences can be associated into or out of it.
        """
        self.words = {}

    def __repr__(self):
        return str(self.words)

    def __getitem__(self, key):
        return self.words[key]

    def getWordsAtPosition(self, position):
        """Get all words that may occur at one position."""
        wordsAtPosition = []
        for w in self.words:
            if position in self.words[w].getPositions().keys():
                wordsAtPosition.append(w)
        return wordsAtPosition

    def dissociate(self, sentence):
        """Dissociate a sentence into this dictionary."""
        for i, token in enumerate(sentence):

            if token not in self.words.keys():
                w = self.words[token] = word(token)
            else:
                w = self.words[token]

            w.addNextFragments(sentence[i+1:])
            w.addPrevFragments(sentence[:i])
            w.addPosition(i)

    def associate(self, depth=1, separator=" "):
        """Associate a sentence from the dictionary."""
        # TODO: depth parameter not used yet
        # we need a first word
        blurb = ""

        w = choice(self.getWordsAtPosition(0))
        while w:
            print w
            try:
                blurb += separator + w
                w = self.words[w].getNextRandomFragment()[0]
            # unclear when IndexError occurs
            except IndexError:
                return blurb

#if __name__ == '__main__':
    #dict = dictionary()
    #while 1:
        #s = stdin.readline()
        #if s == "": break
        #s = s[:-1] + " " # cut of the last char "\n", insert space
        #for t in s.split(". "): # ugly hack
            #sentence(t).dissociate(dict)
        ##p = sentence(s[:-1]) # cut of the last char "\n"
        ##p.dissociate(dict)
    #print "=== Dissociated Press ==="
    #try:
        #while 1:
            #print dict.associate()
            #sleep(1)
    #except KeyboardInterrupt:
        #print "=== Enough! ==="
