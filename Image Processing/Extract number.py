with open('C:/Users/Triton/Desktop/sample.txt',encoding='utf-8') as file:
    for line in file:
        num=re.findall('(?:\+[1-9]\d{0,2}[- ]?)?[1-9]\d{9}', line)
        
        with open('C:/Users/Triton/Desktop/gowtham_num_extraction2.0.txt','a') as fw:
            for item in num:
                fw.writelines('%s\n' % item)
                print('%s\n' % item)