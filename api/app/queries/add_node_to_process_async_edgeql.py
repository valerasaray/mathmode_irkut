# AUTOGENERATED FROM 'app/queries/add_node_to_process.edgeql' WITH:
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
class AddNodeToProcessResult(NoPydanticValidation):
    id: uuid.UUID


async def add_node_to_process(
    executor: edgedb.AsyncIOExecutor,
    *,
    node_id: uuid.UUID,
    process_id: uuid.UUID,
) -> AddNodeToProcessResult | None:
    return await executor.query_single(
        """\
        with node := (select Node filter .id = <uuid>$node_id),
          process_id := <uuid>$process_id,

        select (
          update Process
          filter .id = process_id
          set {
            nodes += node,
          }
        ) {id};\
        """,
        node_id=node_id,
        process_id=process_id,
    )
