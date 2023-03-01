import csv

male = 0
female = 0
salary = 0
employees = []

with open('datos.csv' ,newline='') as csvfile:
    data = csv.reader(csvfile,delimiter=';')
    for value in data:

      if value[4] == 'M':
        female += 1

      if value[4] == 'H':
        male += 1

      if value[8] == 'Equilibrha IT' and value[9] == 'CT2':
        salary += int(value[6])

      if value[8] == 'Equilibrha RRHH' and int(value[6]) >= 28000:
        val = value[0], value[1], value[2], value[6], value[8]
        employees.append(val)


print('--------------- Punto 1 -------------------')    

print('Del total de empleados de la empresa',  male + female, 'son:')
print('hombres:', male)
print('mujeres:', female)

print('--------------- Punto 2 -------------------')    

print('Total salario bruto:', salary)

print('--------------- Punto 3 -------------------')
print('Id', ' ' ,'Nombre',' ','Apellido',' ','Salario',' ', 'Empresa')

for per in employees:
  print(per[0], per[1], per[2],per[3], per[4])

print('-------------------------------------------')