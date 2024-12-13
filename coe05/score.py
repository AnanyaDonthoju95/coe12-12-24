project=int(input("Enter project score:"))
internal=int(input("Enter internal score:"))
external=int(input("Enter external score:"))
if(project>50 & internal>50 & external>50):
    total=project*0.70 + internal*0.10 + external*0.20
    print(total)
elif(project>50,internal<50,external>50):
    print("you failed as your internal score is",internal)
elif(project<50,internal>50,external>50):
    print("you failed as your project score is",project)
elif(project>50,internal>50,external<50):
    print("you failed as your external score is:",external)