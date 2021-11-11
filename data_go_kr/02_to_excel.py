import pandas as pd

def save(df, filename):
    writer = pd.ExcelWriter(filename)
    df.to_excel(writer, "sheet1")
    writer.save()

df = pd.read_json("./nonPayment.json")

print(df.count())

save(df, "nonPayment.xlsx")

