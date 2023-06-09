# AUTOGENERATED FROM 'app/queries/update_node_status.edgeql' WITH:
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
class UpdateNodeStatusResult(NoPydanticValidation):
    id: uuid.UUID
    subs: list[UpdateNodeStatusResultSubsItem]


@dataclasses.dataclass
class UpdateNodeStatusResultSubsItem(NoPydanticValidation):
    id: uuid.UUID
    fit: UpdateNodeStatusResultSubsItemFit | None


@dataclasses.dataclass
class UpdateNodeStatusResultSubsItemFit(NoPydanticValidation):
    id: uuid.UUID


async def update_node_status(
    executor: edgedb.AsyncIOExecutor,
    *,
    subnode_id: uuid.UUID,
) -> list[UpdateNodeStatusResult]:
    return await executor.query(
        """\
        with subnode_id := <uuid>$subnode_id,
          subnode := (select SubNode filter .id = subnode_id),
          status := (select Status filter .color = "yellow"),
        select (
          update Node
          filter .subs = subnode
          set {
            status := status,
          }  
        ) {id, subs: {fit}};\
        """,
        subnode_id=subnode_id,
    )
