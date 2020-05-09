DJRTSHARE
=========

Introduction
^^^^^^^^^^^^

A Real time text sharing system using django and channels.


Requirements
^^^^^^^^^^^^

- Python 3.6
- Django 3.0.4
- channels 2.4.0

Installation
^^^^^^^^^^^^

- Installing system requirements
      
  **Debian/Ubuntu**
          
    ::
       
       sudo apt-get install redis-server
      
      
  **Centos/RedHat**
          
    ::
          
       sudo yum install redis-server

- Start redis server
    
  **Debian/Ubuntu**
          
    ::
       
        sudo service redis-server start
      
      
  **Centos/RedHat**
          
    ::
          
        sudo systemctl start redis
  
-  Clone the repository

   ::

     git clone https://github.com/adityacp/DJRTSHARE.git

-  Go to the project directory

   ::

     cd DJRTSHARE


- Installing project packages

  ::

     pip install -r requirements.txt


- Create superuser

  ::

     python manage.py createsuperuser

- Run migrations
  
  ::
      
     python manage.py migrate


- Run server Locally
      
  ::

     python manage.py runserver

Now go to 127.0.0.1:8000/share and start creating a room
