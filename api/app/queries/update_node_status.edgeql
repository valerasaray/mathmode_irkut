with subnode_id := <uuid>$subnode_id,
  subnode := (select SubNode filter .id = subnode_id),
  status := (select Status filter .color = "yellow"),
select (
  update Node
  filter .subs = subnode
  set {
    status := status,
  }  
) {id, subs: {fit}};