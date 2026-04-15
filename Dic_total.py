# Task 1
emp_data={
    "name":"Dharti",
    "age":"25",
    "marks":[500,220,400],
    
},{
    "name":"krupali",
    "age":"22",
    "marks":[250,150,190],
},{
    "name":"Archana",
    "age":"23",
    "marks":[150,160,130],
}
for v in emp_data:
    v['total_marks']=sum(v['marks'])
    
print(emp_data)



# Task 2
emp_data=[{
    "name":"Dharti",
    "age":"25",
    "incentive":[180,200,4000],
    "salary":9000
},
{
    "name":"Krupali",
    "age":"22",
    "incentive":[190,1500,2200],
    "salary":18000
}
]
for i in emp_data:
    i['total_salary']=sum(i['incentive'],i['salary'])

print(emp_data)


