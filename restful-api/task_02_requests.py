#!/usr/bin/python3
"""Module to get data from an external source"""


import requests
import csv

def fetch_and_print_posts():
    """Function to fetch and print the fetched data"""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        print(f"Status Code: {response.status_code}")   
        for row in data:
            print(row["title"])
        # print(data)

def fetch_and_save_posts():
    """Function to fetch and save posts in a csv file format"""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    csv_file = 'posts.csv'
    
    if response.status_code == 200:
        data = response.json()
        print(f"Status Code: {response.status_code}")   
        
        keys = data[0].keys()

        with open(csv_file, 'w') as file:
            dict_writer = csv.DictWriter(file, fieldnames=keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)

        print("json save to csv file")

