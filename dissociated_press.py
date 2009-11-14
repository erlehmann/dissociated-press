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

    def addNextFragment(self, nextWord):
        """Adds Fragment following this word."""
        self.nextFragments.append(nextWord)

    def addPrevFragment(self, prevWord):
        """Adds Fragment preceding this word."""
        self.prevFragments.append(prevWord)

    def getNextFragments(self):
        """Gets all Fragments following this word."""
        return self.nextFragments

    def getPrevFragments(self):
        """Gets Fragments preceding this word."""
        return self.prevFragments

    def getNextRandomFragment(self):
        randomFragment = choice(self.nextFragments)
        return randomFragment

    def getPrevRandomFragment(self):
        randomFragment = choice(self.prevFragments)
        return randomFragment

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

        sentence = string.split(separator)

        for i, token in enumerate(sentence):

            if token not in self.words.keys():
                w = self.words[token] = word(token)
            else:
                w = self.words[token]

            print sentence[i], i

            try:
                print sentence[i-1]
            except IndexError:
                print "LOL ERROR"

            try:
                print sentence[i+1]
            except IndexError:
                print "LOL ERROR"

            # w.addNextFragment(sentence[i+1])

            # w.addPrevFragment(sentence[i-1])

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
