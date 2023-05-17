with subnode_id := <uuid>$subnode_id,
  date :=  <datetime>$datetime
select(
update SubNode
    filter .id = subnode_id
    set {
    end_verification := date,
    }
) {id};