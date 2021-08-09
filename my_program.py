
def sentence_maker(phrase):
  interrogatives = ("how", "what", "why")
  capitalized = phrase.capitalize()
 #if phrase.startswith(("how", "what", "why"))
  if phrase.startswith(interrogatives):
    return "{}?".format(capitalized)
    #this will capitalize the first letter and also add a ? at the end on the string
  else:
    return "{}.".format(capitalized)

results = []
while True:
  user_input = input("Say something: ")
  if user_input == "\end":
    break
  else:
    results.append(sentence_maker(user_input))
  
print(" ".join(results))