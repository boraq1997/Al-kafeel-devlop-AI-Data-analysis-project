import importsFile as imf

dataFram = ""
# reading the file (CSV, JSON)
def CSVFileReading(path):
    global dataFram
    dataFrame = imf.pd.read_csv(path)
    return dataFrame

def dataAnalysisPage():
    analysisPage = imf.Toplevel()
    analysisPage.title("Analysis Page")
    analysisPage.geometry("900x700")

    analysisPage.rowconfigure(0, weight=1)
    analysisPage.rowconfigure(1, weight=1)
    analysisPage.rowconfigure(2, weight=1)
    analysisPage.rowconfigure(3, weight=1)

    analysisPage.columnconfigure(0, weight=1)
    analysisPage.columnconfigure(1, weight=1)
    analysisPage.columnconfigure(2, weight=1)

    img = "analysis.png"
    def test():
        img = "bar-chart.png"

    mainFrame = imf.ctk.CTkFrame(analysisPage)
    mainFrame.grid(row=0, column=0, columnspan=3, rowspan=4, sticky="news")

    chartImage = imf.Image.open(f"files/images/CHARTS/{img}").resize((250, 250))
    chartImageTk = imf.ImageTk.PhotoImage(chartImage)
    chartImageLabel = imf.ctk.CTkLabel(mainFrame, image=chartImageTk)

    chartImageLabel.pack(padx=0, pady=0)

    button = imf.ctk.CTkButton(mainFrame, text="TEST", command=test).pack()