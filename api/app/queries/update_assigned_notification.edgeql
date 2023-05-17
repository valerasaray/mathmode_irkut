with process_id := <uuid>$process_id,
  process := (select Process filter .id = process_id),
  assigned := process.nodes.assigned,

for i in assigned union (
  insert Notification {
    to_department := i,
    new_assign := process,
  }
)