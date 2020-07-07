# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 17:45:42 2020

@author: Diana Jaganjac
"""

import requests
import json

###########################################################
#Authentication Tokens 


url = "http://193.61.36.92:8000/authentication/token/"
olga = {
 'username': 'Olga',
 'password':'5678'
 }
olga_response = requests.post(url, data = olga)
olga_response = olga_response.json()
olga_token = olga_response['access_token']
print(olga_token)

url = "http://193.61.36.92:8000/authentication/token/"
nick = {
 'username': 'Nick',
 'password':'1234'
 }
nick_response = requests.post(url, data = nick)
nick_response = nick_response.json()
nick_token = nick_response['access_token']
print(nick_token)

url = "http://193.61.36.92:8000/authentication/token/"
mary = {
 'username': 'Mary',
 'password':'5678'
 }
mary_response = requests.post(url, data = mary)
mary_response = mary_response.json()
print(mary_response)

mary_token = mary_response['access_token']
print(mary_token)

######################################################################

#Nick posts an item for auction 

product_url = "http://193.61.36.92:8000/v1/products" # Our API! 
headers = {'Authorization': 'Bearer '+str(nick_token)} 

record = {       "product_category": "Books",
        "title": "Harry Potter",
        "description": "Harry Potter full series",
        "item_condition": "Like New",
        "item_owner_info": "A student selling their childhood copies",
        "quantity": 1,
        "date_posted": "2020-04-18T16:35:26Z"}



nick_response = requests.post(product_url, headers=headers, data=record) 
print(nick_response.json()) 


########################################################################
#Olga posts an item for auction 


product_url = "http://193.61.36.92:8000/v1/products" # Our API! 
headers = {'Authorization': 'Bearer '+str(olga_token)} 

record = {     "product_category": "Home & Furniture",
        "title": "Computer Desk",
        "description": "Wooden PC desk",
        "item_condition": "Like New",
        "item_owner_info": "Selling my computer desk, suitable for adults",
        "quantity": 1,
        "date_posted": "2020-04-18T18:35:32Z"}



olga_response = requests.post(product_url, headers=headers, data=record) 
print(olga_response.json()) 


##########################################################################

product_url = "http://193.61.36.92:8000/v1/products" # Our API! 
headers = {'Authorization': 'Bearer '+str(mary_token)}

record = {   "product_category": "Technology",
        "title": "Ipad",
        "description": "Used Ipad",
        "item_condition": "Used",
        "item_owner_info": "I am selling my used Ipad which is 3 years old",
        "quantity": 1,
        "date_posted": "2020-04-18T18:35:26Z"}


mary_response = requests.post(product_url, headers=headers, data=record) 
print(mary_response.json()) 



###########################################################################
  #Unsuccessful call to API 


product_url = "http://193.61.36.92:8000/v1/products"

response = requests.get(product_url, headers=headers) 
print(response.json()) 

###########################################################################

#Olga bids for Mary's item 

bid_url = "http://193.61.36.92:8000/v1/bids" # Our API! 
headers = {'Authorization': 'Bearer '+str(olga_token)} 

record = {
        "bid_title": "Ipad bid",
        "auction": "http://193.61.36.92:8000/v1/auctions/3/",
        "bid": "27.00",
        "date_posted": "2020-04-18T18:48:00Z"
    }
olga_response = requests.post(bid_url, headers=headers, data=record) 
print(olga_response.json()) 

############################################################################

#Nick bids for Mary's item 

bid_url = "http://193.61.36.92:8000/v1/bids" # Our API! 
headers = {'Authorization': 'Bearer '+str(nick_token)} 

record = {
        "bid_title": "Ipad",
        "auction": "http://193.61.36.92:8000/v1/auctions/3/",
        "bid": "26.00",
        "date_posted": "2020-04-18T18:48:00Z"
    }
nick_response = requests.post(bid_url, headers=headers, data=record) 
print(nick_response.json()) 

############################################################################

#Olga browses all sold items 

product_url = "http://193.61.36.92:8000/v1/auctions" # Our API! 
headers = {'Authorization': 'Bearer '+str(olga_token)} 


response = requests.get(product_url, headers=headers) 
print(response.json())

##############################################################################

#Mary queries list of bids as historical records 

product_url = "http://193.61.36.92:8000/v1/bids" # Our API! 
headers = {'Authorization': 'Bearer '+str(mary_token)} 

response = requests.get(product_url, headers=headers) 
print(response.json())













