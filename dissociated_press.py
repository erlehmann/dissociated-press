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

        # this list holds sentence Fragment occuring after this word
        # imagine the word being before the list
        self.nextFragment = []

        # this list holds sentence Fragment occuring before this word
        # imagine the word being after the list
        self.prevFragment = []

        # keys are possible positions in sentences
        # values are how often the word occurred
        self.positions = {}

        self.value = value

    def __repr__(self):
        return self.value + str(self.positions.keys())

    def __str__(self):
        return self.value

    def addNextFragment(self, nextWords=[]):
        """Adds Fragment following this word."""
        self.nextFragment.append(nextWords)

    def addPrevFragment(self, prevWords=[]):
        """Adds Fragment preceding this word."""
        self.prevFragment.append(prevWords)

    def getNextFragment(self, count=1):
        """Gets Fragment following this word up to a specific depth."""
        Fragment = []
        for f in self.nextFragment:
            Fragment.append(f[:count])
        return Fragment

    def getPrevFragment(self, count=1):
        """Gets Fragment preceding this word up to a specific depth."""
        Fragment = []
        for f in self.nextFragment:
            Fragment.append(f[-count:])
        return Fragment

    def getNextRandomFragment(self, count=1):
        randomFragment = choice(self.nextFragment)
        return randomFragment[:count]

    def getPrevRandomFragment(self, count=1):
        randomFragment = choice(self.prevFragment)
        return randomFragment[-count:]

    def addPosition(self, position):
        try:
            self.positions[position] += 1
        except KeyError:
            self.positions[position] = 1

    def getPositions(self):
        return self.positions

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

    def dissociate(self, string, separator=" "):
        """Dissociate a sentence into this dictionary."""
        self.sentence = string.split(separator)
        for i, token in enumerate(self.sentence):

            if token not in self.words.keys():
                w = self.words[token] = word(token)
            else:
                w = self.words[token]

            w.addNextFragment(self.sentence[i+1:])
            w.addPrevFragment(self.sentence[:i])
            w.addPosition(i)

    def associate(self, separator=" "):
        """Associate a sentence from the dictionary."""
        # TODO: depth parameter not used yet
        # we need a first word
        self.sentence = ""

        w = choice(self.getWordsAtPosition(0))
        while w:
            print w
            try:
                self.sentence += separator + w
                w = self.words[w].getNextRandomFragment()[0]
            # unclear when IndexError occurs
            except IndexError:
                return self.sentence

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
