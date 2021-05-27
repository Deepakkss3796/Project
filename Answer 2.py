dict1={
    "1": "name1",
    "2": "name2",
    "3": "name3",
    "4": "name5",
    "5": "name6"
}
dict2={
    "1": 30,
    "2": 40,
    "3": 70,
    "4": 50,
    "5": 55
}
def maxi(d):
    d1={}
    max_value=0
    max_key=""
    for item in d:
        if d[item]>max_value:
            max_value=d[item]
            max_key=item
    d1[max_key]=max_value
    return d1
print(maxi(dict2))