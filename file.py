line_count1 = sum(1 for line in open('1.txt')) #количество строк в файле
line_count2 = sum(1 for line in open('2.txt'))
line_count3 = sum(1 for line in open('3.txt'))

if line_count1 > line_count2 and line_count1 > line_count3:
    print(line_count1)
    if line_count2 > line_count3:
        print(line_count2)
    else:
        print(line_count3)
elif line_count2 > line_count1 and line_count2 > line_count3:
    print(line_count2)
    if line_count1 > line_count3:
        print(line_count1)
    else:
        print(line_count3)
else:
    print(line_count3)
    if line_count1 > line_count2:
        print(f'{line_count1} \n{line_count2}')
    else:
        print(line_count2,line_count1)