import os
import smtplib
import ssl
import mimetypes
from email.message import EmailMessage
def enviarCorreo(correo, nombre, esVehiculos):
    SERVIDOR = "in-v3.mailjet.com"
    PUERTO = 587
    DIRECCION_DE_ORIGEN = "jalvarezc38@miumg.edu.gt"
    USUARIO = os.getenv("Email_user")
    CONTRASENA = os.getenv("Email_secret")
    DIRECCION_DE_DESTINO = correo
    if esVehiculos:
        ASUNTO = "Reporte de vehiculos"
        MENSAJE = "los Reportes de los vehiculos"
    mensaje = EmailMessage()
    mensaje["From"] = DIRECCION_DE_ORIGEN
    mensaje["To"] = DIRECCION_DE_DESTINO
    mensaje["Subject"] = ASUNTO
    mensaje.set_content(MENSAJE)
    ruta = f"reportes/{nombre}.xlsx"
    ctype, encoding = mimetypes.guess_type(ruta)
    if ctype is None or encoding is not None:
        ctype = "application/octet-stream"
    tipo_principal, sub_tipo = ctype.split("/", 1)
    archivo = open(ruta , "rb")
    mensaje.add_attachment(archivo.read(), maintype= tipo_principal, subtype = sub_tipo, filename = ruta)
    contexto = ssl.create_default_context()
    with smtplib.SMTP(SERVIDOR, PUERTO) as servidor:
        servidor.starttls(context=contexto)
        servidor.login(USUARIO, CONTRASENA)
        servidor.send_message(mensaje)
    print("el Correo ah sido enviado")