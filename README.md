# Financial-Sample-Project-Using-Python-Libraries
This is just a dummy project, where we'll take help of numpy, pandas, sklearn and matplotlib to create amazing plots.
This project analyzes financial data using libraries like Pandas and Matplotlib. The project reads financial data from an Excel file, processes it, and then generates visualizations to analyze the data.


## Prerequisites
Before running the code, ensure you have the following libraries installed:

* Matplotlib
* Pandas
* NumPy
* Scikit-learn

You can install these libraries using pip:

    pip install matplotlib pandas numpy scikit-learn


## Getting Started

1. Clone the repository to your local machine:

       git clone https://github.com/nibeditans/financial-sample-project.git

2. Run the Python script:

       python financial_analysis.py


## Code Explanation

The code and analysis in financial_analysis.ipynb performs the following steps:

* Reads financial data from an Excel file and saves it as a CSV file for processing.
* Converts the 'Date' column to a datetime format.
* Imputes missing values with a constant value.
* Groups the data by 'Country' and 'Date' and calculates the sum of 'Units Sold,' 'Sale Price,' and 'Profit.'
* Generates scatter plots for each country, showing 'Units Sold,' 'Sale Price,' and 'Profit' trends over time.
* Creates a scatter plot for the entire dataset to visualize the overall performance trends.

## Output

The code generates scatter plots for individual countries as well as the entire dataset, displaying trends in 'Units Sold,' 'Sale Price,' and 'Profit' over time.


## Data Source
The financial data used in this project is sourced from an Excel file located at:

Financial Sample.xlsx [Attached in this Repository, you can download it.]


## Author

@nibeditans


Feel free to fork this project, make improvements, or use it as a reference for your own financial data analysis tasks.

Happy exploring!

