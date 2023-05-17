with node := (select Node filter .id = <uuid>$node_id),
  process_id := <uuid>$process_id,

select (
  update Process
  filter .id = process_id
  set {
    nodes += node,
  }
) {id};