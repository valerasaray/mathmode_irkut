with title := <str>$title,
  department_id := <uuid>$department_id,
  node_id := <uuid>$node_id,
  cur_node := (select Node filter .addenable = true and .id = node_id)

select (
  update cur_node
  set {
    addenable := false,
    along := (insert Node {
      title := title,
      addenable := true,
      assigned := (select Department filter .id = department_id),
  })}
) {along: {id, title}};