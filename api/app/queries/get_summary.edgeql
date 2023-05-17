with login := <str>$login,
  group_assigned := (
    select Department filter (.boss.login = login or .staff.login = login)
  )

for subnode in (select SubNode) union (
  for node in (select Node filter .subs = subnode) union (
    for process in (select Process filter .nodes = node) union (
      (select process {title}),
      (select process {priority}),
      (select process {realiser}),
      (select process {realiserGroup}),
      
      (select process {passport_ref}),
      (select process {processType}),

      (select node {title}),
      (select node {assigned}),
      (select node {status}),
      (select node {receipt}),

      (select subnode {title}),
      (select subnode {fit}),
      (select subnode {start_verification}),
      (select subnode {comments}),
      (select subnode {end_verification}),
      (select subnode {end_correction}),
      (select subnode {main}),
    )
  )
)