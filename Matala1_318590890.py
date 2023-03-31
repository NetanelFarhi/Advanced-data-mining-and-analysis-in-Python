
# Netanel Farhi .
# ID 318590890

### Answer Q1

def my_func(x1,x2,x3):
    list_parameters=[x1,x2,x3]
    if  any(isinstance(x, (list, str)) for x in list_parameters):
            return None
    elif not all(isinstance(x, float) for x in list_parameters):
            print( "parameters should be float")
        # If the parameters have been inserted correctly :
    else:
        nominator = (x1 + x2 + x3) * (x2 + x3) * x3
        denominator = x1 + x2 + x3
        if denominator != 0:
            result = float(nominator / denominator)
            return result
        if denominator == 0:
            print("Not a number - denominator equals zero")
#answer=my_func(1,-0.5,-0.5)
#print(answer)

# Answer Q2
def revword(word:str)->str:
    return word[::-1].lower()
#print(revword("tsriF"))
def countword()->int:
    corrected_content=""
    file = open('text.txt', 'r')
    lines = file.read().splitlines()
    word = lines[0].lower()
    text = lines[1:]
    for i in range(0,len(text)):
        splitted_row=text[i].split()
        for j in splitted_row:
          corrected_content=corrected_content+str(revword(j))+" "
        corrected_content=corrected_content+"\n"
    corrected_content=corrected_content.split()
    count=corrected_content.count(word)+1
    return count

#print(countword())



