from __future__ import annotations

from http import HTTPStatus
from typing import List

import edgedb
import uuid
from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel

from fastapi.responses import FileResponse
import os
from datetime import datetime


from __init__ import get_edgedb_client

import queries.get_summary_async_edgeql as get_summary_qry
import queries.create_summary_right_async_edgeql as get_summary_right_qry

import pandas as pd
import openpyxl

def cleaner(x):
    if x == 'None' or x == '[]':
        return ''
    return x

def comment_checker(x):
    if x == 'None'  or x == '[]':
        return 'нет'
    return 'есть'

class SummaryData(BaseModel):
    login: str


router = APIRouter()

@router.post("/summary")
async def get_summary(
    # login: str = Query(None, max_length=1000),
    data: SummaryData,
    client: edgedb.AsyncIOClient = Depends(get_edgedb_client),
    ):

    sheet_data = await get_summary_qry.get_summary(client, login=data.login)
    summary_right = await get_summary_right_qry.create_summary_right(client, login=data.login, right_val="create_summary_right")

    if summary_right:

        df = pd.DataFrame(columns=[
            'Наименвание паспорта',
            'Важность',
            'Выпускающий',
            'Подразделение выпускающего',
            'Ссылка на паспорт',
            'Тип процедуры выпуска',
            'Этап проверки',
            'Назначенные подразделения',
            'Текущий статус этапа согласования',
            'Время постановки этапа на проверку',
            'Задача этапа согласования',
            'Назначенный на задачу пользователь',
            'Начало проверки',
            'Замечания',
            'Конец проверки',
            'Конец исправления'
        ])

        for i in sheet_data:               
            new_row = {
            'Наименвание паспорта':cleaner(str(i[0].title)),
            'Важность':cleaner(str(i[1].priority)),
            'Выпускающий':cleaner(str(i[2].realiser)),
            'Подразделение выпускающего':cleaner(str(i[3].realiserGroup)),
            'Ссылка на паспорт':cleaner(str(i[4].passport_ref)),
            'Тип процедуры выпуска':cleaner(str(i[5].processType)),
            'Этап проверки':cleaner(str(i[6].title)),
            'Назначенные подразделения':cleaner(str(i[7].assigned)),
            'Текущий статус этапа согласования':cleaner(str(i[8].status)),
            'Время постановки этапа на проверку':cleaner(str(i[9].receipt)),
            'Задача этапа согласования':cleaner(str(i[10].title)),
            'Назначенный на задачу пользователь':cleaner(str(i[11].fit)),
            'Начало проверки':cleaner(str(i[12].start_verification)),
            'Замечания':cleaner(comment_checker(str(i[13].comments))),
            'Конец проверки':cleaner(str(i[14].end_verification)),
            'Конец исправления':cleaner(str(i[15].end_correction))
            }

            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        df = df.dropna()

        table_name = f'выгрузка_{data.login}_{datetime.now().strftime("%d-%m-%Y_%H:%M:%S")}.xlsx'

        table_path = os.path.join('tables', table_name)

        df.to_excel(table_path, sheet_name='выгрузка', index=False)
            
            
        # загрузите файл Excel
        workbook = openpyxl.load_workbook(table_path)

        # выберите лист для работы
        worksheet = workbook.active

        # устанавливаем ширину колонок
        for col in worksheet.columns:
            col_width = max(len(str(cell.value)) for cell in col)
            col_letter = col[0].column_letter

            worksheet.row_dimensions[1].height = 40

            worksheet.column_dimensions[col_letter].width = col_width + 5
            for i in range(2, worksheet.max_row + 1):
                worksheet.row_dimensions[i].height = 20

        # сохраните изменения
        workbook.save(table_path)

    # @router.get("/summary/download_xlsx")
    # async def download_xlsx():
        xlsx_path = os.path.abspath(table_path)

        return FileResponse(xlsx_path, filename=table_path[7:], media_type="application/xlsx")
