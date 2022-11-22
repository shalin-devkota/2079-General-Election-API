# 2079-General-Election-API

Simple flask api to get election data for 2079 Nepal Genera Elections (Federal)

Data from: https://election.ekantipur.com/?lng=eng


## Requirements
-python 3.10.8 (Compatible with any python version >=3.7)

-flask 2.2.2

## Installation and Use

-pip install flask

-Download the 2 files

-In the terminal:
 
 `flask --app main --debug run`
 

##Accessing the api

Any calls should be in the form of 

`http://127.0.0.1:port/<state-number>/<district-name>/<constituency-number>`

Eg:

 `http://127.0.0.1:5000/3/kathmandu/3`
 
 Returns a json string with candidate name, name of party and number of votes

  Json string is sorted in ascending order with respsect to obtained votes.
