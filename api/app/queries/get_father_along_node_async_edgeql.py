# AUTOGENERATED FROM 'app/queries/get_father_along_node.edgeql' WITH:
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
class GetFatherAlongNodeResult(NoPydanticValidation):
    id: uuid.UUID
    status: GetFatherAlongNodeResultStatus | None
    next: GetFatherAlongNodeResultNext | None


@dataclasses.dataclass
class GetFatherAlongNodeResultNext(NoPydanticValidation):
    id: uuid.UUID


@dataclasses.dataclass
class GetFatherAlongNodeResultStatus(NoPydanticValidation):
    id: uuid.UUID
    title: str


async def get_father_along_node(
    executor: edgedb.AsyncIOExecutor,
    *,
    node_id: uuid.UUID,
) -> GetFatherAlongNodeResult | None:
    return await executor.query_single(
        """\
        with node := (select Node filter .id = <uuid>$node_id),

        select Node { status: { title}, next} filter .along = node limit 1;\
        """,
        node_id=node_id,
    )
