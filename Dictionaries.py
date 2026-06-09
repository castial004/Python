# 1. Dictionaries are mutable, unordered, key value pair with no duplicate key type of data structure
# 2. keys can of any data type except none and list
# syntax
stud1 = {
    "name":"sahil",
    0:"key is a integer",
    1.1:"key is a float",
    True:"key is a boolean",
    False:"key is boolean false",
    (1,):"key is a tuple",
}
print(stud1)
print("-----------------------------------------------------------------------------")
# 3. you can add a new key value pair by 2 ways
stud1["newKey1"] = "newKey1 added" 
print(stud1)
stud1.update({"newKey2":"newKey2 added","newKey3":"newKey3 added"})
print(stud1)
print("difference is that using update u can add multiple key value pair at once")
print("-----------------------------------------------------------------------------")
# 4. you can update value of key using the existing key otherwise a new key will be created
stud1["name"] = "sahil mall"
print(stud1)
print("-----------------------------------------------------------------------------")
# 5. accessing value of a particular key there are two approaches to this
print("this is traditional approach: ",stud1["name"])
print("this is professional and accurate approach: ",stud1.get("name"))
print("difference is that if key doestnot exist .get() will return none where as traditional one will throw error and halts the code execution")
print("-----------------------------------------------------------------------------")
# 6. get all keys and all values and get all key value pairs using method
# i am casting them into a list for better visibility
print("get all keys: ",list(stud1.keys()))
print("get all values: ",list(stud1.values()))
print("get all key value pair: ",list(stud1.items()))
# 7. dictionaries also support nesting
nesting = {
    "name":"sahil mall",
    "score":{
        "maths":80,
        "dbms":70
    }
}
print(nesting.get("score").items())
print(nesting["score"])
print(nesting["score"]["maths"])