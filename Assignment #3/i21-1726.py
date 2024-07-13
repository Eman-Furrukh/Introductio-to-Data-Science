#!/usr/bin/env python
# coding: utf-8

#    # Eman Furrukh    

# # 21i-1726   

# # BSDS - U

# ### Article Generation using N-grams

# You have to write the urdu article using ngrams (1 grams to 5 grams). So, in short your output must be of 5 paragraphs, the first one is generated using unigram, second one is generated using bigram and so on.
# 
# Input: Your input is the seed sentence. E.g. first 3 to 4 words of the paragraph.
# 
# Output: Your output is the consist of 5 paragraphs for each n gram, each of 200 words.
# 
# You have to make N-gram model using the provided dataset. Dataset can be downloaded from  https://www.kaggle.com/datasets/saurabhshahane/urdu-news-dataset 
# 
# You have to use all News Text column.

# ### Classify language out of the list given below using just stop words. Remove punctuations, make it lower.

# In[1]:


import nltk
from nltk.corpus import stopwords
stopwords.fileids()


# In[2]:


from nltk.tokenize import word_tokenize
def function(example):
    word_tokens = word_tokenize(example)
    filtered_sentence = [word.lower() for word in word_tokens if word.isalnum()]
    stop = {lang: set(stopwords.words(lang)) for lang in stopwords.fileids()}
    zeros=[0]*len(stopwords.fileids())
    count = { lang : 0 for lang in stopwords.fileids() }
    for key , value in stop.items():
        for i in value:
            if i in filtered_sentence:
                count[key] = count[key] +1
    return count


# In[3]:


Test="An article is qualunque member van un class of dedicated words naquele estão used with noun phrases per mark the identifiability of the referents of the noun phrases"


# In[4]:


# Your output looks like
function(Test)


# ### Rule Based Roman Urdu Text Normalization

# Roman Urdu lacks standard lexicon and usually many spelling variations exist for a given word, e.g., the word zindagi (life) is also written as zindagee, zindagy, zaindagee and zndagi. So, in this question you have to Normalize Roman Urdu words using the following Rules given in the attached Pdf. Your Code works for a complete Sentence or multiple sentences.
# 
# For Example: zaroori, zaruri, zarori map to the 'zrory'. So zrory becomes the correct word for all representations mentioned above.

# In[7]:


#Your code here
from nltk.tokenize import word_tokenize

def replaceEnd(sentence, prev, new):
    if sentence.endswith(prev):
        return sentence[:-len(prev)] + new
    return sentence
def replaceMultiple(sentence, prev, new):
    s = "0"
    for i in range(10):
        store = prev + prev[len(prev)-1]*i
        if store in sentence:
            s = store
    sentence = sentence.replace(s , new)
    return sentence
def replaceMultiple2(sentence, prev, new):
    s = "0"
    for i in range(1,10):
        store = prev + prev[len(prev)-1]*i
        if store in sentence:
            s = store
    sentence = sentence.replace(s , new)
    return sentence
def romanUrdu(text):
    t = word_tokenize(text)
    for i in range(0 , len(t)):
        t[i]=replaceEnd(t[i] , "ain" , "ein")
        t[i]=replaceEnd(t[i] , "ay" , "e")
        t[i]=replaceEnd(t[i] , "ey" , "e")
        t[i]=replaceEnd(t[i] , "ie" , "y")
        t[i]=replaceMultiple(t[i] , "ih" , "eh")
        t[i]=replaceMultiple2(t[i] , "s" , "s")
        t[i]=replaceMultiple2(t[i] , "d" , "d")
        t[i]=replaceMultiple2(t[i] , "ee" , "i")
        t[i]=replaceMultiple2(t[i] , "s" , "s")
        t[i]=replaceMultiple2(t[i] , "j" , "j")
        t[i]=replaceMultiple2(t[i] , "o" , "o")
        t[i]=replaceMultiple2(t[i] , "a" , "a")
        
        if not t[i].startswith("ar"):
            t[i]=t[i].replace("ar", "r" )
        else:
            t[i]=t[i].replace( "ar" , "r").replace("r", "ar" ,1)
            
        if not t[i].endswith("ry"):
            t[i]=t[i].replace("ry", "ri" )
        else:
            t[i]=t[i].replace("ry", "ri" , t[i].count("ry") -1 )
            
        if not t[i].endswith("sy"):
            t[i]=t[i].replace("sy", "si" )
        else:
            t[i]=t[i].replace("sy", "si" , t[i].count("sy") -1 )
            
        if not t[i].endswith("ty"):
            t[i]=t[i].replace("ty", "ti" )
        else:
            t[i]=t[i].replace("ty", "ti" , t[i].count("ty") -1 )
            
        if t[i][len(t[i])-1] == 'i' and t[i][len(t[i])-2] !='a' and t[i][len(t[i])-2] !='s':
            s = list(t[i])
            s[len(t[i])-1] = 'y'
            t[i] = "".join(s)
        if t[i].find("ah") != -1 or t[i].find("ch") != -1 or t[i].find("eh") != -1 or t[i].find("fh") != -1 or t[i].find("gh") != -1 or t[i].find("hh") != -1 or t[i].find("ih") != -1 or t[i].find("jh") != -1 or t[i].find("lh") != -1 or t[i].find("mh") != -1 or t[i].find("nh") != -1 or t[i].find("oh")  != -1 or t[i].find("qh") != -1 or t[i].find("rh") != -1 or t[i].find("sh")  != -1 or t[i].find("th") != -1 or t[i].find("uh") != -1 or t[i].find("vh")  != -1 or t[i].find("wh") != -1 or t[i].find("xh") != -1 or t[i].find("yh")  != -1 or t[i].find("zh") != -1:
            t[i] = t[i].replace("h", "")
        t[i]=t[i].replace("ai" , "ae") 
        t[i]=t[i].replace("u", "o")   
    return t


# In[8]:


romanUrdu("aap kay paas pen hai?")


# In[9]:


romanUrdu("mujhay nahi pasand aaya")


# In[11]:


romanUrdu("zaroori tor pe IDS ka kaam krna hai")

