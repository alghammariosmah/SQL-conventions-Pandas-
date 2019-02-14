# SQL Naming Conventions and Styling

This document concatinate multiple Excel files with the same content, and simultaneously defines my standard for SQL naming conventions and source code formatting that I created for my software engineers. Although it is a mandatory standard for them, I thought I’d post it for the benefit of others in case anyone finds value in it

## Import before usage
I used python 2.7 interpreter. You have to install the following libraries:
* pandas
* unicodedata (If you are using other languages other than English)
* os
* datetime
* numpy
* XlsxWriter (Excel writer)
* xlrd (Excel reader)
  
## Usage

Modify 
``tablesConcat("sourceFile", ".xlsx", "output.xlsx","destDir")`` in the `sqlxcsconv.py` file

  
## Structure:
* sourceFile
  * directory where .xlsx files are located at
* `.xlsx`
  * the files have to either end with `.xlsx` or `.csv`
* `output.xlsx`
  * The table will be dumped here
* destDir
  * directory where the results of concatinating and Conventions should be located at 
