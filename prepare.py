import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def prep_superstore(df):
    """This functions takes in the superstore df and:
        - converts sale_date column to datetime
        - sets and sorts the index on datetime (sale_date)
        - adds 3 columns: month, weekday, and sales_total
        - returns df
    ---
    Format: df = function()
    """
    # convert sale_date column to datetime
    df.sale_date = df.sale_date.str.replace(' 00:00:00 GMT', '')
    df.sale_date = pd.to_datetime(df.sale_date, format = '%a, %d %b %Y') 
        
    # set and sort the index for datetime
    df = df.set_index(df.sale_date).sort_index()
    
    # adding necessary columns
    df['month'] = df.index.month_name()
    df['weekday'] = df.index.day_name()
    df['sales_total'] = df.sale_amount * df.item_price
    
    return df
    
def dist_plot(df):
    """This function takes in a df and returns distribution plots of all
    variables.
    """
    # run distribution vizzes
    for col in df.columns:
        plt.hist(df[col])
        plt.title(f"{col.capitalize().replace('_',' ')} Distribution")
        plt.show()
        
        
def prep_germany(df):
    """This functions takes in the germany energy df and:
        - renames and lowercases columns
        - pulls out the index column into 'date'
            - changes to datetime
        - sets and sorts the index on date column
        - adds 2 columns: month and year
        - returns df
    ---
    Format: df = function()
    """
    # rename and lowercase columns
    df.columns = df.columns.str.lower()
    df.rename(columns={'wind+solar':'wind_and_solar'}, inplace=True)
    
    # pull out the index to change to datetime
    df['date'] = df.index
    df.date = pd.to_datetime(df.date)
    
    # set and sort index back on proper datetime column
    df = df.set_index(df.date).sort_index()
    df = df.drop(columns='date')
    
    # add month and year columns
    df['month'] = df.index.month_name()
    df['year'] = df.index.year
    
    # fill null values with min
    df.wind = df.wind.fillna(df.wind.min())
    df.solar = df.solar.fillna(df.solar.min())
    
    # fill null values here with sum
    df.wind_and_solar = df.wind_and_solar.fillna(df.wind+df.solar)
    
    return df
    # i filled the na values for wind and solar with the min because germany 
    # has been producing these power options since 2000. This df starts in 2006.
    # Then I filled the NA values in wind and solar with just adding the columns together

    # I could not justify using the mean because the range is too vast. however, I can justify
    # using the min value because the sun exists and there's always a breeze in germany.
    
    