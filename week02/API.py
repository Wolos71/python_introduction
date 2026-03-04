import requests
import json

url = "https://py10-day2-577570284557.europe-west1.run.app"

response = requests.get("https://py10-day2-577570284557.europe-west1.run.app/ex5/get-tables")
res = response.json()
# print(type(res))
print(res)

flag = {}
values = {}


for t in res:
    print(t)
    columnsRes = requests.post("https://py10-day2-577570284557.europe-west1.run.app/ex5/get-columns", json={"table": t})
    columns = columnsRes.json()
    print(columns)

    rowCountRes = requests.post("https://py10-day2-577570284557.europe-west1.run.app/ex5/get-row-count", json={"table": t})
    print(rowCountRes.json())
    rowCount = rowCountRes.json()["row_count"]
    print(rowCount)


    if t == "flag":
        for row in range(rowCount):
            for c in columns:
                value = requests.post("https://py10-day2-577570284557.europe-west1.run.app/ex5/get-entry", json=
                                        {
                                            "table": "flag",
                                            "row": row,
                                            "column": c
                                            })
                print(value.json())



        # for row in range(rowCount):
        #     for c in columns:
        #         value = requests.post("https://py10-day2-577570284557.europe-west1.run.app/ex5/get-entry", json=
        #                                 {
        #                                     "table": t,
        #                                     "row": row,
        #                                     "column": c
        #                                     })
        #         print(value.json())



# q = requests.post("https://py10-day2-577570284557.europe-west1.run.app/ex5/get-columns", json= {"table": "quotes"} )
# resq = q.json()
# print(resq)

# j = requests.post("https://py10-day2-577570284557.europe-west1.run.app/ex5/get-columns", json= {"table": "jokes"} )
# resj = j.json()
# print(resj)

# f = requests.post("https://py10-day2-577570284557.europe-west1.run.app/ex5/get-columns", json= {"table": "flag"} )
# resf = f.json()
# print(resf)