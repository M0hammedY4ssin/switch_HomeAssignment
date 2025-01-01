''''
Create the deepClone function: 

  x = {a: "b", a2: ["first", "second"]};
  y = {b: x, b3: ["firtsY", x]};
  z = deepClone(y);  

def deepClone(obj) {}

'''

def deepClone(obj):
    if isinstance(obj,dict):
        cloned_dict = dict()
        for key,val in obj.items():
            cloned_dict[key]= deepClone(val)
        return cloned_dict
    elif isinstance(obj,list):
        cloned_list = list()
        for item in obj:
            cloned_list.append(deepClone(item))
        return cloned_list
    else:
        return obj

x = {"a": "b", "a2": ["first", "second"]}
y = {"b": x, "b3": ["firtsY", x]}
z = deepClone(y)

x["a"] = "modified"
y["b3"][0] = "modifiedList"

print("Original y:", y)
print("Cloned z  :", z)