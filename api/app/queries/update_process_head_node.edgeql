with 
  head := (select Node filter .id = <uuid>$head_id),
  process_id := <uuid>$process_id,

select (
  update Process
  filter .id = process_id
  set {
    head := head,
  }
) {id};
