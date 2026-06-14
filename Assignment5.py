{
    "Name":"Marks"
}
{
  "Afreen": 67,
  "Alice": 78,
  "Bob": 89
}
name=input("Enter the name of the students:")
marks={"Afreen":67,"Alice":78,"Bob":89}
if name in marks:
    print(name,"has scored",marks[name],"marks")
else:
    print("Student not found")