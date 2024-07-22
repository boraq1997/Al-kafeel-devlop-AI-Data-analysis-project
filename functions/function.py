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

    dataFrame = imf.af.CSVFileReading(fileChoicedPath)




    columnData = {'names': [], 'types': [], 'emptyColumns': [], 'redundantData': []}
    for column in dataFrame.columns:
     columnData['names'].append(column)
     columnData['types'].append(dataFrame[column].dtypes)
     columnData['emptyColumns'].append(dataFrame[column].isnull().sum())
     columnData['redundantData'].append(len(dataFrame[column].value_counts()))



#     columnData = []
#     for column in dataFrame.columns:
#         columnData.append(column)

      
    table = imf.ttkbootstrap.Treeview(
        dataFrameTable,
        bootstyle='info',
        show='headings',
        columns=('Name', 'Type', 'emptyColumns', 'redundantData')
        )
    table.heading('Name', text="Name")
    table.heading('Type', text="Type")
    table.heading('emptyColumns', text="emptyColumns")
    table.heading('redundantData', text="redundantData")
    table.pack(fill="both")

    for names in dataFrame['names']:
        data = (col['names'])

    table.insert(parent='', index=0, values=data)
#     print(columnData)


# rows['Name', 'type', 'empty_rows',...]