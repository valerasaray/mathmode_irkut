with passport_ref := <str>$passport_ref,
  process_id := <uuid>$process_id,

select (
  update Process
  filter .id = process_id
  set {
    passport_ref := passport_ref,
  }
){id, passport_ref};