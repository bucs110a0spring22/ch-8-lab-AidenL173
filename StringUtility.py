class StringUtility: 
  def __init__(self, string):
    self.string = string
    

  def __str__(self):
    return self.string 

  def vowels(self):
    vowels = "aeiouAEIOU"
    count = 0
    for character in self.string:
      if character in vowels:
        count = count + 1
    if count >= 5:
      return "many"
    return str(count)

  def bothEnds(self):
    string = self.string
    if len(string) <= 2:
      return ""
    return string[0] + string[1] + string[-2] + string[-1]

  def fixStart(self):
    string = self.string
    if len(string) <= 1:
      return string
    return string[0] + string[1:].replace(string[0], "*")

  def asciiSum(self):
    ascii = 0
    for character in self.string:
      ascii = ord(character) + ascii
    return int(ascii)

  def cipher(self): 