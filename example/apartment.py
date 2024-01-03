from final_data_crawler_project import crawl_real_estate

if __name__ == "__main__":
    data_found = crawl_real_estate(object="plot",time_limit=15)
    print(data_found)