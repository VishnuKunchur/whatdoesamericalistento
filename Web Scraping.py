##Lists

my_list = [] #initializes an empty list

my_list = [4,3,2,1] #Creating a list of 4 numeric elements

my_list.append(5) #.append() adds elements to the list. Here '5' is added to the list

my_list.pop(0) #.pop() throws out the value of the list element at the specified *index* value
 
my_list.remove(3) #.remove() throws out the value of the list element when the *element* value is specified

my_list.insert(1,100) #.insert() - first argument: index, second argument: value

my_list.clear() #deletes all elements in the list, returns empty list

my_list = ['a','b','c','d']

my_list.index('d') #outputs the index of a particular element in the list. Outputs 3 in this case

my_list = []

my_list = [1,2,1,1,'a']

my_list.count(1) #outputs the total num of isntances of the input value

my_list.remove('a')

my_list.sort() #sorts the given list

##Dictionaries

my_dict = {} #initializes an empty dictionary
#The idea is to create pairs of keys and values.

my_dict = {'school':'definition of school', 'coding':'definition of coding', 'python':'definition of python'}

my_dict['school'] #Prints out the value of school from the "key" that is school
#Keys are unique in a given dictionary. 

my_dict['pen'] = 'definition of pen' ##Adding another item to the dictionary

my_dict['school'] = 'key number 2' ##changing "value" for the key.

for key, value in my_dict.items():
    print(key,'            ',value) ##printing out the keys and values from the dictionary            

del(my_dict['pen']) ##deleting a value from a dictionary

##Tuples

person = 'vishnu',25,"5.11" #Tuples are declared thus. Round parantheses may be used in tuple declaration
name, age, height = person #unboxing the tuple

for value in person:  
    print(value)    #tuples are iterable. each element is stored as a "value"
    
person = 'vishnu', ('black', 'blue'), 5.11 #Nested tuple. Second element in the "person" tuple is also a tuple
#tuples are immutable!! you cannot replace the elemnts of a tuple with other values

##LIST COMPREHENSIONS

import random

test_list = []
for value in range(0,20):
    test_list.append(random.randint(0,101)) #Creating a list of 20 values, randomly generated

test_list1 = [value for value in range(0,21)] #Doing the same with list comprehension

test_list2 = [random.randint(0,121) for value in range(0,21)] #doing the same with list comprehension

##List comprehension - 2
carts = [['toothpaste','shampoo','tc'],['shoes','flips','fugs'],['fish','fog','fids']]
person1 = ['toothpaste','shampoo','tc']
person2 = ['shoes','flips','fugs']
person3 = ['fish','fog','fids']

ls = [person1, person2, person3]

carts[2][2]

#creating 2-D lists

list_2d = []
in_list = []

for value in range(0,25,5):  ##The long, convoluted method
    in_list = []
    for col in range(value,value+5):
        in_list.append(col)
    list_2d.append(in_list)
        
list_2d = [[col for col in range(value, value+5)] for value in range(0,25,5)]

##in-line ifelse statements

a = 20

['20 is a' if a == 20 else 'a is not 20'] ##inline ifelse statements

ls = [] #initializing an empty list
ls = [value for value in range(-5,5)] #list expressions for

positive_ls = [value for value in range(-5,5) if value > 0] #combining for and if list expressions

##Writing to Excel, making .csv files

from xlsxwriter import Workbook
import xlrd

workbook = Workbook('first_file.xlsx') ##creates an empty workbook

worksheet1 = workbook.add_worksheet()

for value in range(0,200):
    worksheet1.write(0,value, print('rownumber is ',value))
    
workbook.close() ##closes the empty workbook

##HOW WEBSITES ARE HOSTED
##USER - REQUEST - SERVER - RESPONSE - USER

##BeautifulSoup Intro Exercise
from bs4 import BeautifulSoup #imports BeautifulSoup package
import requests #imports requests package

url = "http://example.com/" #specifying the url of the site to be scraped

response = requests.get(url) #requests.get() - Gets the webpage and creates a response object

data = response.text #obtains source code for the response object

soup = BeautifulSoup(data, 'html.parser') #creating a BS object from the response text(html file)

tags = soup.find_all('a')

for tag in tags:
    print(tag.get('href'))

'''How do requests work?'''
##Two types of requests are most commonly used - "get" and "push"
##'get' obtains info, 'push' pushes info

#requests.get(url) - generates a response object

response = requests.get("http://google.com") #gives you a response object from the Google server

print(response) ##prints out a status code

##status code is a 3 digit integer, indicates how the server processed our request and gave a response

'''STATUS CODES AND INTERPRETATIONS

100 - 199: Informational Response
200 - 299: Success Response
300 - 399: Redirection Response
400 - 499: Client Error
500  -599: Server Error
'''

response.content ##Prints out the complete content of the response ('html format')

print(response.status_code) #Prints out the status_code of a response

#Obtaining headers:
headers = response.headers ##Outputs a dictionary

for key, value in response.headers.items():
    print(key,'                             ',value) ##Printing out the items in the headers dictionary
    
##Fake User Agent -- It may be useful to use a fake agent on some sites that do not allow robots
import requests
from fake_useragent import UserAgent #allows you to say that a browser is sending the request and not a bot

ua = UserAgent()

header = {'user_agent':ua.chrome} ##create a dictionary that will add an exception to the site

page = requests.get('https://www.google.com',headers = header) ##adds the exception so that the scraper may work

