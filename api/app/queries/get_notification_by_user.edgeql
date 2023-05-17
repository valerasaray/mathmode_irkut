with login := <str>$login,
  user := (select User filter .login = login),
select Notification {
  user_to: {
    id,
    login,
    rights: {value},
  },
  to_department: {
    id,
    title,
  },
  comment: {
    id,
    text_str,
    author: {
      id,
      login,
      rights: {value},
    },
    answer,
  },
  new_assign: {id},
  passed_node: {id},
} filter .user_to = user;