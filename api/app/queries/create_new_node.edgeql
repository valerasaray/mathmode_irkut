with 
addenable := <bool>$addentable,
title := <str>$title

select (
  insert Node { 
    addenable := addenable,
    title := title,
  }
) {id};