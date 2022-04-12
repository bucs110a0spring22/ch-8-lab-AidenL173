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
    vowels = "aeiouAEIOU"
    count = 0
    for character in self.string:
      if character in vowels:
        count = count + 1
    if count >= 5:
      return "many"
    return str(count)

  def bothEnds(self):
    '''
    returns a string made of the first 2 and last 2 chars of the original string unless its lengths <= 2
    self: str, inputted string
    returns: str, returns first and last 2 chars of string if it's length is over 2, otherwise returns an empty string
    '''
    string = self.string
    if len(string) <= 2:
      return ""
    return string[0] + string[1] + string[-2] + string[-1]

  def fixStart(self):
    '''
    returns a string where all occurrences of its first char have been changed to '*', except the first char itself.
    self: str, inputted string
    return: str, returns the changed string if length is over 1, otherwise returns original string
    '''
    string = self.string
    if len(string) <= 1:
      return string
    return string[0] + string[1:].replace(string[0], "*")

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
    ciphered = ""
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    space = " "
    for character in self.string:
      if character in uppercase:
        changedcharacter = chr(((ord(character) + len(self.string) - 65) % 26) + 65)
        ciphered = ciphered + changedcharacter
      if character in lowercase: 
        changedcharacter = chr(((ord(character) + len(self.string) - 97) % 26) + 97)
        ciphered = ciphered + changedcharacter
      if character in space: 
        ciphered = ciphered + character
    return ciphered