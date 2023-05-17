with node := (select Node filter .id = <uuid>$node_id),
  assigned := node.assigned,

for i in assigned union (
  insert Notification {
    to_department := i,
    passed_node := node,
  }
)