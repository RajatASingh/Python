#!/usr/bin/env python
# coding: utf-8

# #### Q.1. Given a sentence as input, calculate and output the average word length of that sentence.To calculate the average word length, you need to divide the sum of all word lengths by the number of words in the sentence.

# <font color = red> **Sample Input:** </font> <br>
#    this is some text 
# 
# <font color= red> **Sample Output:** </font> <br>
# 3.5
# 
# <font color=red> **Explanation:** </font> <br>
#   _There are 4 words in the given input, with a total of 14 letters, so the average length will be: 14/4 = 3.5_ 

# In[ ]:



taken_input = input()
# Given input is "This is some text"

str_split = taken_input.split() 
# Split function help us to separate string after space, which makes it easy to count number of  words in a sentance. 

replace_space = taken_input.replace(" ","")
# Replace function is used to replace something in a syntax. Here we are replacing spaces with no spaces to find of length of a sentance. 
avg_of_word = (len(replace_space)/len(str_split))

print (avg_of_word)
                         


# 
# 

# #### <font color= green>  Sourse: SOLOLEARN (pyhton Basics) </font>
# 
# * #### <font color= olive>  _Issues which i faced while solving this problem:_ </font>
# 
# 1. While working on this problem! the biggest question was in my mind how to count the exact length of words without counting the spaces in between them.
# 2. While counting the length with the help of len FUNCTION it was also counting spaces in a sentence as length.
# 
# ####  <font color= olive> Approch to solve the above issue </font>
# 1. Replacing the spaces with no spaces ( taken_input.replace(" ","") ) was the approach in my mind which will work to solve the above issue which I was facing in point number 2. 
# 

# In[ ]:





# #### Q.2. Take a string as input and output each letter of the string on a new line, repeated N times, where N is the position of the letter in the string.
# 
# 

# <font color = red> **Sample Input:** </font> <br>
# data
# 
# <font color = red> **Sample Output:** </font> <br>
# d <br>
# aa <br>
# t t t <br>
# aaaa 

# <font color=red> **Solution:** </font>

# In[1]:


N = "Data"       

for i in range(len(N)):
    print(N[i]* (i +1))


# In[ ]:




