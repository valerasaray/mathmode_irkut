with node_id := <uuid>$node_id, rec_time := <datetime>$rec_time, new_status_title := <str>$new_status_title,

select (
  update Node
  filter .id = node_id
  set {
    status := (select Status filter .title = new_status_title),
    receipt := rec_time,
  }
) {id, along};
