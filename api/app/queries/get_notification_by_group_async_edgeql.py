# AUTOGENERATED FROM 'app/queries/get_notification_by_group.edgeql' WITH:
#     $ edgedb-py


from __future__ import annotations
import dataclasses
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
class GetNotificationByGroupResult(NoPydanticValidation):
    id: uuid.UUID
    user_to: GetNotificationByGroupResultUserTo | None
    to_department: GetNotificationByGroupResultToDepartment | None
    comment: GetNotificationByGroupResultComment | None
    new_assign: GetNotificationByGroupResultNewAssign | None
    passed_node: list[GetNotificationByGroupResultPassedNodeItem]


@dataclasses.dataclass
class GetNotificationByGroupResultComment(NoPydanticValidation):
    id: uuid.UUID
    text_str: str
    author: GetNotificationByGroupResultUserTo | None
    answer: str | None


@dataclasses.dataclass
class GetNotificationByGroupResultNewAssign(NoPydanticValidation):
    id: uuid.UUID


@dataclasses.dataclass
class GetNotificationByGroupResultPassedNodeItem(NoPydanticValidation):
    id: uuid.UUID


@dataclasses.dataclass
class GetNotificationByGroupResultToDepartment(NoPydanticValidation):
    id: uuid.UUID
    title: str


@dataclasses.dataclass
class GetNotificationByGroupResultUserTo(NoPydanticValidation):
    id: uuid.UUID
    login: str
    rights: list[GetNotificationByGroupResultUserToRightsItem]


@dataclasses.dataclass
class GetNotificationByGroupResultUserToRightsItem(NoPydanticValidation):
    id: uuid.UUID
    value: str


async def get_notification_by_group(
    executor: edgedb.AsyncIOExecutor,
    *,
    login: str,
) -> list[GetNotificationByGroupResult]:
    return await executor.query(
        """\
        with login := <str>$login,
          user_group := (select Department filter (.boss.login = login or .staff.login = login)),
        select Notification {
          user_to: {
            id,
            login,
            rights: {value},
          },
          to_department: {
            id,
            title,
          },
          comment: {
            id,
            text_str,
            author: {
              id,
              login,
              rights: {value},
            },
            answer,
          },
          new_assign: {id},
          passed_node: {id},
        } filter .to_department = user_group;\
        """,
        login=login,
    )
