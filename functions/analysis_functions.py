import importsFile as imf

dataFram = ""
# reading the file (CSV, JSON)
def CSVFileReading(path):
    global dataFram
    dataFrame = imf.pd.read_csv(path)
    return dataFrame

def start(char, x, y, hue):
    # imf.pl.style.use('grayscale')
    # imf.pl.figure(figsize=(8, 5))
    # ax = imf.sns.countplot(x = x, data = CSVFileReading(imf.func.fileChoicedPath), palette="rocket_r")
    # ax.set_title("TITLE")
    # ax.set_xlabel(x)
    # ax.set_ylabel(y)
    # imf.pl.show()

    ax = imf.sns.jointplot(x = x, y=y, data=CSVFileReading(imf.func.fileChoicedPath), kind=char, hue=hue)
    imf.pl.show()
    

def dataAnalysisPage():
    def runAnalysis():
        char = comboboxChar.get()
        xVal = x.get()
        yVal = y.get()
        hueVal = hue.get()
        start(char, xVal, yVal, hueVal)
    analysisPage = imf.Toplevel()
    analysisPage.title("Analysis Page")
    analysisPage.geometry("900x700")

    img = "analysis.png"

    mainFrame = imf.ctk.CTkFrame(analysisPage)
    mainFrame.pack(side="top", fill="both", expand=True)

    mainFrame.rowconfigure(0, weight=1)
    mainFrame.rowconfigure(1, weight=1)
    mainFrame.rowconfigure(2, weight=1)
    mainFrame.rowconfigure(3, weight=1)

    mainFrame.columnconfigure(0, weight=1)
    mainFrame.columnconfigure(1, weight=1)
    mainFrame.columnconfigure(2, weight=1)

    frameOne = imf.ctk.CTkFrame(mainFrame)
    frameTwo = imf.ctk.CTkFrame(mainFrame)
    frameThree = imf.ctk.CTkFrame(mainFrame)
    frameFoure = imf.ctk.CTkFrame(mainFrame)

    frameOne.grid(row=0, column=0, columnspan=3, sticky="news")
    frameTwo.grid(row=1, column=0, columnspan=3, sticky="news")
    frameThree.grid(row=2, column=0, columnspan=3, sticky="news")
    frameFoure.grid(row=3, column=0, columnspan=3, sticky="news")

    #========[Frame One]===
    chartImage = imf.Image.open(f"files/images/CHARTS/{img}").resize((250, 250))
    chartImageTk = imf.ImageTk.PhotoImage(chartImage)
    chartImageLabel = imf.ctk.CTkLabel(mainFrame, image=chartImageTk)
    chartImageLabel.grid(row=0, column=1)


    #=========[Frame Two]===
    frameTwo.rowconfigure(0, weight=1)
    frameTwo.rowconfigure(1, weight=1)

    frameTwo.columnconfigure(0, weight=1)
    frameTwo.columnconfigure(1, weight=1)
    frameTwo.columnconfigure(2, weight=1)
    frameTwo.columnconfigure(3, weight=1)

    charLabel = imf.ctk.CTkLabel(frameTwo, text="TEST")

    comboboxChar = imf.ctk.CTkComboBox(frameTwo, values=["", "scatter", "hist", "hex", "kde", "reg", "resid"], width=200)
    dataFrame = CSVFileReading(imf.func.fileChoicedPath)

    columns = []
    for co in dataFrame.columns:
        columns.append(co)
    x = imf.ctk.CTkComboBox(frameTwo, values=columns, width=200)
    y = imf.ctk.CTkComboBox(frameTwo, values=columns, width=200)
    hue = imf.ctk.CTkComboBox(frameTwo, values=columns, width=200)
    
    charLabel.grid(row=0, column=1)
    comboboxChar.grid(row=1, column=0)
    x.grid(row=1, column=1)
    y.grid(row=1, column=2)
    hue.grid(row=1, column=3)


    #========[frameThree]===
    frameThree.columnconfigure(0, weight=1)
    frameThree.columnconfigure(1, weight=1)
    frameThree.columnconfigure(2, weight=1)

    startButton = imf.ctk.CTkButton(frameThree, text="Start", command=runAnalysis)
    startButton.grid(row=0, column=1, pady=50)