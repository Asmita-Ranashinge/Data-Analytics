import pandas as pd

# Assign spreadsheet filename to `file`
file = 'Dataset.xlsx'

# Load spreadsheet
xl = pd.ExcelFile(file)

# Print the sheet names
print(xl.sheet_names)

# Load a sheet into a DataFrame by name: df1
df = xl.parse('Phishing')

#Feature: Existence of the “@” symbol
df['@_Char_Phishing'] = pd.np.where(df.URL.str.contains("@"), "1",
                   pd.np.where(df.URL.str.contains(""), "0", "0"))

# new data frame with split value columns
df["URL"] = df["URL"].str.split("/", n = 1, expand = True)

#Feature: Existence of the “-” symbol
df['URL_Phishing'] = pd.np.where(df.URL.str.contains("-"), "1",
                   pd.np.where(df.URL.str.contains(""), "0", "0"))

#Feature: Existence of digit “1-9”
df['Digit_Phishing'] = pd.np.where(df.URL.str.contains("0"), "1", pd.np.where(df.URL.str.contains("1"), "1", pd.np.where(df.URL.str.contains("2"), "1", pd.np.where(df.URL.str.contains("3"), "1", pd.np.where(df.URL.str.contains("4"), "1", pd.np.where(df.URL.str.contains("5"), "1", pd.np.where(df.URL.str.contains("6"), "1", pd.np.where(df.URL.str.contains("7"), "1", pd.np.where(df.URL.str.contains("8"), "1", pd.np.where(df.URL.str.contains("9"), "1", pd.np.where(df.URL.str.contains(""), "0", "0")))))))))))

#output file
df.to_excel("Output_Dataset.xlsx")
