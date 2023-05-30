try: 
    peso = float(input("Ingrese su peso corporal en KG: "))
    altura = float (input ("Ingrese su altura en METROS: "))
    print ("NO INGRESO UN VALOR VALIDO")
    alt2 = altura** 2
    IMC = peso/alt2
    print ("Para su peso: ", peso)
    print ("Con respecto a su altura: ", altura)
    print ("Su indice de masa corporal es: ", IMC)  
    if IMC<=18.4 :
        print ("USTED ESTA EN BAJO PESO")
    elif IMC>=18.5 and IMC<=24.9:
        print ("usted esta en un PESO NORMAL")
    elif IMC>=25 and IMC<=29.9:
        print ("Uste sufre de sobre peso ")
    elif IMC>=30 and IMC<=34.9:
        print ("Usted sufre obesidad tipo 1")
    elif IMC>=35 and IMC<=39.9:
        print ("usted sufre de obesidad tipo 2") 
    elif IMC>=40:
        print("usted sufre de obesidad tipo 3")
except ValueError:
    print ("ERROR: no agrego un valor valido D:")