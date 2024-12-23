Sdata={"Steven":["maths","english","science,17"],"Gavi":["maths","english","science,16"],"Pedri":["maths","english","science,18"],"Steven":["maths","english","science,17"]}
result={}
for key,value in Sdata.items():
    if value not in result.values():
        result[key]=value
print("The unique elements of the dictionary are",result)