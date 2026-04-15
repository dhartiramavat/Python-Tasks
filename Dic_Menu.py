emp_data={
    101:{"name":"Dharti","email":"Dharti@gmail.com","salary":50000,"city":"ahemdabad"},
    102:{"name":"Krupali","email":"Krupali@gmail.com","salary":28000,"city":"Rajkot"},
    103:{"name":"Archana","email":"Archana@gmail.com","salary":60000,"city":"ahemdabad"},
    

print(emp_data)

while True:

  print("1 Add Employee")

  print("2 Search Employee id")

  print("3 Display All Employee")

  print("4. Update Employee ")

  print("5. Delete")

  print("6. Search by Salary")

  print("7. Search by City ")

  print("5. Exit")

  choice=int(input("Enter choice "))

  match choice:
     case 1:
        emp_id=int(input("enter the employee id"));
        name=input("enter the name");
        email=input("enter the email");
        salary=int(input("enter the salary"));
        emp_data[emp_id]={"name":name,"email":email,"salary":salary}
        
        
        print(emp_data); 
      
     case 2:
         emp_id=int(input("enter the employee id"));
         for k,v in emp_data.items():
            if emp_id==k:
               for k1,v1 in v.items():
                  print(k1,v1)

     case 3:
         for k,v in emp_data.items():
            print(k)
            for k1,v1 in v.items():
                  print(k1,v1);          
    
     case 4:
        
        emp_id=int(input("enter the employee id"));

        if emp_id in emp_data.keys():
          newsalary=int(input("enter the salary"));
          emp_data[emp_id]["salary"]=newsalary
        print(emp_data[emp_id])
        
     case 5:
        emp_id=int(input("enter the employee id"));
        del emp_data[emp_id]
        print("succesfully deleted")
        print(emp_data)
        
     case 6:
        gsalary=int(input("enter the salary"));

        for k,v in emp_data.items():
           if v["salary"] == gsalary:
              print(k,v)

     case 7:
        city=int(input("enter the city"));

        for k,v in emp_data.items():
           if v["salary"] == city:
              print(k,v)
                  
     case 8:   break          
          
                 
}  