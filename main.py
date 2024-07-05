import importsFile as imf

# get json file
settingsFile = open("files/settings/settings.json")
settings = imf.json.load(settingsFile)

theme = 'dark' if settings['SETTINGS']['THEME'] == "" else settings['SETTINGS']['THEME']

root = imf.Tk()
root.title("TITLE")
root.option_add("*tearOff", False)

# Make the app responsive
root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)
root.columnconfigure(index=2, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=1)
root.rowconfigure(index=2, weight=1)

style = imf.ttk.Style(root)
forest = "forest-"+theme+".tcl"
root.tk.call("source", f"forest-{theme}.tcl")
# Set the theme with the theme_use method
style.theme_use(f"forest-{theme}")

frame = imf.ttk.Frame(root)
frame.pack()

uploadFrame = imf.ttk.LabelFrame(frame, text="upload frame")
uploadFrame.grid(row=0, column=0)

getFile = imf.Button(uploadFrame, text="upload file", command=imf.func.fileUpload)
getFile.pack()
root.mainloop()