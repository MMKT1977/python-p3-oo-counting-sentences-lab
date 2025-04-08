#!/usr/bin/env python3

class MyString:
  def __init__(self, value =""):
    self.value= value

  @property
  def value(self):
    return self._value

  @value.setter
  def value(self, new_value):
    if not isinstance(new_value, str):
      print("The value must be a string.")
      return
    self._value = new_value

  def is_sentence(self):
    return self._value.endswith(".")
  
  def is_question(self):
    return self._value.endswith("?")
  
  def is_exclamation(self):
    return self._value.endswith("!")
  
  def count_sentences(self):
    if not self.value.split():
      return 0
    sentence = self.value.replace("!",".").replace("?",".")
    potential_sentences = sentence.split(".")
    return len([s for s in potential_sentences if s.strip()])
  


my_string = MyString()
print(f"Initial value: '{my_string.value}'") 

my_string.value = "This, well, is a sentence. This is too!! And so is this, I think? Woo..."
print(f"String is: '{my_string.value}'")
print(my_string.is_sentence())
print(my_string.is_exclamation())
print(my_string.is_question())
print(my_string.count_sentences())
    
