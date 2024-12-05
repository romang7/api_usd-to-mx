bilbiotecas necesarias (descargar desde la terminal de pycharm):
{
pip install flask flask-cors requests apscheduler
pip install mysql-connector-python
pip install fastapi uvicorn requests

}

comando para ejecutar el servidor de la api:

uvicorn app:app --host 0.0.0.0 --port 8000 --reload

End point:

http://127.0.0.1:8000/api/usd-to-mxn


Ctrl + C    //Para matar el servidor