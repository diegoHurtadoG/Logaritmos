import random
import string

N_MIN = 4 #Minimo largo nombre usuario
N_MAX = 10 #Maximo largo nombre usuario
M_MIN = 10 #Minimo largo mail
M_MAX = 30 #Maximo largo mail

caracteres = string.ascii_letters + string.digits

def generar(n):
    file = open("L.txt", "w")
    names = []
    mails = []
    # Agrego n - 1 al archivo
    for i in range(n - 1):
        #Genero el nombre aleatorio
        name_buffer = ""
        for j in range(random.randint(N_MIN, N_MAX)):
            name_buffer = name_buffer + caracteres[random.randint(0, len(caracteres) - 1)]
        names.append(name_buffer)

        #Genero el mail aleatorio
        mail_buffer = ""
        mail_pre_comma = random.randint(1, M_MIN)
        for j in range(random.randint(M_MIN, M_MAX)):
            mail_buffer = mail_buffer + caracteres[random.randint(0, len(caracteres) - 1)]
            if len(mail_buffer) == mail_pre_comma:
                mail_buffer = mail_buffer + "@"
        mails.append(mail_buffer)

        # name_buffer y mail_buffer tienen nombre y mail
        file.write(name_buffer + " " + mail_buffer + "\n")

    #Aqui agrego el ultimo (para que no quede un espacio extra)

    #Genero el nombre aleatorio
    name_buffer = ""
    for j in range(random.randint(N_MIN, N_MAX)):
        name_buffer = name_buffer + caracteres[random.randint(0, len(caracteres) - 1)]
    names.append(name_buffer)

    #Genero el mail aleatorio
    mail_buffer = ""
    mail_pre_comma = random.randint(1, M_MIN)
    for j in range(random.randint(M_MIN, M_MAX)):
        mail_buffer = mail_buffer + caracteres[random.randint(0, len(caracteres) - 1)]
        if len(mail_buffer) == mail_pre_comma:
            mail_buffer = mail_buffer + "@"
    mails.append(mail_buffer)

    # name_buffer y mail_buffer tienen nombre y mail
    file.write(name_buffer + " " + mail_buffer)
    file.close()
    return names