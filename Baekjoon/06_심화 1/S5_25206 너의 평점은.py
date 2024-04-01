scoreList = {'A+':'4.5','A0':'4.0','B+':'3.5','B0':'3.0',
             'C+':'2.5','C0':'2.0','D+':'1.5','D0':'1.0',
             'F':'0.0'}
scoreSum = 0
gradeSum = 0

for i in range(20):
    subject, score, grade = map(str,input().split())
    if grade == 'P':
        continue
    else:
        scoreSum += float(score)
        gradeSum += float(score) * float(scoreList[grade])

print(gradeSum/scoreSum)
