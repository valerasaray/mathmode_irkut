with process_id := <uuid>$process_id,

select Process {
  head: {
      id,
    },
    id,
    title,
    nodes: {
      id,
      title,
      assigned: {
        id, 
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
        fit: {id, login, FIO, rights: {value}},
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
    },
    realiser: {id, login},
    realiserGroup: {id, title, boss: {login}, staff: {login}},
    priority: {value},
    passport_ref,
    processType: {title},
} filter .id = process_id