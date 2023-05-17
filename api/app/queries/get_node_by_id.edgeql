select Node {
  id,
  title,
  assigned: {id, 
            title, 
            boss: {id, login}, 
            staff: {id, login}},
  along: {
    id,
    title,
    addenable,
  },
  addenable,
  subs: {
    id, 
    title, 
    start_verification, 
    comments: {
      text_str,
      author,
      answer,
    },
    fit: {id, login, rights: {value}},
    end_verification,
    end_correction,
  },
  next: {id},
  customField: {
    value, 
    titleField: {value},
  },
  status: {title, color},
  receipt,
} filter .id = <uuid>$node_id