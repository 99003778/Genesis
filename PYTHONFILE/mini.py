import re
count = 0
software = []
lines = 0
pattern = re.compile("software",re.IGNORECASE)
with open("input.txt",'rt' ) as file_info:
    for file_line in file_info:
        lines+=1
        if pattern.search(file_line) != None:
            software.append((lines,file_line.rstrip('\n')))
    for answer in software:
        count+=1
        #print(answer[1])
    #print("count=",count)
        with open("software.txt" , 'a') as file_answer:
            file_answer.writelines(str(count)+ ':')
            file_answer.writelines(answer[1]+'\n')


'''count = 0
license = []
lines = 0
pattern = re.compile("License",re.IGNORECASE)
with open("input.txt",'rt' ) as file_info:
    for file_line in file_info:
        lines+=1
        if pattern.search(file_line) != None:
            license.append((lines,file_line.rstrip('\n')))
    for answer in license:
        count += 1
        print(answer[1])
    print("count=",count)'''


'''file_store=[]
with open("output.txt",'rt') as text:
    for input_file in text:
        file_store.append(input_file.rstrip('\n'))
        for element in file_store:
            re.findall("software" , "output.txt")
with open("software" , answer) as file_answer:
    file_answer.writelines(str(count)+ ':')
    file_answer.writelines(answer[1]+'\n')'''
    