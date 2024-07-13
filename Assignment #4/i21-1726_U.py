#!/usr/bin/env python
# coding: utf-8

# # Name: Eman Furrukh
# # Roll No.: 21i1726
# # Assignment 6

# # Instruction

# 1. Don’t plagiarize, Plagiarism would lead to straight zero
# 2. Clearly mention your NAME and ROLL NO#.
# 3. Late submissions are not allowed. Start Early.

# In[ ]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install selenium')
get_ipython().system('pip install webdriver-manager')


# In[2]:


#import libraries
import time
import pandas as pd
from time import sleep
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


# # Question 1  (10 marks)

# Scrape 3 pages of reviews for a single product listing using product URL.<br /> Note: Product must have more than 1 review page. The code must be generic and should work for every product listing URL, with proper checks in place.

# In[18]:


path = r'C:\Users\DELL\Downloads\webscraping\chromedriver.exe'


# In[ ]:


driver = webdriver.Chrome(executable_path = path)
url = "https://priceoye.pk/"
driver.get(url)


# In[ ]:


# get the input elements
ratings = [3, 4]
query = input('Enter search term: ').replace(' ', '%20')
print(f'Modified search term: {query}')


# In[ ]:


options = Options()
#driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
for j in ratings:
    driver.get(f"https://priceoye.pk/catalog/?from=input&q={query}&rating={j}")
    #driver.get(f'https://www.daraz.pk/catalog/?from=input&q={query}&rating={j}')


# In[ ]:


#element = driver.get("https://priceoye.pk/mobiles/samsung/samsung-galaxy-a13")
element = driver.find_element_by_xpath('//*[@id="productGridList"]/div[2]/div[2]/div/div[1]/a/div[3]/h4')
print(element)


# In[ ]:


from selenium.webdriver import ActionChains
action_chains = ActionChains(driver)
driver.implicitly_wait(5)
element = driver.find_element_by_xpath('//*[@id="productGridList"]/div[2]/div[2]/div/div[1]/a/div[3]/h4')
action_chains.click(element).perform()
product_id = browser.current_url.split('/')[-1]
print(product_id)


# In[ ]:


review_data = pd.DataFrame(columns=['Review date', 'Reviewer name', 'Review title', 'Review body', 'Ratings'])
primary_url = driver.current_url
for j in range(1,30):
    browser.get(primary_url+"&page="+str(j))
    response = browser.page_source
    date=[]
    name=[]
    title=[]
    reviews=[]
    rating=[]
    [date.append(i.text) for i in range("div",{'class':"review-date"})]    
    [name.append(i.text) for i in range("div",{'class':"review-user"})]
    # [title.append(i.text) for i in range("h3",{'itemprop':"name"})]
    [reviews.append(i.text) for i in range("div",{'class':"review-body"})]
    [rating.append(i.find("span",{'class':"visuallyhidden seo-avg-rating"}).text)    
    for i in range("div",{'class':"review-heading"}):
        title_present = bool(len(i.findAll("h3")))
        if (title_present):
            title.append(i.find("h3").text)
        else :
            title.append(np.nan)
    rev={'Review date':date, 'Reviewer name':name, 'Review title':title,\
         'Review body':reviews, 'Ratings':rating}
    
    review_data= review_data.append(pd.DataFrame.from_dict(rev), ignore_index=True)


# In[ ]:


review_data= review_data.append(pd.DataFrame.from_dict(rev), ignore_index=True)
review_data['Reviewer name'] = review_data['Reviewer name'].str.replace('Reviewed by ','')
review_data['Review date'] = review_data['Review date'].str.replace('Verified purchase','')
review_data['Review date'] = pd.to_datetime(review_data['Review date'])
review_data = review_data.set_index(['Review date'])
review_data= review_data[review_data.index > pd.to_datetime('2020-12-01')]
review_data.to_csv('output.csv')


# In[22]:


#Output
df


# ### Question 1 Part b  (10 marks)

# Clean the Reviews using NLTK,RE. Remove Punctuations, Smilies and other garbage using any library. 
# 
# Apply Vader Sentiment to find the sentiment of the review, and append it in a column named "Sentiment".
# 
# You can get help of Vader sentiment from this; https://towardsdatascience.com/sentimental-analysis-using-vader-a3415fef7664

# # Question 2   (20 marks)

# Scrape 80 items for a keyword search e.g., 'mobile covers'<br/>Note: Must use "click()" function of webElement, URL changing for pages is not allowed. The code must be generic and should work for every keyword, with proper checks in place. Bonus for also scraping country and Daraz Mall availability.

# In[4]:


query = 'mobile covers'
url = 'https://www.amazon.in'


# In[ ]:


from selenium import webdriver
from time import sleep


# In[ ]:


path = 'chromedriver.exe'
browser = webdriver.Chrome(executable_path=path)
browser.get(url)


# In[ ]:


input_search = browser.find_element_by_id('twotabsearchtextbox')
search_button = browser.find_element_by_xpath("(//input[@type='submit'])[1]")


# In[ ]:


input_search.send_keys(query)
sleep(5)
search_button.click()


# In[ ]:


products = []
for i in range(10):
    product = browser.find_elements_by_xpath("//span[@class='a-size-medium a-color-base a-text-normal']")
    for p in product:
        products.append(p.text)
    next_button = browser.find_element_by_xpath("//li[@class='a-last']")
    next_button.click()
    sleep(5)


# In[ ]:


products[:80]


# In[ ]:


browser.quit()


# In[19]:


#Output
df


# # Question 3  (30 marks)

# <!-- Which Products are on Flash sale? Display Product name, Actual Price, Discounted Price, Discount Percentage, Rating, No. of Reviews, Top 3 reviews displayed.
# 
# Display output must be like this. Products may vary. -->
# 
# If a user wants to make a store to sell something, lets say "Mobile Covers". He/She wants to see folowing things:
# 1. Top 10 Sellers store names
# 2. Daraz Mall Store/ Private store
# 3. Total "Mobile Covers" listings on his store
# 4. Avg Prices
# 5. Avg Units selling
# 6. Positive Seller Ratings
# 7. Seller Country

# In[3]:


#Run this cell to see the sample output
import pandas as pd
pd.read_csv('output.csv')

