from final_data_crawler_project import crawl_real_estate

if __name__ == "__main__":
    # Crawling house listings related to search query "Kauno raj" witin time limit of 60s 
    # Printing out data as list of records in dict format
    data_found = crawl_real_estate(object="house", query="Kauno raj", time_limit=60, return_format="records")
    print(data_found)