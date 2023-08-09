# Using Pandas Excel Writer

When working on a data integration project, I was curious if there was a way to export columns of data based on a calculation using Excel formula logic. This would allow the end-user to view the formulas in the Excel spreadsheet, as opposed to seeing the values without using the calculations. Using `pandas` ExcelWriter, you can!

## Dynamically Changing Column Labels

In order to avoid problems when running the application in the future, i.e., if there is the possibility that number of columns, column position, etc will change, it is important to set up a way for the Excel formulas to change automatically to accommodate these sorts of changes. First, create a dictionary of key-value pairs where the keys are the indices from 0 - number of columns and values are the corresponding Excel column labels.

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

The next step involves using the `ExcelWriter` method in pandas. This function is used to write to Excel files, and allows the inclusion of Excel formulas to be exported. This example shows how to export two pandas data frames to the same workbook, and will include Excel formulas that use references from the opposite sheet.

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

```py

    for row in range(1, length+1):
        # Example formula:
        # =A1+B1
        excel_formula = f'={columna_primera}{row+1}+{columna_segunda}{row+2}'
        sheet2.write_formula(row=row, col=4, formula=excel_formula)
```

### Writing a function to dynamically create Excel formula formatted strings

The below function allows you to deal with long Excel formulas in a way that helps prevent human-error of manually creating the formatted string. Notice that there is a parameter called `columns_dict` which must be a dictionary where the keys are the pandas indices of the orignal data frame and the values are the Excel indices as per formula logic.

For example an acceptable dictionary could be `{0:"A", 1:"B", 2:"C"}`.

```py

def excel_formulas(string, row, columns_dict):
    """
    To allow for dynamic insertion of variables in Excel formula,
    Convert an Excel formula raw string to a formatted string.

    :param string: should be a raw string where the formula from row 4 is pasted in to avoid #REF errors
    :param row: when function is within a for loop, row is incremented
    :param columns_dict: a dictionary containing the names of the columns, where each key & value in the dictionary is
    already defined as the index using the Excel letter notation

    :returns:
    This f-string is to be used to create the formula in Excel logic

    """

    new_string = []
    numbers_dict = {"0": -3, "1": -2, "2": -1, "3": 0, "4": 1, "5": 2, "6": 3, "7": 4, "8": 5, "9": 6}
    chars = [",", "="]
    for index, value in enumerate(string):
        previous_element = string[index - 1]
        if value in columns_dict.keys():
            value = value.replace(value, f"{columns_dict.get(value)}")
            new_string.append(value)
        elif value in numbers_dict.keys():
            # for numbers in formula that are not row numbers (MULTIPLE DIGITS ARE NOT SUPPORTED)
            # these numbers are either preceded by a comma or equal sign
            if previous_element in chars:
                new_string.append(value)
            else:
                # for row numbers
                x = str(numbers_dict.get(value))
                value = value.replace(value, f"{row + int(x)}")
                new_string.append(value)
        else:
            new_string.append(value)

        new = "".join(new_string)
        f_string = f'{new}'

    return f_string

```

### Dynamically Creating the `column_dict` input

For Excel spreadsheets that have several columns, it is not ideal to have to manually create this input dictionary. Also, depending on the state of the spreadsheet, this function makes it easy to add or remove columns without having to change this input dictionary every time a change needs to be made.

```py

def dynamic_dict(number_of_columns):
    """
    Create a dictionary that is used to dynamically reference columns in Excel formulas

    :param number_of_columns: Number of column labels to create (can support up to 701)

    :returns: A dictionary where the keys are the indices in pandas notation and the values are the indices in Excel
    notation
    """

    key_list = []
    value_list = []
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for i in range(0, number_of_columns + 1):
        key_list.append(i)
        for first_letter_index in range(0, number_of_columns*26):
            if i // 26 == first_letter_index:
                if first_letter_index == 0:
                    letter = alphabet[i - 26]
                    value_list.append(letter)
                else:
                    letters = str(alphabet[first_letter_index - 1]) + str(alphabet[i - 26 * first_letter_index])
                    value_list.append(letters)

        i += 1

    final_dict = dict(zip(key_list, value_list))

    return final_dict

```

### Re-writing the above Excel formulas with these changes

```py

    # PUT CLOUMN LOCATION VARS HERE

    column_dict = dynamic_dict(len(df.columns))

    for row in range(1, length+1):
        # Example formula:
        example_str '=A4+B4'
        excel_formula = excel_formulas(example_str, column_dict)
        sheet2.write_formula(row=row, col=4, formula=excel_formula)
```
