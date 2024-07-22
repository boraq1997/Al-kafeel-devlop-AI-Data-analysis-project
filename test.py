import importsFile as imf

df = imf.pd.read_csv("C:/Users/archive-first/Desktop/superstore_data.csv")
# print(len(df['Year_Birth'].value_counts()))
# print(df.isnull().sum())
# print(df['Year_Birth'].sum())
# print(df['Year_Birth'].dtypes)

columnData = {'names': [], 'types': [], 'emptyColumns': [], 'redundantData': []}
for column in df.columns:
    columnData['names'].append(column)
    columnData['types'].append(df[column].dtypes)
    columnData['emptyColumns'].append(df[column].isnull().sum())
    columnData['redundantData'].append(len(df[column].value_counts()))


root = imf.Tk()
root.geometry("800x700")


table = imf.ttkbootstrap.Treeview(root, columns=("names", "types", "empty", "rend"), bootstyle='info', show='headings')
table.heading("names", text="names")
table.heading("types", text="types")
table.heading("empty", text="empty")
table.heading("rend", text="rend")
table.pack()

data = []
for col in columnData:
    for name in columnData[col]:
        data = (name)
        print(type(data))
        
data = (("boraq", "ali"), "man", "null", False).insert(parent='', index=0, values=data)
data = ("ali", "man", "null", False).insert(parent='', index=0, values=data)
# table.insert(parent='', index=0, values=data)

root.mainloop()
