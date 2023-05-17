with node := (select Node filter .id = <uuid>$node_id),

select Node { status: { title}, next} filter .along = node limit 1;