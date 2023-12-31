# Final Data Crawler Project

## Description

Final Data Crawler Project is a Python package designed for crawling specific real estate listing page. This project is done to test the knowledge of python and to learn data collection.

## Installation

### Using a package manager

You can install the crawler as a package: Using `pip`:

```sh
pip install final_data_crawler_project
```

Or using `poetry`:

```sh
poetry add final_data_crawler_project
```

### Cloning the repository

You can also clone the repository and install the dependencies. Using `poetry`:

```sh
git clone https://github.com/kmaciekus/final_data_crawler_project.git
cd final_data_crawler_project
poetry install
```

Afterwards you can checkout and run some [example](./examples) scripts, e.g.:

```sh
poetry run python example/apartment.py
```

## Usage

### As a module

```python
from final_data_crawler_project import crawl_real_estate

print(crawl_real_estate(object="house", query="Kauno raj", time_limit=60, return_format="records"))
```

For more examples look in the [examples](./examples) directory.

## Structure

The project is structured as follows:

- `final_data_crawler_project/`: Main package directory.
  - `__init__.py`: Package initialization file.
  - `crawler_objects/`: Directory containing individual crawler scripts.
    - `__init__.py`: Initialization file for crawlers module.
    - `apartment_crawler.py`: Crawler for apartments listings.
    - `house_crawler.py`: Crawler for house listings.
    - `plot_crawler.py`: Crawler for plot listings.
  - `utils/`: Directory containing help functions.
    - `converters.py`: Holds function for handling convertion to int or float.
    - `error_handler.py`: Holds function for handling text value errors.
  - `definitions.py`: Definitions.
  - `main.py`: Main script for the crawler package.
- `example/`: Directory containing example scripts.
  - `apartment.py/`: Examples getting apartment listings.
  - `house.py/`: Examples getting house listings.
  - `plot.py/`: Examples getting plot listings.
- `tests/`: Test scripts for the package.
  - `mock/`: Directory containing mock data
    - ``
  - `__init__.py`: Initialization file for tests.
  - `converters_test.py`: Testing file for converter functions.
  - `text_error_handler_test.py`: Testing file for error handling function.

## License

This project is licensed under the MIT license.
