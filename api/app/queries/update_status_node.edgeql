with node_id := <uuid>$node_id, new_status_title := <str>$new_status_title

select (
  update Node
  filter .id = node_id
  set {
    status := (select Status filter .title = new_status_title),
  }
) {id, along, next, status: {title}};