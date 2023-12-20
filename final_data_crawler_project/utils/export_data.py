import pandas as pd
import json

class ExportTo:
    """
    The ExportTo class facilitates the export of a list of objects to various file formats, such as JSON, CSV, and Excel.

    Attributes:
    - list_of_objects (list): A list of objects to be exported.
    - object_name (str): A descriptive name for the type of objects in the list.
    - export_file_name (str): The base name of the exported file without extension.

    Methods:
    - to_json(): Exports the list of objects to a JSON file.
    - to_csv(): Exports the list of objects to a CSV file.
    - to_excel(): Exports the list of objects to an Excel file.

    Usage Example:
    ```
    data_to_export = [...]  # Replace with the actual list of objects
    exporter = ExportTo(data_to_export, "MyObject", "exported_data")
    exporter.to_json()
    exporter.to_csv()
    exporter.to_excel()
    ```
    """
    def __init__(self, list_of_objects: list, object_name: str,export_file_name: str):
        """
        Initializes an ExportTo object.

        Parameters:
        - list_of_objects (list): A list of objects to be exported.
        - object_name (str): A descriptive name for the type of objects in the list.
        - export_file_name (str): The base name of the exported file without extension.

        Raises:
        - TypeError: If list_of_objects is not of type list.
        - ValueError: If list_of_objects is empty.
        """
        if type(list_of_objects) is not list:
            raise TypeError("Class accepts only list types")
        elif not list_of_objects:
            raise ValueError("List is empty!")
        else:
            self.list_of_objects = list_of_objects
        self.object_name = object_name
        self.export_file_name = export_file_name
    
    def to_json(self):
        """
        Exports the list of objects to a JSON file.

        Returns:
        - None

        Side Effects:
        - Creates a JSON file with the exported data.
        - Prints a message indicating that the file has been saved.
        """
        with open(f"{self.export_file_name}.json", "w", encoding='utf-8') as file:
            json.dump({f"{self.object_name}": self.list_of_objects}, file, indent=4, ensure_ascii=False)
        print(f"File: {self.export_file_name}.json saved!")
        return
    
    def to_csv(self):
        """
        Exports the list of objects to a CSV file.

        Returns:
        - None

        Side Effects:
        - Creates a CSV file with the exported data.
        - Prints a message indicating that the file has been saved.
        """
        df = pd.DataFrame.from_records(self.list_of_objects)
        df.to_csv(f"{self.export_file_name}.csv", encoding="utf-8", float_format=str)
        print(f"File: {self.export_file_name}.csv saved!")
        return
    def to_excel(self):
        """
        Exports the list of objects to an Excel file.

        Returns:
        - None

        Side Effects:
        - Creates an Excel file with the exported data.
        - Prints a message indicating that the file has been saved.
        """
        df = pd.DataFrame.from_records(self.list_of_objects)
        df.to_excel(f"{self.export_file_name}.xlsx", sheet_name=self.object_name)
        print(f"File: {self.export_file_name}.xlsx saved!")
        return