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
    dataFrameTable = imf.Toplevel()
    dataFrameTable.title("DATA FRAME")
    dataFrameTable.geometry("900x700")

    dataFrameTable.rowconfigure(0, weight=2)
    dataFrameTable.rowconfigure(1, weight=2)
    # dataFrameTable.rowconfigure(2, weight=1)

    dataFrameTable.columnconfigure(0, weight=1)
    dataFrameTable.columnconfigure(1, weight=1)
    dataFrameTable.columnconfigure(2, weight=1)

    #===[BUTTONS]==
    buttonsFrame = imf.ttkbootstrap.Frame(dataFrameTable)
    buttonsFrame.grid(row=0, column=0, sticky="news", columnspan=3)

    buttonsFrame.columnconfigure(0, weight=1)
    buttonsFrame.columnconfigure(1, weight=1)
    buttonsFrame.columnconfigure(2, weight=1)

    startAnalysis = imf.ctk.CTkButton(buttonsFrame, text="Start Analysis", command=dataAnalysisButton)
    startAnalysis.grid(row=0, column=1)

    #===[DATA FRAME TABLE]==
    tableFrame = imf.Frame(dataFrameTable, background="red")
    tableFrame.grid(row=1, column=0, sticky="news", columnspan=3)

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
    # table.grid(row=0, column=0, columnspan=3, sticky="news")

    for i in range(len(columnData['names'])):
        table.insert("", "end", values=(
            columnData['names'][i],
            columnData['types'][i],
            columnData['emptyColumns'][i],
            columnData['redundantData'][i]
        ))

    fileInfoFrame = imf.Frame(dataFrameTable)
    fileInfoFrame.grid(row=2, column=0, sticky="news", columnspan=3)

    fileInfoFrame.rowconfigure(0, weight=3)
    fileInfoFrame.rowconfigure(1, weight=1)

    fileInfoFrame.columnconfigure(0, weight=5)
    fileInfoFrame.columnconfigure(1, weight=2)

    #=={FILE INFO}
    fileName = imf.os.path.basename(fileChoicedPath)
    filePath = fileChoicedPath
    columnsCount = format(dataFrame.shape[1])
    rowCount = format(dataFrame.shape[0])
    emptyRows = ""
    emptyColumns = ""

    fileInfoTable = imf.ttkbootstrap.Treeview(fileInfoFrame, show="headings", bootstyle="info", columns=('name', 'value'))
    fileInfoTable.heading("name", text="Name")
    fileInfoTable.heading("value", text="Value")
    # fileInfoFrame.pack(side="left", fill="both", expand=True)
    fileInfoTable.grid(row=1, column=0, columnspan=2, rowspan=1, sticky="news", pady=30)

    fileInfoTable.column("name", width=30)

    fileInfoTable.insert("", "end", values=("FIle Path", filePath))
    fileInfoTable.insert("", "end", values=("fileName", fileName))
    fileInfoTable.insert("", "end", values=("Columns Count", columnsCount))
    fileInfoTable.insert("", "end", values=("Rows Count", rowCount))

def dataAnalysisButton():
    imf.af.dataAnalysisPage()