import importsFile as imf

df = imf.pd.read_csv("C:/Users/archive-first/Desktop/superstore_data.csv")

print(df.round())
print(df.clip())











# print(len(df['Year_Birth'].value_counts()))
# print(df.isnull().sum())
# print(df['Year_Birth'].sum())
# print(df['Year_Birth'].dtypes)

# columnData = {'names': [], 'types': [], 'emptyColumns': [], 'redundantData': []}
# for column in df.columns:
#     columnData['names'].append(column)
#     columnData['types'].append(df[column].dtypes)
#     columnData['emptyColumns'].append(df[column].isnull().sum())
#     columnData['redundantData'].append(len(df[column].value_counts()))


# root = imf.Tk()
# root.geometry("800x700")


# table = imf.ttkbootstrap.Treeview(root, columns=("names", "types", "empty", "rend"), bootstyle='info', show='headings')
# table.heading("names", text="names")
# table.heading("types", text="types")
# table.heading("empty", text="empty")
# table.heading("rend", text="rend")


# data = []
# for i in range(len(columnData['names'])):
#     table.insert("", "end", values=(columnData["names"][i], columnData["types"][i], columnData["emptyColumns"][i], columnData["redundantData"][i]))
# table.pack(side="top", fill="both", expand=True)
# data = (("boraq", "ali"), "man", "null", False)
# print(type(data))
# table.insert(parent='', index=0, values=data)
# data = ("ali", "man", "null", False)
# table.insert(parent='', index=0, values=data)
# table.insert(parent='', index=0, values=data)

# root.mainloop()


