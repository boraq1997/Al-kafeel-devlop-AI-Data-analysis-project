import importsFile as imf

fileChoicedPath = ""

def callSettingsFunction():
    imf.func.settingsButton(root)

root = imf.tk.Tk()
root.title("data analysis")
root.geometry("1000x700")
root.option_add("*tearOff", False)
root.resizable(False, False)

style = imf.ttk.Style(root)
root.tk.call("source", f"forest-dark.tcl")
style.theme_use(f"forest-dark")

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

sideBar = imf.ttk.Frame(root).pack()

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

root.mainloop()