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
) {id};