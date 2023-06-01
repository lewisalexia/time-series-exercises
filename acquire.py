# Imports
import pandas as pd
import requests
import math
import os

# Functions

def star_wars(endpoint, key_name):
    """This function will take in an endpoint (with a slash) and the key_name
    for the preferred results and return:
        - a csv file in the local directory, if none
        - a df with populated with results
        
    Format: df = function()
    """
    
    # Empty list for results to turn into df later
    endpoint_list = [] 
    
    # API query
    base_url = 'https://swapi.dev/api/'
    query = requests.get(base_url)
    print(f"Query Completed for {endpoint.strip('/').capitalize()}...")
    
    # File check
    if os.path.isfile(f"{endpoint.strip('/')}.csv"):
        df = pd.read_csv(f"{endpoint.strip('/')}.csv", index_col=0)
        print(f"CSV File Found, Loading...")
        
    else:
        print(f"CSV Not Found, Writing Data to CSV...")
        
        # establish specific endpoint connection
        endpoint_uri = requests.get(base_url + endpoint + '/')
        data = endpoint_uri.json()
        print(f"Data Found, Identifying Range...")

        # identifying number of endpoint results
        number_of_endpoints = data['count']
        next_page = data['next']
        previous_page = data['previous']
        print(f'''Number of {endpoint.strip('/').capitalize()}: {number_of_endpoints}
        Next Page: {next_page}
        Previous Page: {previous_page}''')

        # determine number of endpoint pages 
        number_of_results_per_page = len(data[key_name])
        max_page = math.ceil(number_of_endpoints / number_of_results_per_page)
        print(f'''Number of Results Per Page: {number_of_results_per_page}
        Max Pages: {max_page}''')
        print(f"Creating DF Results...")
        print(f"Iterating through pages to gather all applicable results...")

        # loop to iterate through each page
        for i in range(max_page):
            pg_results = base_url + endpoint + (f"?page={i+1}")
            data_loop = requests.get(pg_results).json()

            # going through to grab each row
            for r in range(len(data_loop[key_name])):
                result = data_loop[key_name][r]
                endpoint_list.append(result)
        
        # return results in dataframe     
        df = pd.DataFrame(endpoint_list)
        
        # write to csv
        df.to_csv(f"{endpoint.strip('/')}.csv")
        
    return df

def germany_energy():
    """This function loads or writes a CSV file from a hardcoded URL
    ---
    Format: df = function()
    """
    if os.path.isfile(f"germany.csv"):
        df = pd.read_csv(f"germany.csv", index_col=0)
        print(f"CSV File Found, Loading...")
        
    else:
        print(f"CSV Not Found, Writing Data to CSV...")
        df = pd.read_csv("https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv")
        
        # write to csv
        df.to_csv(f"germany.csv")
        
    return df

def superstore():
    """This function loads or writes a CSV file from a hardcoded URL
    ---
    Format: df = function()
    """
    if os.path.isfile(f"ts_superstore.csv"):
        df = pd.read_csv(f"ts_superstore.csv", index_col=0)
        print(f"CSV File Found, Loading...")
        
    return df