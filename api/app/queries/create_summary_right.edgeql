with user := (select User filter .login = <str>$login), 
right_val := (select Right filter .value = <str>$right_val)

select (
  true if right_val in user.rights else false
);