# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.

    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
    """
    
    if count >= 10:
        print "Number of donuts: many"
    elif count < 0:
        print "Number of donuts can't be negative!"
    else:
        print "Number of donuts: " + count
        
    """raise NotImplementedError"""


def both_ends(s):
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.

    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """
    num_chars = len(s)
    
    if num_chars <= 1:
        print "String should have more than 1 character!"
    else:    
        start = s[0:2]
        end = s[numchars-2:numchars]
        print start + end

    ### raise NotImplementedError ###


def fix_start(s):
    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.

    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    """
    
    numchar = len(s)
    
    if numchar <=1:
        print "String must have more than 1 character!"
    else:
        firstchar = s[0]
        b = s.replace(firstchar,"*")
        newword = firstchar + b[1:numchar]
        print newword

def mix_up(a, b):
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
    numcharsa = len(a)
    numcharsb = len(b)

    if numcharsa < 2 or numcharsb < 2:
        print "Strings should have 2 or more characters!"
    else:
        auxiliar = a
        first = b[0:2] + a[2:numcharsa]
        secon = a[0:2] + b[2:numcharsb]
    
    print first + " " + secon



def verbing(s):
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """
    
    numchars = len(s)
    
    ending = s[numchars-3:numchars]
    
    if numchars < 3:
        print "String must have at least 3 characters!"
    elif ending == "ing":
        s = s + "ly"
    else:
        s = s + "ing"
        
    return s    


def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """
    
    startnot = s.find("not")
    startbad = s.find("bad")

    
    if startnot != -1 and startbad != -1 and startnot < startbad:
        auxiliar = s[0:startnot] + "good"
        s = auxiliar
            
    return s


def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
    
    alen = len(a)
    blen = len(b)
    
    if alen == 0 or blen == 0:
        print "Both strings should have more than 0 characters"
    else:    
        if alen%2 == 0:
           aendfirsthalf = (alen / 2)
           afirsthalf = a[0:aendfirsthalf]
        else:
            aendfirsthalf = (alen / 2)
            afirsthalf = a[0:aendfirsthalf+1]
            
        if blen%2 == 0:
            bendfirsthalf = (blen / 2)
            bfirsthalf = b[0:bendfirsthalf]
        else:
            bendfirsthalf = (blen / 2)
            bfirsthalf = b[0:bendfirsthalf+1]


        aseconhalf = a[aendfirsthalf:alen]
        bseconhalf = b[bendfirsthalf:blen]

         
        newstring = afirsthalf + bfirsthalf + aseconhalf + bseconhalf
        
    return newstring


    
    ### raise NotImplementedError ###
