# Data Pipeline Mini Project
## Development setup
### Container
I'm using an ubuntu container as a development environment. 

The following commands create a container, map port 22 to host port 2222, and push the project csv file to the container.

```
lxc launch local_ubuntu data-pipeline
lxc config device add data-pipeline sshdev proxy listen=tcp:0.0.0.0:2222 connect=tcp:127.0.0.1:22
lxc file push third_party_sales_1.csv data-pipeline/root/
```
### Ubuntu
I use the following command to install python3, pip3 and mysql.
```
apt install -y python3-pip mysql-server
```

## Runtime setup
### Python
This project requires mysql's python connector. I installed it using pip3.
```
pip3 install mysql-connector-python
```

### MySQL
Passing the file `populate_data.sql` will setup a database with the requisite table and a user.

In my environment I load it as follows
```
mysql --defaults-file=/etc/mysql/debian.cnf < populate_data.sql
```

## etl.py
In keeping with the instructions I have implemented the functions described in `etl.py`

### loading rows into the database
```
python3 etl.py -f third_party_sales_1.csv
```

### querying the database
```
python3 etl.py -l
```

## etl module
In keeping with OOP practices I've also implemented the same functionality in a module with interfaces for database and records.

### loading rows into the database
```
python3 -m etl -f third_party_sales_1.csv
```

### querying the database
```
python3 -m etl -l
```