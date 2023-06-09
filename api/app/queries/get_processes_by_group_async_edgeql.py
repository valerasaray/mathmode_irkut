# AUTOGENERATED FROM 'app/queries/get_processes_by_group.edgeql' WITH:
#     $ edgedb-py


from __future__ import annotations
import dataclasses
import datetime
import edgedb
import uuid


class NoPydanticValidation:
    @classmethod
    def __get_validators__(cls):
        from pydantic.dataclasses import dataclass as pydantic_dataclass
        pydantic_dataclass(cls)
        cls.__pydantic_model__.__get_validators__ = lambda: []
        return []


@dataclasses.dataclass
class GetProcessesByGroupResult(NoPydanticValidation):
    id: uuid.UUID
    title: str
    nodes: list[GetProcessesByGroupResultNodesItem]
    realiser: GetProcessesByGroupResultNodesItemAssignedItemBoss | None
    realiserGroup: GetProcessesByGroupResultrealiserGroup | None
    priority: GetProcessesByGroupResultPriority | None
    passport_ref: str | None
    processType: GetProcessesByGroupResultprocessType | None


@dataclasses.dataclass
class GetProcessesByGroupResultNodesItem(NoPydanticValidation):
    id: uuid.UUID
    title: str
    assigned: list[GetProcessesByGroupResultNodesItemAssignedItem]
    along: GetProcessesByGroupResultNodesItemAlong | None
    addenable: bool | None
    subs: list[GetProcessesByGroupResultNodesItemSubsItem]
    next: GetProcessesByGroupResultNodesItemNext | None
    customField: list[GetProcessesByGroupResultNodesItemcustomFieldItem]
    status: GetProcessesByGroupResultNodesItemStatus | None
    receipt: datetime.datetime | None


@dataclasses.dataclass
class GetProcessesByGroupResultNodesItemAlong(NoPydanticValidation):
    id: uuid.UUID
    title: str
    addenable: bool | None


@dataclasses.dataclass
class GetProcessesByGroupResultNodesItemAssignedItem(NoPydanticValidation):
    id: uuid.UUID
    title: str
    boss: GetProcessesByGroupResultNodesItemAssignedItemBoss | None
    staff: list[GetProcessesByGroupResultNodesItemAssignedItemBoss]


@dataclasses.dataclass
class GetProcessesByGroupResultNodesItemAssignedItemBoss(NoPydanticValidation):
    id: uuid.UUID
    login: str


@dataclasses.dataclass
class GetProcessesByGroupResultNodesItemNext(NoPydanticValidation):
    id: uuid.UUID


@dataclasses.dataclass
class GetProcessesByGroupResultNodesItemStatus(NoPydanticValidation):
    id: uuid.UUID
    title: str
    color: str


@dataclasses.dataclass
class GetProcessesByGroupResultNodesItemSubsItem(NoPydanticValidation):
    id: uuid.UUID
    title: str
    start_verification: datetime.datetime | None
    comments: list[GetProcessesByGroupResultNodesItemSubsItemCommentsItem]
    fit: GetProcessesByGroupResultNodesItemSubsItemFit | None
    end_verification: datetime.datetime | None
    end_correction: datetime.datetime | None


@dataclasses.dataclass
class GetProcessesByGroupResultNodesItemSubsItemCommentsItem(NoPydanticValidation):
    id: uuid.UUID
    text_str: str
    author: GetProcessesByGroupResultNodesItemSubsItemCommentsItemAuthor | None
    answer: str | None


@dataclasses.dataclass
class GetProcessesByGroupResultNodesItemSubsItemCommentsItemAuthor(NoPydanticValidation):
    id: uuid.UUID


@dataclasses.dataclass
class GetProcessesByGroupResultNodesItemSubsItemFit(NoPydanticValidation):
    id: uuid.UUID
    login: str
    FIO: str | None
    rights: list[GetProcessesByGroupResultNodesItemSubsItemFitRightsItem]


@dataclasses.dataclass
class GetProcessesByGroupResultNodesItemSubsItemFitRightsItem(NoPydanticValidation):
    id: uuid.UUID
    value: str


@dataclasses.dataclass
class GetProcessesByGroupResultNodesItemcustomFieldItem(NoPydanticValidation):
    id: uuid.UUID
    value: str
    titleField: GetProcessesByGroupResultNodesItemcustomFieldItemtitleField | None


@dataclasses.dataclass
class GetProcessesByGroupResultNodesItemcustomFieldItemtitleField(NoPydanticValidation):
    id: uuid.UUID
    value: str


@dataclasses.dataclass
class GetProcessesByGroupResultPriority(NoPydanticValidation):
    id: uuid.UUID
    value: str


@dataclasses.dataclass
class GetProcessesByGroupResultprocessType(NoPydanticValidation):
    id: uuid.UUID
    title: str


@dataclasses.dataclass
class GetProcessesByGroupResultrealiserGroup(NoPydanticValidation):
    id: uuid.UUID
    title: str
    boss: GetProcessesByGroupResultrealiserGroupBoss | None
    staff: list[GetProcessesByGroupResultrealiserGroupBoss]


@dataclasses.dataclass
class GetProcessesByGroupResultrealiserGroupBoss(NoPydanticValidation):
    id: uuid.UUID
    login: str


async def get_processes_by_group(
    executor: edgedb.AsyncIOExecutor,
    *,
    login: str,
) -> list[GetProcessesByGroupResult]:
    return await executor.query(
        """\
        with login := <str>$login,
          group_realizer := (
            select Department filter (.boss.login = login or .staff.login = login)
          )

        select Process {
            id,
            title,
            nodes: {
              id,
              title,
              assigned: {
                id, 
                title, 
                boss: {id, login}, 
                staff: {id, login}},
              along: {
                id,
                title,
                addenable,
              },
              addenable,
              subs: {
                id, 
                title, 
                start_verification, 
                comments: {
                  text_str,
                  author,
                  answer,
                },
                fit: {id, login, FIO, rights: {value}},
                end_verification,
                end_correction,
              },
              next: {id},
              customField: {
                value, 
                titleField: {value},
              },
              status: {title, color},
              receipt,
            },
            realiser: {id, login},
            realiserGroup: {id, title, boss: {login}, staff: {login}},
            priority: {value},
            passport_ref,
            processType: {title},
        } filter .realiserGroup = group_realizer;\
        """,
        login=login,
    )
