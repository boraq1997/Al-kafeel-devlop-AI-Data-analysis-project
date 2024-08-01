# # import importsFile as imf

# # dataFrame = imf.pd.read_csv("C:/Users/archive-first/Desktop/aiProject/CSV'S/Online_Sales_Data.csv")

# # penguins = imf.sns.load_dataset("penguins")
# # imf.sns.histplot(data=penguins, x="Product_Category", hue="Date", multiple="stack")

# # # Transaction ID
# # # Date
# # # Product Category
# # # Product Name
# # # Units Sold
# # # Unit Price
# # # Total Revenue
# # # Region
# # # Payment Method


# import pandas as pd
# import numpy as np
# import seaborn as sns

# df = pd.read_csv("C:/Users/archive-first/Desktop/aiProject/CSV'S/Online_Sales_Data.csv")

# # print(df['Product Category'].describe())

# print(df.agg(['sum', 'count']))


# CTkTable Widget by Akascape
# License: MIT
# Author: Akash Bora

import customtkinter
from CTkTable import *

root = customtkinter.CTk()

value = [[1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5],
         [1,2,3,4,5]]

table = CTkTable(master=root, row=5, column=5, values=value)
table.pack(expand=True, fill="both", padx=20, pady=20)

root.mainloop()