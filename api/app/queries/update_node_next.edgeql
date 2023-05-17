with node_id := <uuid>$node_id, next_id := <uuid>$next_id,
  node := (select Node filter .id = next_id),

select (
  update Node
  filter .id = node_id
  set {
    next := node,
  }
) {id};