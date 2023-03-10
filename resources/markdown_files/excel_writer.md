# Using Pandas Excel Writer

When working on a data integration project, I was curious if there was a way to export columns of data based on a calculation using Excel formula logic. This would allow the end-user to view the formulas in the Excel spreadsheet, as opposed to seeing the values without ssing the calculations. Using `pandas` ExcelWriter, you can!

## Dynamically Chaning Column Labels

In order to avoid problems when running the application in the future, i.e., if there is the possibility that number of columns, column position, etc will change, it is important to set up a way for the Excel formulas to change automatically to accomadate these sorts of changes. First, create a dictionary of key-value pairs where the keys are the indices from 0 - number of columns and values are the corresponding Excel column labels.

```py
# dynamically change columns labels (pandas index to Excel index)
column_labels_excel = {0: "A", 1: "B", 2: "C"}
```

An index variable is created for each sheet using the `.columns` method from pandas. This variable is later used to access the appropriate Excel column label.

```py
indices = df.columns
```

Then it is helpful to create variable names for each column, so that is easier to read the final Excel formulas' logic later. It is best to use descriptive names for these variables. Each variable uses the built-in Python method `.get` which finds the value for a key of a dictionary. The `indices.get_loc("FirstColumnName")` parameter evaluates to the index as found in the pandas data frame; let's say that this column's index is 0. The `the_first_column` ultimately evaluates to "A" in this case. Notice that if this column's index changes in the data frame, this value will change accordingly.

A variable called length is created so that if the number of rows change in the Excel output, the formulas will be applied to the correct number of rows.

```py
length = df.shape[0]

# The First Sheet's columns
the_first_column = column_labels_excel.get(indices.get_loc("FirstColumnName"))
the_second_column = column_labels_excel.get(indices.get_loc("SecondColumnName"))
the_third_column = column_labels_excel.get(indices.get_loc("ThirdColumnName"))

# The Second Sheet's columns
columna_primera = column_labels_excel.get(indices.get_loc("ColumnaPrimera"))
columna_segunda = column_labels_excel.get(indices.get_loc("ColumnaSegunda"))
columna_tercera = column_labels_excel.get(indices.get_loc("ColumnaTercera"))

```

## Variables for New Columns

First create the new columns in each data frame.

---

## Using ExcelWriter

The next step involves using the `ExcelWriter` method in pandas. This funciton is used to write to Excel files, and allows the inclusion of Excel formulas to be exported. This example shows how to export two pandas data frames to the same workbook, and will include Excel formulas that use references from the opposite sheet.

```py
with pd.ExcelWriter("name_of_file.xlsx", engine="xlsxwriter") as writer:
    df.to_excel(writer, sheet_name="Sheet1", index=False)
    df2.to_excel(writer, sheet_name="Sheet2", index=False)
    workbook = writer.book
    sheet1 = writer.sheets["Sheet1"]
    sheet2 = writer.sheets["Sheet2"]
```

### Using for loops to apply the formulas to each cell

In this example, Sheet2 contains a calculated field that is used as a reference in formulas in Sheet1. For this reason, Sheet2's calculated field is defined first. Using f strings, the desired Excel formula is written, replacing the actual letters in curly braces with the variable names defined above.

MAKE NOTE OF col param - make that dynamic too!!

```py

    for row in range(1, length+1):
        # Example formula:
        # =A1+B1
        excel_formula = f'={columna_primera}{row+1}+{columna_segunda}{row+2}'
        sheet2.write_formula(row=row, col=4, formula=excel_formula)
```
