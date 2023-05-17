with process_id := <uuid>$process_id,
  process := (select Process filter .id = process_id),
  status_blue := (select Status filter .color = "blue"),
  status_green := (select Status filter .color = "green"),

select (
  update process.nodes
  filter .status = status_green
  set {
    status := status_blue,
  }
) {id};