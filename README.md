# mathmode_irkut
Единая информационная система отслеживания процесса согласования (ИСОПС)
## Задача
Данный кейс от компании Иркут, решался на III Весенней Школе Матмод МАИ.
### Главные задачи
1. Реализовать систему распределения задач и отслеживания согласования документации
2. Реализовать систему уведомлений
3. Реализовать систему хранения КД
4. Реализовать систему замечаний
## Информация
Таблица Miro: https://miro.com/welcomeonboard/SmZrSlM1Tm4wM2lxaWFlVGVndWhldExYSlE5TFJNQmJSSVN2MXVoOERZM2lXQzlxT0lJZkV3aXg5bVQyQUMxU3wzNDU4NzY0NTI1Nzc4NjY2NDU4fDI=?share_link_id=253311310582

Схема БД:
![Схема БД](./doc/bd.jpg)

Основная бизнес-логика:
![Основная бизнес-логика](./doc/bl.jpg)

Диаграмма прециндентов:
![Диаграмма прециндентов](./doc/diag_prec.jpg)

Документация по API:
[openapi](./doc/openapi.json)

## Архитектура
1. База данных для обработки и хранения состояния системы отслеживанья согласования - EdgeDB
2. База данных для хранения файлов - Postgres
3. Backend - FastAPI
4. Frontend - TypeScript, MuUI

## Как запустить на локальной машине
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
