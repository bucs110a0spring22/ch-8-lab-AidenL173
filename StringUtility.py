class StringUtility: 
  def __init__(self, string):
    '''
    takes a string as a parameter and stores it as an instance variable
    self: str, inputted string
    '''
    self.string = string
    
  def __str__(self):
    '''
    returns the internal string itself, unchanged
    self: str, inputted string
    return: str, returns the string
    '''
    return self.string 

  def vowels(self):
    '''
    counts amount of vowels
    self: str, inputted string
    return: str, returns the amount of vowels if it's less than 5, otherwise returns "many"
    '''
    return str(len([vowel for vowel in self.string if vowel in "aeiouAEIOU"])) if len([vowel for vowel in self.string if vowel in "aeiouAEIOU"]) < 5 else "many"

  def bothEnds(self):
    '''
    returns a string made of the first 2 and last 2 chars of the original string unless its lengths <= 2
    self: str, inputted string
    returns: str, returns first and last 2 chars of string if it's length is over 2, otherwise returns an empty string
    '''
    return self.string[0] + self.string[1] + self.string[-2] + self.string[-1] if len(self.string) > 2 else ""

  def fixStart(self):
    '''
    returns a string where all occurrences of its first char have been changed to '*', except the first char itself.
    self: str, inputted string
    return: str, returns the changed string if length is over 1, otherwise returns original string
    ''' 
    return self.string[0] + self.string[1:].replace(self.string[0], "*") if len(self.string) > 1 else self.string

  def asciiSum(self):
    '''
    returns an integer that is the sum of all ascii values in the string
    self: str, inputted string
    returns: int, returns the combined ascii values of all characters in the string.
    '''
    return sum([ord(character) for character in self.string])

  def cipher(self):
    '''
    returns an encoded string by incrementing all letters by the length of the string (accounts for wrap arounds).
    self: str, inputted string
    returns: str, returns the encrypted letters of the string
    '''
    return (''.join([chr(((ord(character) + len(self.string) - 97) % 26) + 97) if character in "abcdefghijklmnopqrstuvwxyz" else chr(((ord(character) + len(self.string) - 65) % 26) + 65) if character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" else character for character in self.string]))