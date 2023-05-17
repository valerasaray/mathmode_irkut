# mathmode_irkut
Единая информационная система отслеживания процесса согласования (ИСОПС)

# как запустить на локальной машине
в директории app \
установить edgedb 
```
curl --proto '=https' --tlsv1.2 -sSf https://sh.edgedb.com | sh
source <Путь_из_вывода>
```
запустить БД и API (в докере): \ 
```
sudo rm -rf ./data
sudo rm -rf ./dbschema
docker-compose --env-file .env -f docker-compose.yml up
```
(в docker-compose только образ edgeDB) \

Запустить фронт (локально)
