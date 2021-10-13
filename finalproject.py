# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 08:49:17 2019

@author: john
"""
"""I've marked sections of code that I wrote by saying 'my own work' throughout"""


import math


"""my own work"""
def stem(s):
    """helper function that determines stems of words"""
    if s[-3:] == 'ing':
        if len(s) < 5:
            return s
        elif s[-4] == s[-5]:
            s = s[:-4]
        else:
            s = s[:-3]
    elif s[-2:] == 'er':
        if len(s) < 4:
            return s
        elif s[-3] == s[-4]:
            s = s[:-3]
        else:
            s = s[:-2]
    elif s[-3:] == 'ish':
        s = s[:-3]
    elif s[-1] == 'y':
        s = s[:-1] + 'i'
    elif s[-3:] == 'ies':
        s = s[:-2]
    elif s[-2:] == 'ed':
        if len(s) < 4:
            return s
        elif s[-3] == s[-4]:
            s = s[:-3]
        else:
            s = s[:-2]
    elif s[-2:] == "'s":
        s = s[:-2]  
    elif s[-1] == 'e':
        if len(s) < 3:
            return s
        elif s[-1] == s[-2]:
            return s
        else:
            s = s[:-1]
    elif len(s) > 3 and s[-1] == s[-2]:
        s = s[:-1]
    elif s[-1] == 's':
        s = s[:-1]
        
    return s
    
        
            


def clean_text(txt):
    """my own work"""
    """helper function which 'cleanses' a body of text of certain elements"""     
    for n in txt:
        if n in '.,?!"':
            txt = txt.replace(n, '')
            txtlist = txt.lower().split(' ')
        
    return txtlist

