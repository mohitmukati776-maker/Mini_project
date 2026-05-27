#flipkart_dataset analyses
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load data set
df= pd.read_csv(r'C:\Users\mohit\OneDrive\Desktop\data analytics\cleaned_flipkart_dataset.csv')     
#print(df.head(5))
#print(df.info())
#print(df.describe()) 
#missing values in each column
#print(df.isnull().sum())  
#convering product_rating and overall_rating into float data type 
df['product_rating']= pd.to_numeric(df['product_rating'], errors='coerce')
df['overall_rating']= pd.to_numeric(df['overall_rating'], errors='coerce')  
#print(df.describe())
#print(df.head(5))
#coverting product_category_tree into clean string format accepting only first string eg cloting ,footwear not any anothe number or string
df['product_category_tree']= df['product_category_tree'].str.split('>').str[0]
#print(df['product_category_tree'].unique())
#print(df.head(5))
#print(df['product_category_tree'].value_counts())
# in the brand column conver data type to string and fill null values as unknown
df["brand"]=df["brand"].astype(str).fillna("unknown")
#print(df['brand'].value_counts())
#print  values of brand column at row no 27
#print(df['brand'].iloc[27])
# create a new column called discount_percent which calculates the discount percentage based on the retail_price with % symbol

df['discount_percent'] = ((df['retail_price'] - df['discounted_price']) / df['retail_price']) * 100
df['discount_percent'] = df['discount_percent'].round(2).astype(str) + '%'
print(df[['retail_price', 'discounted_price', 'discount_percent']].head(5))

#add new column called price_range which categorizes the products into three categories based on retail_price as low (0-1000), medium (1001-5000) and high (5001 and above)
def price_range(price):
    if price <= 1000:
        return 'low'
    elif price <= 5000:
        return 'medium'
    else:
        return 'high'
df['price_range'] = df['retail_price'].apply(price_range)
print(df['price_range'].value_counts())


# create a new column calles is_risky which categorizes the products as risky if the product_rating is less than 3 and and retail_price greater than 2000 otherwise not risky and store its result as boolean dataype

def is_risky(row):
    if row['product_rating'] < 3 and row['retail_price'] > 2000:
        return True
    else:
        return False
df['is_risky'] = df.apply(is_risky, axis=1)
print(df['is_risky'].value_counts())

# REMOVE WRONG DATA  EX NEGATIVE VALUES IN RETAIL PRICE AND DISCOUNTED PRICE AND DUPICATES ROWS AND RATING GREATER THAN 5
df = df[df['retail_price'] >= 0]
df = df[df['discounted_price'] >= 0]
df = df[df['product_rating'] <= 5]
df = df.drop_duplicates()   

#df.to_csv('cleaned_flipkart_dataset.csv', index=False)
# create two column date and time from crawl time column
df['crawl_timestamp'] = pd.to_datetime(df['crawl_timestamp'], errors='coerce')    
df['date'] = df['crawl_timestamp'].dt.date
df['time'] = df['crawl_timestamp'].dt.time
#change date formate into dd-mm-yyyy
df['date'] = pd.to_datetime(df['date'], errors='coerce').dt.strftime('%d-%m-%Y')
print(df[['crawl_timestamp', 'date', 'time']].head(5))
#save the csv file after cleaning and adding new columns
df.to_csv('cleaned2_flipkart_dataset.csv', index=False)
df.info()

