import requests
import json

url = "***"

response = requests.get("***")
res = response.json()
# print(type(res))
print(res)


values = {}


for t in res:
    print(t)
    columnsRes = requests.post("***", json={"table": t})
    columns = columnsRes.json()
    print(columns)

    rowCountRes = requests.post("***", json={"table": t})
    print(rowCountRes.json())
    rowCount = rowCountRes.json()["row_count"]
    print(rowCount)


    if t == "flag":
        for row in range(rowCount):
            for c in columns:
                value = requests.post("***", json=
                                        {
                                            "table": "flag",
                                            "row": row,
                                            "column": c
                                            })
                

                entry = value.json()["entry"]

                if c == "character":
                    char = entry
                elif c == "index":
                    index = entry


            if char is not None and index is not None:
                values[index] = char

# print(values)

flaga = ""
klucze = list(values.keys())
klucze.sort()

for k in klucze:
    znak = values[k]
    flaga += znak

print(flaga)











        # for row in range(rowCount):
        #     for c in columns:
        #         value = requests.post("***", json=
        #                                 {
        #                                     "table": t,
        #                                     "row": row,
        #                                     "column": c
        #                                     })
        #         print(value.json())



# q = requests.post("***", json= {"table": "quotes"} )
# resq = q.json()
# print(resq)

# j = requests.post("***", json= {"table": "jokes"} )
# resj = j.json()
# print(resj)

# f = requests.post("***", json= {"table": "flag"} )
# resf = f.json()
# print(resf)