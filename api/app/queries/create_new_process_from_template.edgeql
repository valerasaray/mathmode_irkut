with 
  user := (select User filter .login = <str>$login),
  department := (select Department filter .id = <uuid>$department_id),
  priority := (select Priority filter .id = <uuid>$priority_id),
  template := (select Template filter .id = <uuid>$template_id),
  process := template.process,
  passport_ref := <str>$passport_ref

select (
  insert Process {
    realiser := user,
    realiserGroup := department,
    priority := priority,
    title := passport_ref,
    processType := process.processType,
  }  
) {id};
