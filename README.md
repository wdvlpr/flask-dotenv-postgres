# flask-dotenv-postgres

Modelo de projeto em Python ultilizando micro web framework Flask, variáveis de ambiente com dotenv (.env) e banco de dados PostgresSQL.

## Install

```cd ~```

```git clone https://github.com/wdvlpr/flask-dotenv-postgres.git flaskapp```

```cd ~/flaskapp```

```sudo ln -sT ~/flaskapp /var/www/html/flaskapp```

```sudo apt-get install apache2```

```sudo apt-get install python3```

```sudo apt-get install python3-pip```

```sudo apt-get install libapache2-mod-wsgi-py3```

```sudo systemctl restart apache2```

```pip3 install flask```

```pip3 install python-dotenv```

```pip3 install psycopg2-binary```

## Config

```sudo nano /etc/apache2/sites-available/000-default.conf```

Adicione o seguinte conteudo apos DocumentRoot /var/www/html

````
WSGIDaemonProcess flaskapp threads=5
WSGIScriptAlias / /var/www/html/flaskapp/app.wsgi
WSGIApplicationGroup %{GLOBAL}
<Directory flaskapp>
	 WSGIProcessGroup flaskapp
	 WSGIApplicationGroup %{GLOBAL}
	 Order deny,allow
	 Allow from all
</Directory>
````

## JavaScript - Fetch

````
var myHeaders = new Headers();
myHeaders.append("A-Api-Key", "asdewq321098");

var requestOptions = {
  method: 'GET',
  headers: myHeaders,
  redirect: 'follow'
};

fetch("127.0.0.1:5000", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
````