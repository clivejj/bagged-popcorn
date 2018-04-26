def checkPass(password):
    upper = [0 for val in password if val.isupper()]
    lower = [0 for val in password if val.islower()]
    num = [0 for val in password if val.isdigit()]
    return 0 in upper and 0 in lower and 0 in num

print checkPass("Ab1")
print checkPass("ab1")
print checkPass(")))")

def rate(password):
    upper = [1 for val in password if val.isupper()]
    lower = [1 for val in password if val.islower()]
    num = [1 for val in password if val.isdigit()]
    special = [1 for val in password if val in  ". ? ! & # , ; : - _ *"]
    arrs = [upper, lower, num, special]
    count = [10.0 * sum(arr) / len(password) for arr in arrs]
    #return count
    new_count = [2.5 if val > 2.5 else val for val in count]
    #return new_count
    return sum(new_count)



print rate("AAAAAAAAAAaaaaaaaaaaaaaaa11111&&&&&")
 
