#Programa para calcular cantidades y precio CangreBrownies


entrada = int(input("\nBienvenido al programa CangreBrownies:\n\n1 para ir a la receta 'cookies and cream'\n2 para ir a la receta 'Pinguinos'\n3 para ir a la receta 'galletas'\n\nDigite su receta de hoy: "))


def BrowniesCaC(units):

    masa_unit = 30 #gr
    mantequilla_unit = 20 #gr
    galleta_unit = 1 #unidad
    chocolateB_unit = 18 #gr
    papelMantequilla_constant = 1 #1/8
    Esencia_Ingrediente = 1.4 #gr

    calculo_masa = masa_unit * units
    print(f"\nNecesitaremos: \n\n{calculo_masa} gr de masa para brownie")

    calculo_mantequilla = mantequilla_unit * units
    print(f"{calculo_mantequilla} gr de mantequilla")
    if units > 6:
        calculo_galleta = units / 6
        print(f"{round(calculo_galleta,1)} paquetes de galletas glasitas")
    else:
        calculo_galleta = galleta_unit * units
        print(f"{calculo_galleta} galletas glasitas")
    calculo_chocolateB = chocolateB_unit  * units
    print(f"{calculo_chocolateB} gr de chocolate blanco")
    
    calculo_papelM = print(f"{papelMantequilla_constant}/8 de papel mantequilla")

    calculo_OrangeH = Esencia_Ingrediente * units
    print(f"{round(calculo_OrangeH,1)} gr de Esencia Especial")

    #--------------------------------------Costos------------------------------------------------------------#
    print("\nCostos:")

    masa_valorXunit = (5800 / 340) * masa_unit 
    mantequillaXunit = (2000 / 500) * mantequilla_unit
    galletasXunit = (600 / 6) * galleta_unit
    chocolateBXunit = (6000 / 500) * chocolateB_unit
    papelMantequilla = 300

    CostoXmasa = masa_valorXunit * units
    print(f"\n{round(CostoXmasa)} Pesos en Masa haz de Oros ---> Paquete a '5.800'")
    CostoXmantequilla = mantequillaXunit * units 
    print(f"{round(CostoXmantequilla)} Pesos en Mantequilla industrial ---> libra a '2.000'")
    CostoXgalletas = galletasXunit * units
    print(f"{round(CostoXgalletas)} Pesos en galletas glasitas ---> paquete a '600.00'")
    CostoXchocolateB = chocolateBXunit * units
    print(f"{round(CostoXchocolateB)} Pesos en chocolate blanco ---> libra a '6.000'")
    print(f"{papelMantequilla} Pesos de papel mantequilla ----> 1/8 a '300.00'\n")

    Costo_total = CostoXmasa + CostoXmantequilla + CostoXchocolateB + CostoXgalletas + papelMantequilla
    print(f"Costo total estimado: {round(Costo_total)}\n")
    return True

if entrada == 1:
    BrowniesCaC(units = int(input("\nIngrese la cantidad de brownies cookies and cream a cocinar: ")))




