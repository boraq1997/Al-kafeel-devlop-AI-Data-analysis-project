import importsFile as imf 


# Global variables to store file paths
fileChoicedPath = ""

# upload file function 
def browseFile():
     filename = imf.filedialog.askopenfilename(initialdir="/", title="Select a csv file", filetypes=(("CSV files", "*.csv*"), ("json file", "*.json*")))
     return filename

def choiceFile():
     global fileChoicedPath
     fileChoicedPath = browseFile()
     if fileChoicedPath:
        print(fileChoicedPath)
        showDataFrameTable()
        
     
def loadData(theFile):
    dataFream = imf.pd.read_csv(theFile)
    return dataFream
 

# this function run on click of exit button in side bar
def exitButton():
    exit()

def applicationInfoButton():
    print(fileChoicedPath)

def settingsButton(root):
    settingsWindow = imf.Toplevel(root)
    settingsWindow.title("settings page")
    settingsWindow.geometry("500x400")

def showDataFrameTable():
    dataFrameTable = imf.Tk()
    dataFrameTable.title("DATA FRAME")
    dataFrameTable.geometry("900x700")

    dataFrameTable.rowconfigure(0, weight=3)
    dataFrameTable.rowconfigure(1, weight=1)

    dataFrameTable.columnconfigure(0, weight=1)
    dataFrameTable.columnconfigure(1, weight=1)
    dataFrameTable.columnconfigure(2, weight=1)

    tableFrame = imf.Frame(dataFrameTable)
    tableFrame.grid(row=0, column=0, sticky="news", columnspan=3)

    dataFrame = imf.af.CSVFileReading(fileChoicedPath)

    columnData = {'names': [], 'types': [], 'emptyColumns': [], 'redundantData': []}
    for column in dataFrame.columns:
     columnData['names'].append(column)
     columnData['types'].append(dataFrame[column].dtypes)
     columnData['emptyColumns'].append(dataFrame[column].isnull().sum())
     columnData['redundantData'].append(len(dataFrame[column].value_counts()))

    table = imf.ttkbootstrap.Treeview(
        tableFrame,
        bootstyle='info',
        show='headings',
        columns=('Name', 'Type', 'emptyColumns', 'redundantData')
        )
    table.heading('Name', text="Name")
    table.heading('Type', text="Type")
    table.heading('emptyColumns', text="emptyColumns")
    table.heading('redundantData', text="redundantData")
    table.pack(side="top", fill="both", expand=True)

    for i in range(len(columnData['names'])):
        table.insert("", "end", values=(
            columnData['names'][i],
            columnData['types'][i],
            columnData['emptyColumns'][i],
            columnData['redundantData'][i]
        ))

    fileInfoFrame = imf.Frame(dataFrameTable, background="red")
    fileInfoFrame.grid(row=1, column=0, sticky="news", columnspan=3)

    #=={FILE INFO}
    fileName = ""
    filePath = ""
    columnsCount = ""
    rowCount = ""
    emptyRows = ""
    emptyColumns = ""
    