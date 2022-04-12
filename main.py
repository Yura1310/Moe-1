temp_above_80 = 0

daily_temp_c = [20.5, 19, 15, 25, 27, 30, 31, 29, 26, 21,
                19, 25, 27.5, 28, 26, 29.5, 31, 27.5, 26, 29,
                18, 17.5, 17, 16.5, 19, 20, 25, 26.5, 27, 28,
                20.5, 19, 25, 27.5, 28, 26, 15, 25, 27, 28]


temp_c = 5/9 * (80-32)
print(temp_c)
for i in daily_temp_c:
  if i >= temp_c:
    temp_above_80 +=1
print(temp_above_80)


