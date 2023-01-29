# 2079-General-Election-API

Simple flask api to get election data for 2079 Nepal Genera Elections (Federal)

Data from: https://election.ekantipur.com/?lng=eng


## Prerequisites
Python 3.10.8 (Compatible with any python version >=3.7)

Flask 2.2.2

## Host your own instance

1. Clone the repo to your local machine.

2. Install flask using

```
pip install Flask
```

3. Run the app.py file using

```
python app.py
```

## Accessing the api

Any calls should be in the form of 

```
http://127.0.0.1:port/<state-number>/<district-name>/<constituency-number>
```

Eg:

 ```
 http://127.0.0.1:5000/3/kathmandu/3
 ```
 
 Returns a json string with candidate name, name of party and number of votes

  Json string is sorted in ascending order with respsect to obtained votes.
 
## Contributing
 
If you want to contribute to the project, please follow the following steps:
1. Fork the repository
2. Clone the repository to your local machine
3. Create a new branch with a descriptive name
4. Make your changes and commit them
5. Push your changes to your forked repository
6. Create a pull request to the main repository


