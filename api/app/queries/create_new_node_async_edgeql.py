# AUTOGENERATED FROM 'app/queries/create_new_node.edgeql' WITH:
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
class CreateNewNodeResult(NoPydanticValidation):
    id: uuid.UUID


async def create_new_node(
    executor: edgedb.AsyncIOExecutor,
    *,
    addentable: bool,
    title: str,
) -> CreateNewNodeResult:
    return await executor.query_single(
        """\
        with 
        addenable := <bool>$addentable,
        title := <str>$title

        select (
          insert Node { 
            addenable := addenable,
            title := title,
          }
        ) {id};\
        """,
        addentable=addentable,
        title=title,
    )