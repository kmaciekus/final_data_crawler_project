from io import StringIO
from typing import Any, Callable, Literal
from pandas import DataFrame

from .crawler_objects import ApartmentEstateCrawler, PlotEstateCrawler, HouseEstateCrawler

CRAWLERS: dict[str, Callable[...,DataFrame]] = {
    "plot": PlotEstateCrawler,
    "apartment": ApartmentEstateCrawler,
    "house": HouseEstateCrawler
}
def crawl_real_estate(object: Literal["plot", "apartment", "house"],
                      time_limit: int,
                      query: str ="",
                      return_format: Literal["csv", "df", "records"] = "df"):
    if object not in CRAWLERS:
        raise ValueError(f"Object '{object}' is not available in the crawler")
    data= CRAWLERS[object](query, time_limit)

    if return_format == "csv":
        with StringIO as output:
            data.to_csv(output)
            content = output.getvalue()
        return content
    elif return_format == "records":
        return data.to_dict(orient="records")
    else:
        return data