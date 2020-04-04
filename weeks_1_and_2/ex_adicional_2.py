seg = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dia = seg // 86400
dia_sobra = seg % 86400
horas = dia_sobra // 3600
horas_sobra = dia_sobra % 3600
minutos = horas_sobra // 60
seg_restante = horas_sobra % 60

print(dia,"dias",horas,"horas",minutos,"minutos e",seg_restante,"segundos.")
