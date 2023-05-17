with login := <str>$login,
  user := (select User filter .login = login),
  subnode_id := <uuid>$subnode_id,
update SubNode
filter .id = subnode_id
set {
  fit := user,
}