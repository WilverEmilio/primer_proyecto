Pasos para crear el entorno virtual

1.	Abrir el visual estudio y dirigirse a un archivo .py
![image](https://github.com/user-attachments/assets/483de94c-6dc3-4ce5-a43c-9fa655335aa3)

2.	En la parte inferior del archivo .py, buscar donde dice la versión de Python
![image](https://github.com/user-attachments/assets/13af3440-707d-46ad-b446-54589057e0d0)
Nota: Darle click

3.	Seleccionar “Create Virtual Envionment” y seleccionar Venv
![image](https://github.com/user-attachments/assets/96319db0-f4df-4bcf-a7f8-b04253892a01)
Nota: Este crea un entorno virtual (Ver flecha verde)

4.	Ahora abrir un terminal y poner el siguiente comando (Sin las comillas)
“.venv\Scripts\activate.bat”
![image](https://github.com/user-attachments/assets/19350b9f-1c79-40c9-829a-e930e25babc4)
Este les encenderá el entorno virtual, ahora aparece (.venv)
![image](https://github.com/user-attachments/assets/ae392114-cb4f-43ca-91cd-b95d42f819a5)

5.	Instalar todo lo que se encuentra en el requeriments.txt
![image](https://github.com/user-attachments/assets/752b8f13-926d-4934-8543-78744ab340f0)

Poner el siguiente comando en la terminal donde activamos el entorno virtual (Sin las comillas)
“pip install -r requirements.txt”   

6.	Ya se puede trabajar en el proyecto
Ejecutar el comando (sin comillas)
“uvicorn app.main:app –reload”

7.	Si ya no se va a trabajar se debe de poner el siguiente comando en la terminal para desactivar el entorno virtual (Sin comillas)
“deactivate”
![image](https://github.com/user-attachments/assets/61daec8d-49c9-4260-8a2e-340c3d736948)



