with login := <str>$login,
  user_group := (select Department filter (.boss.login = login or .staff.login = login)),
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
} filter .to_department = user_group;