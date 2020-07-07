
import requests

url = "http://193.61.36.92:8000/authentication/register/"
nick = {
 'username': 'Nick',
 'password':'1234'
 }
nick_response = requests.post(url, data = nick)
nick_response = nick_response.json()
print(nick_response)

url = "http://193.61.36.92:8000/authentication/register/"
olga = {
 'username': 'Olga',
 'password':'5678'
 }
olga_response = requests.post(url, data = olga)
olga_response = olga_response.json()
print(olga_response)

url = "http://193.61.36.92:8000/authentication/register/"
mary = {
 'username': 'Mary',
 'password':'5678'
 }
mary_response = requests.post(url, data = mary)
mary_response = mary_response.json()
print(mary_response)


nick_token = nick_response['access_token']
print(nick_token)

mary_token = mary_response['access_token']
print(mary_token)

olga_token = olga_response['access_token']
print(olga_token)