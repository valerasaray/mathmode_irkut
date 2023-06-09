# AUTOGENERATED FROM 'app/queries/update_process_node_status.edgeql' WITH:
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
class UpdateProcessNodeStatusResult(NoPydanticValidation):
    id: uuid.UUID


async def update_process_node_status(
    executor: edgedb.AsyncIOExecutor,
    *,
    process_id: uuid.UUID,
) -> list[UpdateProcessNodeStatusResult]:
    return await executor.query(
        """\
        with process_id := <uuid>$process_id,
          process := (select Process filter .id = process_id),
          status_blue := (select Status filter .color = "blue"),
          status_green := (select Status filter .color = "green"),

        select (
          update process.nodes
          filter .status = status_green
          set {
            status := status_blue,
          }
        ) {id};\
        """,
        process_id=process_id,
    )
