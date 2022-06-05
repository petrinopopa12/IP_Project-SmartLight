# IP_Project-SmartLight
 
 
 
**Eclipse Mosquitto**

Eclipse Mosquitto este un broker de mesaje open source (cu licență EPL/EDL) care implementează versiunile 5.0, 3.1.1 și 3.1 ale protocolului MQTT. Mosquitto este ușor și poate fi utilizat pe toate dispozitivele, de la computere cu o singură placă de mică putere până la servere complete.

**Flask**

Flask este un framework web, un modul Python care permite să dezvoltam cu ușurință aplicații web. Are un nucleu mic și ușor de extins; este un microframework care nu include un ORM (Object Relational Manager) sau alte caracteristici similare.

**Pytest**

pytest facilitează scrierea de teste mici și ușor de citit și poate fi extins pentru a susține teste funcționale complexe pentru aplicații și biblioteci.



**Required versions:**
eventlet==0.33.1

Flask==2.1.2

Flask-MQTT==1.1.1

Flask-SocketIO==5.2.0

pytest==7.1.2

requests==2.27.1




**How to run:**

•	Install the indicated version of Mosquitto

•	Start a python console and run the following commands

    o	pip install -r requirements.txt
 
    o	python db_init.py
 
    o	python main.py
 
    o	python -m flask run
 
•	To run the tests use the following command in a python console

    o	python -m pytest -v
 
