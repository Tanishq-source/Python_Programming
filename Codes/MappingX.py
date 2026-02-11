Information = {"Name" : "Rahul","Age" : 25,"City" : "Pune","Marks" : 89.90,"City" : "Mumbai"}  # Duplication of key is not allowed 
print(Information)

print(Information["City"])  # It will override the value pune and will print mumbai 

Information["Age"] = 26
print(Information)