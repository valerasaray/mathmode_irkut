with node_id := <uuid>$node_id, along_id := <uuid>$along_id,
  node := (select Node filter .id = along_id),

select (
  update Node
  filter .id = node_id
  set {
    along := node,
  }
) {id};