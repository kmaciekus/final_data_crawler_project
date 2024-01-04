from final_data_crawler_project import crawl_real_estate

if __name__ == "__main__":
    # Crawling all aparatments listings related to search query "Panevėžy" witin time limit of 30s 
    # Printing out data in Pandas dataframe (as it is default return of data)
    data_found = crawl_real_estate(object="apartment", query="Panevėžy", time_limit=30)
    print(data_found)