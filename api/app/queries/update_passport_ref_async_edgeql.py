# AUTOGENERATED FROM 'app/queries/update_passport_ref.edgeql' WITH:
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
class UpdatePassportRefResult(NoPydanticValidation):
    id: uuid.UUID
    passport_ref: str | None


async def update_passport_ref(
    executor: edgedb.AsyncIOExecutor,
    *,
    passport_ref: str,
    process_id: uuid.UUID,
) -> UpdatePassportRefResult | None:
    return await executor.query_single(
        """\
        with passport_ref := <str>$passport_ref,
          process_id := <uuid>$process_id,

        select (
          update Process
          filter .id = process_id
          set {
            passport_ref := passport_ref,
          }
        ){id, passport_ref};\
        """,
        passport_ref=passport_ref,
        process_id=process_id,
    )