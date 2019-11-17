### Real Server Install Instruction

* Mysql 5.7

`apt update && sudo apt install mysql-server`

See the logs

```text
update-alternatives: using /etc/mysql/mysql.cnf 

to provide /etc/mysql/my.cnf (my.cnf) in auto mode

Renaming removed key_buffer and myisam-recover options (if present)

Created symlink /etc/systemd/system/multi-user.target.wants/mysql.service 

→ /lib/systemd/system/mysql.service.

```

* Setup mysql server configuration

* View the `deployments/mysqlconfig` directory

Restart mysql and see the current character settings:

```text
mysql> SHOW VARIABLES LIKE 'char%';
+--------------------------+----------------------------+
| Variable_name            | Value                      |
+--------------------------+----------------------------+
| character_set_client     | utf8mb4                    |
| character_set_connection | utf8mb4                    |
| character_set_database   | utf8mb4                    |
| character_set_filesystem | binary                     |
| character_set_results    | utf8mb4                    |
| character_set_server     | utf8mb4                    |
| character_set_system     | utf8                       |
| character_sets_dir       | /usr/share/mysql/charsets/ |
+--------------------------+----------------------------+
8 rows in set (0.00 sec)
```

#### Install python for flask in teko20

* Using available version of python on ubuntu 18 : `python3 -v` (3.6)

* Install pip `apt install python3-pip`

Install latest pip3 version 

```textmate
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py
ln -s /usr/local/bin/pip3 /usr/bin/pip3
```
* Link python

```textmate
ln -s /usr/bin/python3 /usr/bin/python
ln -s /usr/bin/pip3 /usr/bin/pip
```

* Install other packages

```text
pip install virtualenv 
apt install nginx
```

* Open port `vim /etc/sysconfig/iptables`

```text
### Port 80 and 443 for http
-A INPUT -p tcp -m tcp --dport 80 -j ACCEPT
-A INPUT -p tcp -m tcp --dport 443 -j ACCEPT
```

Restart `service netfilter-persistent restart`

Check to see if you can access `http://103.126.156.20/`

* Setup git

```text
ln -s /home/quandm/.ssh/id_rsa /root/.ssh/id_rsa
ln -s /home/quandm/.ssh/id_rsa.pub /root/.ssh/id_rsa.pub
cd /var/www/html
git clone git@github.com:teko-vn/user-service-api.git
```

* Edit your localhost `hosts` file:

`103.126.156.20 user-service.teko.vn`

* `virtualenv -p python3.6 venv`

```text
CREATE USER 'teko_user_service'@'%' IDENTIFIED BY 'TekoUsApi@123';
GRANT ALL PRIVILEGES ON user_service_api.* TO 'teko_user_service'@'%';
GRANT ALL PRIVILEGES ON user_service_api_test.* TO 'teko_user_service'@'%';
FLUSH PRIVILEGES;
```

Allow host 3306 for teko21 server.

Run 

```text
ln -s /var/www/html/user-service-api/deployments/services/teko_user.service  

/etc/systemd/system/teko_user.service

ln -s /var/www/html/user-service-api/deployments/nginx/user-service.teko.vn 

/etc/nginx/sites-enabled/user-service.teko.vn

service teko_user stop
service teko_user start
service nginx restart
```

### Celery with RabbitMQ

```textmate
pip --version
pip 19.3.1 from /usr/local/lib/python3.6/dist-packages/pip (python 3.6)
```

We install `celery` global base no need each celery version for each project.

```textmate
pip install celery
sudo apt-get install rabbitmq-server
service rabbitmq-server status
```

Create user with permission for rabbitmq

```text
rabbitmqctl add_user test test
Creating user "test"
rabbitmqctl add_vhost test_vhost
Creating vhost "test_vhost"
rabbitmqctl set_user_tags test test_tag
Setting tags for user "test" to [test_tag]
rabbitmqctl set_permissions -p test_vhost test ".*" ".*" ".*"
Setting permissions for user "test" in vhost "test_vhost"
```
Created symlink 

```text
ln -s /var/www/html/user-service-api/deployments/services/celery_worker.service /etc/systemd/system/celery_worker.service
```

### Test celery is working on test server

* We stop rabbitmq server on teko20 server 

`service rabbitmq-server stop`

* Stop `celery_worker` service

`service celery_worker stop`

Test with get rating by id api will hanging forever.