class TextModel:
    """first two functions are template"""
    def __init__(self, model_name):
        self.name = model_name
        self.words = {}
        self.word_lengths = {}
        self.stems = {}
        self.sentence_lengths = {}
        self.punctuation = {}
        
    def __repr__(self):
        s = 'text model name: ' + self.name + '\n'
        s += '  number of words: ' + str(len(self.words)) + '\n'
        s += '  number of word lengths: ' + str(len(self.word_lengths)) + '\n'
        s += '  number of stems: ' + str(len(self.stems)) + '\n'
        s += '  number of sentence lengths: ' + str(len(self.sentence_lengths)) + '\n'
        s += '  total punctuation: ' + str(len(self.punctuation)) + '\n'
        return s        


    """my own work"""
    def add_string(self, s):
       """Analyzes the string txt and adds its pieces
       to all of the dictionaries in this text model.
       """
       word_list = clean_text(s)
       c = 1
       
       for w in word_list:
           if w not in self.words:
               self.words[w] = 1
           else:
               self.words[w] += 1
           if len(w) not in self.word_lengths:
               self.word_lengths[len(w)] = 1
           else:
               self.word_lengths[len(w)] = self.word_lengths[len(w)] + 1
        
       for w in word_list:
           if stem(w) not in self.stems:
                self.stems[stem(w)] = 1
           else:
                self.stems[stem(w)] += 1
                
       for w in range(len(s)):
           if s[w] == ' ':
               if s[w-1] != ':':
                   c += 1
           elif s[w] in '.?!':
               if c not in self.sentence_lengths:
                   self.sentence_lengths[c] = 1
               else:
                   self.sentence_lengths[c] += 1
               c = 0
               
       for w in range(len(s)):
           if s[w] in '.,?!"()':
               if s[w] not in self.punctuation:
                   self.punctuation[s[w]] = 1
               else:
                   self.punctuation[s[w]] += 1
            
    """template"""       
    def add_file(self, filename):
        """adds a file of text to the object"""
        f = open(filename, 'r', encoding='utf8', errors='ignore')
        text = f.read()
        self.add_string(text)
        
    """my own work"""    
    def save_model(self):
        """saves the model object and its dictionaries"""
        wordfile1 = self.name + '_words'
        d = self.words   # Create a sample dictionary.
        f = open(wordfile1, 'w')      # Open file for writing.
        f.write(str(d))              # Writes the dictionary to the file.
        f.close()
        
        wordfile2 = self.name + '_word_lengths'
        d1 = self.word_lengths
        f = open(wordfile2, 'w')
        f.write(str(d1))
        f.close()
        
        wordfile3 = self.name + '_stems'
        d2 = self.stems
        f = open(wordfile3, 'w')
        f.write(str(d2))
        f.close()
        
        wordfile4 = self.name + '_sentence_lengths'
        d3 = self.sentence_lengths
        f = open(wordfile4, 'w')
        f.write(str(d3))
        f.close()
        
        wordfile5 = self.name + '_punctuation'
        d4 = self.punctuation
        f = open(wordfile5, 'w')
        f.write(str(d4))
        f.close()
    """my own work"""    
    def read_model(self):
        """opens up the model object and its dictionaries"""
        filename = self.name + '_words'
        f = open(filename, 'r')
        d_str = f.read()
        f.close()        
        d = dict(eval(d_str))
        self.words = d
        
        filename2 = self.name + '_word_lengths'
        f1 = open(filename2, 'r')
        d1_str = f1.read()
        f1.close()
        d1 = dict(eval(d1_str))
        self.word_lengths = d1
        
        filename3 = self.name + '_stems'
        f2 = open(filename3, 'r')
        d2_str = f2.read()
        f2.close()
        d2 = dict(eval(d2_str))
        self.stems = d2
        
        filename4 = self.name + '_sentence_lengths'
        f4 = open(filename4, 'r')
        d4_str = f4.read()
        f4.close()
        d4 = dict(eval(d4_str))
        self.sentence_lengths = d4
        
        filename5 = self.name + '_punctuation'
        f5 = open(filename5, 'r')
        d5_str = f5.read()
        f5.close()
        d5 = dict(eval(d5_str))
        self.punctuation = d5


        
    """my own work"""  
    def similarity_scores(self, other):
        """creates a list of similarity scores between the model object and some 
        other object"""
        thislst = []
        thislst += [compare_dictionaries(other.words, self.words)]
        thislst += [compare_dictionaries(other.word_lengths, self.word_lengths)]
        thislst += [compare_dictionaries(other.stems, self.stems)]
        thislst += [compare_dictionaries(other.sentence_lengths, self.sentence_lengths)]
        thislst += [compare_dictionaries(other.punctuation, self.punctuation)]
        return thislst


    """my own work"""  
    def classify(self, source1, source2):
        scores1 = self.similarity_scores(source1)
        scores2 = self.similarity_scores(source2)
        
        print('scores for TOS: ', scores1)
        print('scores for TNG: ', scores2)
        
        s1c = 0
        s2c = 0
        for w in range(len(scores1)):
            if scores1[w] > scores2[w]:
                s1c += 1
            else:
                s2c += 1
        
        if s1c > s2c:
            print(self.name, 'is more likely to be a TOS episode than a TNG episode.')
        else:
            print(self.name, 'is more likely to be a TNG episode than a TOS episode.')



"""my own work"""  
def compare_dictionaries(d1, d2):
    """compares two given dictionaries d1 and d2"""
    s_score = 0
    total = 0
    for key in d1:
        total += d1[key]
    for key in d2:
        if key in d1:
            s_score += (d2[key]*math.log(d1[key]/total))
        else:
            s_score += (d2[key]*math.log(0.5/total))
  
    return s_score



"""tests I wrote and ran when originally submitting"""  
"""
def run_tests():
    official test code for the four files I have chosen
    source1 = TextModel('Corbomite Maneuver')
    source1.add_file('CorbomiteManeuver.txt')

    source2 = TextModel('Darmok')
    source2.add_file('Darmok.txt')

    new1 = TextModel('Power Play')
    new1.add_file('Power Play.txt')
    new1.classify(source1, source2)
    
    new2 = TextModel('Duet')
    new2.add_file('Duet.txt')
    new2.classify(source1, source2)
    
    new3 = TextModel('The City On The Edge Of Forever')
    new3.add_file('CityOnTheEdgeOfForever.txt')
    new3.classify(source1, source2)
    
    new4 = TextModel('Imperfection')
    new4.add_file('Imperfection.txt')
    new4.classify(source1, source2)
    
    new5 = TextModel('Ensign Ro')
    new5.add_file('Ensign Ro.txt')
    new5.classify(source1, source2)
"""
    
    
