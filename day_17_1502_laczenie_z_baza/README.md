# Praca z danymi tabelarycznymi i pozyskiwanie danych z baz (biblioteka Pandas) - 9h

SQLAlchemy

## Docker + Oracle XE 11g 
Link: https://hub.docker.com/r/oracleinanutshell/oracle-xe-11g

Minimal start:

`docker run -d -p 49161:1521 -p 8080:8080  -e ORACLE_ALLOW_REMOTE=true oracleinanutshell/oracle-xe-11g`


Dane dostępowe:

```commandline
hostname: localhost
port: 49161
sid: xe
username: system
password: oracle
```




### Cz. 2
Oracle what's new: https://docs.oracle.com/en/database/oracle/oracle-database/21/whats-new.html
Oracle PE na Linux: https://tutorialforlinux.com/2018/06/08/how-to-install-oracle-sql-developer-on-manjaro-linux-easy-guide/2/
Oracle install PE: https://docs.oracle.com/en/database/oracle/oracle-database/21/xeinl/
* Oracle Linux 8.7 (https://yum.oracle.com/ISOS/OracleLinux/OL8/u7/x86_64/OracleLinux-R8-U7-x86_64-dvd.iso)
* 

Install guide: https://docs.oracle.com/en/database/oracle/oracle-database/21/xeinl/installation-guide.html#GUID-31891F22-B1FA-4489-A1C5-195E6B3D89C8
Java on Manjaro: sudo pacman -Sy jdk17-openjdk
Python access to Oracle:
 - https://oracle.github.io/python-cx_Oracle/
 - https://oracle.github.io/python-oracledb/

Python sample app with Oracle
 - https://www.oracle.com/database/technologies/appdev/python/quickstartpythononprem.html

---
