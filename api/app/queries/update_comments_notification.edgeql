with login := <str>$login,
  user := (select User filter .login = login),
  answer := <str>$answer,
  comment_id := <uuid>$comment_id,
  comment := (select Comment filter .id = comment_id),
  subnode := (select SubNode filter .comments = comment),
  node := (select Node filter .subs = subnode),
  process := (select Process filter .nodes = node),

select (
  insert Notification {
    comment := (
        update Comment
        filter (.id = comment_id and process.realiser = user)
        set {
          answer := answer,
        }
    ),
    user_to := comment.author,
  }  
) {id, comment: {id, author: {login}, text_str, answer}};