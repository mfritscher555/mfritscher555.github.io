# Data Matching Project - Learning Regex along the Way

## The matching process

As a part of data matching project, I wanted to be able to display people's names as accurately as possible. The matching process I used entailed matching a customer ID from one source to another. The interested party wanted to know which customers that the application was unable to match; i.e., any customers that were in one data source but not the other. The final deliverable was to be a list of customer names and customer IDs that were unmatched, so that the interested party could review these transactions. Though customer IDs are usually sufficient to identify these transactions, in the process, it is much more helpful if other information such as name and date are available and accurate.

## Using Regex

Once the matching process was established, regex was used as a way to fix some mistakes in people's names. For instance, suffixes for some reason got attached to the back of people's last names in the dataset. For example, a person's name might display "FRITSCHERJR, MATTHEW" instead of "FRITSCHER JR, MATTHEW" (by the way, I am not a Junior). Using a regular expression allowed me to make such changes. The following expression identifies any names that follow this convention:

```py
pattern = re.compile(r".+\S[jJ][rR],.+")
```

Since there were other errors in people's names that were yet to be addressed (for example, the occasional symbol instead of a letter), the first part of the expression includes any character (the period denotes this). The "+" indicates that it will match anything up until the character after, which in this case is a non-space character followed by a j or J (and subsequently either an r or R, followed by a ,). The comma is a key part here; the comma allows us to differentiate a suffix versus the instances of "jr" appearing in someone's name. The ".+" denotes that any amount of characters can follow the comma.

From here, a function was used to replace any instances of people's name that follow this pattern and fix the name so that a space separates the last name and the suffix. A function similar to one below was written and then called when writing to the final Excel file for the client.

```py
    def suffix_fixer(names):
        master_list = []
        for name in names:
            pattern = re.compile(r".+\S[jJ][rR],.+")
            matches = sr_pattern.findall(i)
            if i in matches:
                i = [sub.replace("JR", " JR") for sub in _matches]
                i = i[0]
                master_list.append(i)
            else:
                master_list.append(i)
        return master_list
```

Being new to regex, there is a lot more to learn; however, I already see that there a lot of applications for using regular expressions.
