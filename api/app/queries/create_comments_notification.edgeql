with login := <str>$login,
  user := (select User filter .login = login),
  subnode_id := <uuid>$subnode_id,
  subnode := (select SubNode filter .id = subnode_id),
  text_str := <str>$text_str,

select (
  insert Notification {
    comment := (
      insert Comment {
        text_str := text_str,
        author := user,
      }
    ),
    passed_node := (
      update Node
      filter (.subs = subnode)
      set {
        status := (select Status filter .color = "yellow"),
      }
    )
  }
) {id, comment: {id, author: {login}, text_str, answer}};