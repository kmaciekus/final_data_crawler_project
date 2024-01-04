from final_data_crawler_project import crawl_real_estate

if __name__ == "__main__":
    # Crawling all plots listed on the page
    # Saving data to csv file
    # Encoding for lithuanian characters "Šš", "Čč" etc.
    data_found = crawl_real_estate(object="plot")
    data_found.to_csv("plots_aruodas.csv", encoding='utf-16') 