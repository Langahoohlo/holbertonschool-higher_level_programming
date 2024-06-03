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

    try:
        res = requests.get(url)
    except:
        print("Failed to retrieve data")
        return

    json_data = res.json()

    filtered_data = [{key: post[key] for key in ('id', 'title', 'body')} for post in json_data]

    headers = ['id', 'title', 'body']

    with open(csv_file, "w", newline="") as file:
        csv_write = csv.DictWriter(file, fieldnames=headers)
        csv_write.writeheader()
        csv_write.writerows(filtered_data)
