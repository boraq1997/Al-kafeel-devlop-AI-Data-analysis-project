import importsFile as imf 


# Global variables to store file paths
file = None

# upload file function 
def browseFile():
     filename = imf.filedialog.askopenfilename(initialdir="/", title="Select a csv file", filetypes=(("json file", "*.json*"), ("CSV files", "*.csv*")))
     return filename

def onClick():
     selectedFile = browseFile()
     if selectedFile:
        global file
        file = loadData(selectedFile)

        for head in imf.af.getColumnNames(file):
            # imf.ttk.Treeview.heading(head, text=head)
            print(head)
        
     
def loadData(theFile):
    dataFream = imf.pd.read_csv(theFile)
    return dataFream
 