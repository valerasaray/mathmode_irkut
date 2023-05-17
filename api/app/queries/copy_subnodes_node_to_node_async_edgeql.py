# AUTOGENERATED FROM 'app/queries/copy_subnodes_node_to_node.edgeql' WITH:
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
class CopySubnodesNodeToNodeResult(NoPydanticValidation):
    id: uuid.UUID


async def copy_subnodes_node_to_node(
    executor: edgedb.AsyncIOExecutor,
    *,
    temp_node_id: uuid.UUID,
    node_id: uuid.UUID,
) -> CopySubnodesNodeToNodeResult | None:
    return await executor.query_single(
        """\
        with temp_node := (select Node filter .id = <uuid>$temp_node_id),
          node_id := <uuid>$node_id,


        select (
          update Node
          filter .id = node_id
          set {
            subs := (
              for sub in temp_node.subs union (
                select (
                  insert SubNode {
                    title := sub.title,
                    main := sub.main,
                  }
                )
              )
            ),
            assigned := temp_node.assigned
          }
        ) {id};\
        """,
        temp_node_id=temp_node_id,
        node_id=node_id,
    )
