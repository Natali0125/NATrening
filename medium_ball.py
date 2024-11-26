students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
students.sort()
a = {}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
st_1 = float(sum(grades[0])/len(grades[0]))
st_2 =float(sum(grades[1])/len(grades[1]))
st_3 =float(sum(grades[2])/len(grades[2]))
st_4 =float(sum(grades[3])/len(grades[3]))
st_5 =float(sum(grades[4])/len(grades[4]))
a.update({students[0]: st_1,
          students[1]: st_2,
          students[2]: st_3,
          students[3]: st_4,
          students[4]: st_5})
print(a)