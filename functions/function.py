import importsFile as imf 

# upload file function 
def fileUpload():
    path = imf.filedialog.askopenfilename()
    if path:
        print(path)