#Find ascii using python
print ("Please enter the String: ", end = "")  
string = input()  
string_length = len(string)  
for K in string:  
    ASCII = ord(K)  
    print (K, "\t", ASCII)  