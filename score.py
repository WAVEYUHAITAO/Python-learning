score=66
level=('D' if 0<= score <60 else
       'C' if 60<= score <80 else
       'B' if 80<= score <90 else
       'A' if 90<= score <100 else
       'S' if score == 100 else
       "请输入 0~100 之间的分值^o^")
print(level)
