import importsFile as imf

dataFram = ""
# reading the file (CSV, JSON)
def CSVFileReading(path):
    global dataFram
    dataFrame = imf.pd.read_csv(path)
    return dataFrame

def dataAnalysisPage():
    analysisPage = imf.Tk()
    analysisPage.title("Analysis Page")
    analysisPage.geometry("900x700")

    