# AUTOGENERATED FROM 'app/queries/update_status_node.edgeql' WITH:
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
class UpdateStatusNodeResult(NoPydanticValidation):
    id: uuid.UUID
    along: UpdateStatusNodeResultAlong | None
    next: UpdateStatusNodeResultAlong | None
    status: UpdateStatusNodeResultStatus | None


@dataclasses.dataclass
class UpdateStatusNodeResultAlong(NoPydanticValidation):
    id: uuid.UUID


@dataclasses.dataclass
class UpdateStatusNodeResultStatus(NoPydanticValidation):
    id: uuid.UUID
    title: str


async def update_status_node(
    executor: edgedb.AsyncIOExecutor,
    *,
    node_id: uuid.UUID,
    new_status_title: str,
) -> UpdateStatusNodeResult | None:
    return await executor.query_single(
        """\
        with node_id := <uuid>$node_id, new_status_title := <str>$new_status_title

        select (
          update Node
          filter .id = node_id
          set {
            status := (select Status filter .title = new_status_title),
          }
        ) {id, along, next, status: {title}};\
        """,
        node_id=node_id,
        new_status_title=new_status_title,
    )
