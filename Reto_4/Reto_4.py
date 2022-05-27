def calcularCosto(alto,ancho,profundo):
    volumen = float(alto * ancho * profundo)
    costo = float(volumen*12)
    if (alto > 30):
        costo += 2000
        return costo
 
    if (costo > 10000):
        iva = float(costo* 0.19)
        costo = (costo + iva)
        return costo

print(calcularCosto(35,10,5))
