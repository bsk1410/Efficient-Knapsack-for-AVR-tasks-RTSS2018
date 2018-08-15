from pprint import pprint
diff = dict()
with open('DRTAlgOutput.txt') as file1, open('NewAlgOutput.txt') as file2:
    for line1, line2 in zip(file1, file2):
        p1 = line1.index('=')
        p2 = line2.index('=')
        p1c = line1.index(':')
        p2c = line2.index(':')

        if float(line1[p1+1:]) != float(line2[p2+1:]):
            diff[float(line1[p1c+1:p1-1])] = (float(line1[p1+1:]),float(line2[p2+1:]),float(line1[p1+1:])-float(line2[p2+1:]))
pprint(diff)
print('No. of mis-matches = ',len(diff))