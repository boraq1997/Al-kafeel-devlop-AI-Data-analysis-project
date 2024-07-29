import importsFile as imf

fileChoicedPath = ""

def callSettingsFunction():
    imf.func.settingsButton(root)

# get json file
settingsFile = open("files/settings/settings.json")
settings = imf.json.load(settingsFile)

theme = 'dark' if settings['SETTINGS']['THEME'] == "" else settings['SETTINGS']['THEME']
root = imf.Tk()
root.title("data analysis")
root.geometry("1000x700")
root.option_add("*tearOff", False)
root.resizable(False, False)

style = imf.ttk.Style(root)
root.tk.call("source", f"forest-{theme}.tcl")
style.theme_use(f"forest-{theme}")

icon_path = 'files/images/logo.ico'
icon = imf.Image.open(icon_path)
icon = imf.ImageTk.PhotoImage(icon)
root.iconphoto(True, icon)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.columnconfigure(4, weight=1)

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)

#===[SIDE BAR]==
sideBar = imf.ttk.Frame(root)

sideBarHomeIco = imf.Image.open("files/images/home.png").resize((30, 30))
sideBarAboutusIco = imf.Image.open("files/images/information-button.png").resize((30, 30))
sideBarSettingsIco = imf.Image.open("files/images/settings.png").resize((30, 30))
sideBarAppInfoIco = imf.Image.open("files/images/curriculum-vitae.png").resize((30, 30))
sideBarExitIco = imf.Image.open("files/images/logout.png").resize((30, 30))

sideBarHomeIco = imf.ImageTk.PhotoImage(sideBarHomeIco)
sideBarAboutusIco = imf.ImageTk.PhotoImage(sideBarAboutusIco)
sideBarSettingsIco = imf.ImageTk.PhotoImage(sideBarSettingsIco)
sideBarAppInfoIco = imf.ImageTk.PhotoImage(sideBarAppInfoIco)
sideBarExitIco = imf.ImageTk.PhotoImage(sideBarExitIco)

sideBarHomeBtn = imf.ttk.Button(sideBar, text="HOME", image=sideBarHomeIco, compound=imf.LEFT).pack(fill="x", pady=5)
sideBarAboutusBtn = imf.ttk.Button(sideBar, text="ABOUT US", image=sideBarAboutusIco, compound=imf.LEFT).pack(fill="x", pady=5)
sideBarSettingsBtn = imf.ttk.Button(sideBar, text="SETTINGS", image=sideBarSettingsIco, compound=imf.LEFT, command=callSettingsFunction).pack(fill="x", pady=5)
sideBarAppInfoBtn = imf.ttk.Button(sideBar, text="APPLICATION INFO", image=sideBarAppInfoIco, compound=imf.LEFT, command=imf.func.applicationInfoButton).pack(fill="x", pady=5)
sideBarExitBtn = imf.ttk.Button(sideBar, text="EXIT", image=sideBarExitIco, compound=imf.LEFT, command=imf.func.exitButton).pack(fill="x", pady=5, side="bottom")

#===[MAIN SECTION]==
mainSection = imf.ttk.Frame(root)
mainHeader = imf.ttk.Frame(mainSection)
mainBody = imf.ttk.Frame(mainSection)

headerImage = imf.Image.open("files/images/analysis.png").resize((250, 250))
heaerImageTk = imf.ImageTk.PhotoImage(headerImage)
headerImageLabel = imf.ttk.Label(mainHeader, image=heaerImageTk)

headerLabelText = "Welcome back to this program. \n You can do some logical analyzes related to your company or work by uploading files related to your work, \n so that some analyzes can be done. For more information, go to the application overview page."
headerLabel = imf.ttk.Label(mainHeader, text=headerLabelText, font=("arial", 12))

bodyBtnImage = imf.Image.open("files/images/uploade.png").resize((30, 30))
bodyBtnImageTk = imf.ImageTk.PhotoImage(bodyBtnImage)

bodyChoiceButton = imf.ttk.Button(mainBody, text=f"Choice File", image=bodyBtnImageTk, compound=imf.LEFT, command=imf.func.choiceFile)
bodyExtensionsAllowedLabel = imf.ttk.Label(mainBody, text="files extensions allowed is (csv, json)")
# #GRIDS
mainSection.columnconfigure(0, weight=1)
mainSection.columnconfigure(1, weight=1)
mainSection.columnconfigure(2, weight=1)
mainSection.rowconfigure(0, weight=1)
mainSection.rowconfigure(1, weight=3)

#DISPLAY
sideBar.grid(row=0, column=0, rowspan=5, sticky="news", padx=10, pady=10) #root
mainSection.grid(row=0, column=1, rowspan=5, columnspan=4, sticky="news", pady=10) #root
mainHeader.grid(row=0, column=0, columnspan=4, sticky="news") #mainSection
mainBody.grid(row=1, column=0, columnspan=4, sticky="news") #mainSection
headerImageLabel.pack(padx=0, pady=0)
headerLabel.pack(pady=30)
bodyChoiceButton.pack()
bodyExtensionsAllowedLabel.pack()


#===[FOOTER FRAME]==
root.mainloop()
