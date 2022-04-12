# Create two lists
# - letters contains !random letters of the Latin alphabet
# - vowels contains only the 5 vowels

# Define a function choose_vowels() that, given the list letters, 
# would return only those letters that are vowels. 

# Print out the result.

# Sample of the list letters:
# ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'i', 'n', 'g', 'l', 'a', 'n', 'g', 'u', 'a', 'g', 'e']

# Sample output:
# ['o', 'a', 'i', 'a', 'u', 'a', 'e']

import random
gl = ["a","e","i","o","u","y"]
a = ["q","w",'e',"r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
k = []
w = []
for i in range(random.randint(0,50)):
  e = random.randint(0,25)
  w.append(a[e])
print(w)
for i in range(len(w)):
  for l in range(len(gl)):
    if w[i] == gl[l]:
      k.append(w[i])
print(k)
    
  
  
  
  
  



