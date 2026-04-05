name=input("What is your name? ")
classs=int(input("What is your class? "))
section=input("What is your section? ")
age=int(input("What is your age? "))
rollno=int(input("What is your roll number? "))
eng=int(input("What is your English marks? "))
math=int(input("What is your Math marks? "))
sci=int(input("What is your Science marks? "))
lang2=int(input("What is your second language marks? "))
soc=int(input("What is your Social marks? "))
ds=int(input("What is your Data science marks? "))
total=eng+math+sci+lang2+soc+ds
per=total*100/450
print(name,"of class",classs,section,"with roll number",rollno,"has scored",total,"marks with a percentage of",per    )