page = requests.get('https://www.google.com', timeout = 30) ##so that your bot doesnt wait for eternity

##Beautiful Soup
##Syntax for making soup - BeautifulSoup('html file', lxml/'html.parser')
response = requests.get('http://nooooooooooooooo.com/') ##getting response object from nooooo.com server

noo = response.text ##isolating text from response object

noosoup = BeautifulSoup(noo,'html.parser') ##parsing text to obtain html file

nsp = noosoup.prettify() ##creates a nice pretty looking html file with distinguishable tags

'''IMPORTANT: DO NOT USE THE prettify() object to get tag data! Only look at the html file that has been created after BeautifulSoup has parsed the
response.text onject'''

##getting attributes within tags:
'''
tag = noosoup.tag
print(tag.get('attribute')) ##Prints out the value contained inside the required attribute of the tag   
(Another way of doing this:)
print(tag['attribute']) ##tag is a dictionary, all attributes contained within the tag are obtainable by subsetting dictionary
'''

'''
Multivalued attributed will always return a list of values. Ex:
    <tag attr = 'as df'/>
when we do tag.get('attr'), we would see an output as follows:
['as', 'df'] ##this is a list
'''

'''Navigable strings:
Let's try to get the text from a 'title' tag
title = soup.title ##gets the title tag
title.string ##outputs the contents of title ##the .string method is applied to the tag to extract strings from it
title.string.replace_with("new title name") ##this code would replace the contents of the title with something else
'''

##Let's scrape the http://nooooooooooooooo.com/ website

response  = requests.get('http://nooooooooooooooo.com/') 

data = response.text 

soup = BeautifulSoup(data, 'html.parser') 

soup.meta['http-equiv']

def read_file():
   file = open('three-sisters.html')
   data = file.read()
   file.close()
   return data

soup3 = BeautifulSoup(read_file(), 'lxml') 

soup3_p = soup3.prettify()

##Accessing multiple tags with the same name

'''
tag.contents -> returns all contents of the tag's "children"
Say we wanted to access all the children of the head tag from noooooooo/com
'''

head = soup.head

for child in head.contents:
    print(child if child is not None else '', end = '\n\n\n\n') ##accesses all the tag's children and prints them out, if they exist
    
'We can also do the same with head.children'

for child in head.children:
    print(child if child is not None else '', end = '\n') ##same output as above.
    
'''Is there a way to DRILL DOWN INTO every tag and mine ALL the children, or descendents? YES!'''
'''DESCENDANTS METHOD'''

for index, child in enumerate(head.descendants): ##PRINTS OUT ALL CHILDREN, GRANDCHILDREN, ....."
    print(index)
    print(child)

noo_list = []
for child in head.descendants:
    noo_list.append([child] if child != '\n' else '')

noo_list[3]

for index, des in enumerate(soup3.body.descendants):
    print(index)
    print(des)

'''PARENTS METHOD'''
'''To find parents of a given tag'''

head = soup.head
head.parent ##returns the 'parent' tag

'''.parents --> returns a generator of all parents of a given tag'''

p = soup.p

for parent in soup.p.parents: ##Basically prints out the entire html document, since html is a parent
    print(parent)

for parent in soup.p.parents:
    print(parent.name) ##prints out the name of the parent tag

'''WE'RE GOING SIDEWAYS!'''
'''we look at 'siblings' of tags'''
for index, sibling in enumerate(soup3.p.next_sibling.next_sibling): ##we do next_sibling twice because first next_sibling is '\n'
    print(index)
    print(sibling)

'''same idea for previous sibling'''

'''we can just get a list of all the next and previous siblings with next.siblings and previous.siblings'''

for ns in soup3.p.next_siblings:                    ##helps you navigate across all siblings!!
    print(ns.name if ns.name is not None else '')

'''REGULAR EXPRESSIONS'''

import re  ##YOU NEED THIS FOR REGEX!!

reg_obj = re.compile('[abcd]')
print(reg_obj.match('nb'))

import re

reg = re.compile('abc')
reg.match('ab')

'''
METACHARACTERS
* - lets you repeat the thing just before it ANY number of times, i.e. from 0 to infinity
+ - matches if the exp just before it matches ATLEAST once
[] - like an "or" function for anything within it
? - WHAT COMES JUST BEFORE THIS IS OPTIONAL
{m,n} - what comes just before must come ATLEAST m times and at MAX n times
^ - string MUST START with whatever comes just after it
$ - whatever comes JUST BEFORE IT must be the last character
| - this is the OR operator
'''
reg = re.compile('a{0,1}')
reg.match('aaax')

'''PARSING THE TREE'''
'''.find('tag_name') and .find_all('tag_name') -> takes a tag/regex as input and finds all tags in the soup with that name
'''

soup.find_all('div') ##prints out ALL 'div' tags

'''Using regex to find tags'''
reg = re.compile('^t')

soup3.find_all(reg)

for tag in soup3.find_all(reg):
    print(tag.name)
    
'''You can also pass lists of regexs'''                                                              
for tag in soup3.find_all(['a','b']):
    print(tag.name)
    
'''Scraping the Junk Food Dataset'''
response = requests.get('http://www.acaloriecounter.com/fast-food.php')

data = response.text
soup = BeautifulSoup(data, 'html.parser')

soup_pretty = soup.prettify()

soup.find_all('th')

def has_class(th):
    return th.has_attr('scope')  ###Checks whether a tag has a particular attribute

for tag in soup.find_all(has_class): ###Prints all tags with the specified attributes
    print(tag)





