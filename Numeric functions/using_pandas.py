import pandas as pd
sales_df=pd.read_excel('D:/Codebasics/Data Analyics/Excel/Sales.xlsx')
sales_df.head()
# count of values in all columns
print(f"count of values in OrderId column :{sales_df['OrderID'].count()}")
print(f"count of values in ProductID column :{sales_df['ProductID'].count()}")
print(f"count of values in ProductName column :{sales_df['ProductName'].count()}")
print(f"count of values in Quantity column :{sales_df['Quantity'].count()}")
print(f"count of values in UnitPrice column :{sales_df['UnitPrice'].count()}")
print(f"count of values in Discount column :{sales_df['Discount'].count()}")
# sum of values in numeric columns
print(f"Sum of values in Quantity column :{sales_df['Quantity'].sum()}")
print(f"Sum of values in UnitPrice column :{sales_df['UnitPrice'].sum()}")
print(f"Sum of values in Discount column :{sales_df['Discount'].sum()}")
# Maximum values in numeric columns
print(f"Maximum value in Quantity column :{sales_df['Quantity'].max()}")
print(f"Maximum value in UnitPrice column :{sales_df['UnitPrice'].max()}")
print(f"Maximum value in Discount column :{sales_df['Discount'].max()}")
# Minimum values in numeric columns
print(f"Minimum value in Quantity column :{sales_df['Quantity'].min()}")
print(f"Minimum value in UnitPrice column :{sales_df['UnitPrice'].min()}")
print(f"Minimum value in Discount column :{sales_df['Discount'].min()}")
# Average values in numeric columns
print(f"Average value in Quantity column :{sales_df['Quantity'].mean()}")
print(f"Average value in UnitPrice column :{sales_df['UnitPrice'].mean()}")
print(f"Average value in Discount column :{sales_df['Discount'].mean()}")
