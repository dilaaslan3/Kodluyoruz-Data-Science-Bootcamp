import pandas as pd
from bs4 import BeautifulSoup
import requests
import warnings


def get_data(pageNo, url):

    headers = {"User-Agent" : "Your user agent"}
    
    r = requests.get(url+str(pageNo)+'?ie=UTF8&pg='+str(pageNo), verify=False, headers=headers)
    content = r.content
    soup = BeautifulSoup(content)
    
    product_data = []

    for product_item in soup.findAll('div', attrs={'id':'gridItemRoot'}):

        name = product_item.find('div', attrs={'class':'_p13n-zg-list-grid-desktop_truncationStyles_p13n-sc-css-line-clamp-1__1Fn1y'})
        author = product_item.find('div', attrs={'class':'a-row a-size-small'})   
        rating = product_item.find('span', attrs={'class':'a-icon-alt'})
        
        users_rated = product_item.find('div', attrs={'class':'a-icon-row'})
        
        if users_rated is not None:
            user_rated2 = users_rated.find('span', attrs={'class':'a-size-small'})
        else:
            user_rated2 = "None"
        
        price = product_item.find('span', attrs={'class':'_p13n-zg-list-grid-desktop_price_p13n-sc-price__3mJ9Z'})
        
        data=[]
                        
        
        if name is not None:
            data.append(name.text) 
        else:
            data.append("unknown-product")
        
        
        if author is not None:
            data.append(author.text) 
        else:
            data.append("0")
            
        
        if rating is not None:
            data.append(rating.text)
        else:
            data.append('-1')
        

        if isinstance(user_rated2, str):
            data.append(user_rated2)
        else:
            data.append(user_rated2.text)     

            
        if price is not None:
            data.append(price.text)
        else:
            data.append('0')
        
        product_data.append(data)    
    
    return product_data



def data_to_df(url):

    no_pages = 10
    results = [] 

    for i in range(1, no_pages+1):
        results.append(get_data(i, url))
        
    flatten = lambda l: [item for sublist in l for item in sublist]

    df = pd.DataFrame(flatten(results), columns=['Book Name','Author','Rating', 'User Rates', 'Price'])

    return df


def main():
    
    url = 'https://www.amazon.com.tr/gp/bestsellers/books/ref=zg_bs_pg_'
    url_computer_books = 'https://www.amazon.com.tr/gp/bestsellers/books/13808201031/ref=zg_bs_pg_'
    url_eng_books = 'https://www.amazon.com.tr/gp/bestsellers/books/13808216031/ref=zg_bs_pg_'
    
    df = data_to_df(url)
    df.to_csv('bestseller_books.csv', index=False, encoding='utf-8-sig')

    #df_comp_books = data_to_df(url_computer_books)
    #df_comp_books.to_csv('computer_books.csv', index=False, encoding='utf-8-sig')

    #df_eng_books = data_to_df(url_eng_books)
    #df_eng_books.to_csv('engineering_books.csv', index=False, encoding='utf-8-sig')


if __name__ == "__main__":
    main()