# Project Documentation: Folder Content Size Analyzer

## Overview
The Folder Content Size Analyzer is a Python project that analyzes the contents of a specified folder, summarizing the total size of files by their extensions. It provides visual representations of the data using pie and bar charts, and exports the summary to an Excel file for further analysis.

## Requirements
To run this project, you need:
- Python 3.x
- Required libraries:
  - `matplotlib`
  - `pandas`
  
You can install the necessary libraries using pip:

```bash
pip install matplotlib pandas openpyxl
```

## Project Structure
- **analyzer.py**: Main script containing the functions for analyzing and visualizing folder contents.

## Functions

### `summarize_folder_contents(folder_path)`
This function traverses the specified folder and calculates the total size of files based on their extensions.

#### Parameters
- `folder_path` (str): The path to the folder to analyze.

#### Returns
- `file_sizes` (dict): A dictionary with file extensions as keys and their total sizes in bytes as values.
- `total_size` (int): The total size of all files in the folder in bytes.

### `visualize_data(file_sizes, total_size)`
This function visualizes the data using pie and bar charts, and saves the results in an Excel file.

#### Parameters
- `file_sizes` (dict): A dictionary containing file extensions and their sizes in bytes.
- `total_size` (int): The total size of all files in bytes.

### Visualizations
- **Pie Chart**: Shows the distribution of file sizes by type.
- **Bar Chart**: Compares the total size of each file type.
- **Excel Export**: Saves the summarized data to an Excel file named `file_sizes.xlsx`.

## Usage
To use the Folder Content Size Analyzer, follow these steps:

1. Set the `folder_path` variable to the path of the folder you wish to analyze.
2. Run the script.

```python
# Example usage
folder_path = 'E:\\epaathlfs\\epaath_tracking_files'  # Update the path as necessary
file_sizes, total_size = summarize_folder_contents(folder_path)
visualize_data(file_sizes, total_size)
```

## Output
- The script will display:
  - A pie chart of file sizes by type.
  - A bar chart comparing total sizes by file type.
- An Excel file named `file_sizes.xlsx` will be created in the current working directory, containing the summary of file sizes by type.

## Notes
- Ensure that the specified folder path exists and is accessible.
- The script is designed to work on all operating systems that support Python and the required libraries.

## Conclusion
The Folder Content Size Analyzer is a useful tool for users who need to analyze file sizes in a directory. It simplifies the process of understanding storage usage by file type and provides visual aids to support data-driven decisions.
