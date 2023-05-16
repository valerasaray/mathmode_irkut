# mathmode_irkut
Единая информационная система отслеживания процесса согласования (ИСОПС)

# как запустить на локальной машине
в директории app \
установить edgedb 
```
curl --proto '=https' --tlsv1.2 -sSf https://sh.edgedb.com | sh
source <Путь_из_вывода>
```
запустить БД (локально):
```
edgedb project init
```
запустить БД (в докере): \
в первом терминале: 
```
docker-compose up
```
(в docker-compose только образ edgeDB) \

Во втором терминале: 



