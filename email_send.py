import time
import smtplib

dia = (time.strftime("%d"))
mes = (time.strftime("%m"))
año = (time.strftime("%y"))

restadia = int(dia) - 1
fecha2 = str(restadia) + "/" + mes + "/" + año

mensaje = """Buen dia,

La red ha permanecido estable.

Saludos.
"""

asunto = "Reporte de actividades " + fecha2
mensaje = "Subject: %s\n\n%s"%(asunto, mensaje)
conexion = smtplib.SMTP("smtp.gmail.com", 587)
conexion.starttls()
conexion.login("xxxxxx@gmail.com", "password")
conexion.sendmail("xxxxxx@gmail.com", 'xxxxxxx@gmail.com', mensaje)
conexion.quit()

print("El correo se ha enviado con exito")
