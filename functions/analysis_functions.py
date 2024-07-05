import importsFile as imf

# reading the file (CSV, JSON)
def CSVFileReading(path, filename):
    file = "THIS MEAN THE PATH WITH FILE NAME"
    dataFrame = imf.pd.read_csv(file)
    return dataFrame

def rowsColumnLen(dataframe):
    return len(dataframe.axes[0]), len(dataframe.axes[1])

def getColumnNames(dataFrame):
    return dataFrame.head()