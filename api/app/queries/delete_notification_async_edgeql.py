# AUTOGENERATED FROM 'app/queries/delete_notification.edgeql' WITH:
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
class DeleteNotificationResult(NoPydanticValidation):
    id: uuid.UUID


async def delete_notification(
    executor: edgedb.AsyncIOExecutor,
    *,
    notification_id: uuid.UUID,
) -> DeleteNotificationResult | None:
    return await executor.query_single(
        """\
        with notification_id := <uuid>$notification_id
        delete Notification filter .id = notification_id;\
        """,
        notification_id=notification_id,
    )
