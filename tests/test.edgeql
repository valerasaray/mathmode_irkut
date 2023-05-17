with insert0 := (
insert Status {
    color := 'green',
    title := 'Проверено'
}),

insert1 := (
insert Status {
    color := 'blue',
    title := 'Принято на проверку'
}),

insert2 := (
insert Status {
    color := 'yellow',
    title := 'В приоритете проверки'
}),

insert3 := (
insert Status {
    color := 'red',
    title := 'Обнаружены замечания'
}),

insert4 := (
insert Priority {
    value := 'Важно'
}),

insert5 := (
insert Priority {
    value := 'Средней важности'
}),

insert6 := (
insert Priority {
    value := 'Низкой важности'
}),

insert7 := (
insert ProcessType {
    title := 'ИИ'
}),

insert8 := (
insert ProcessType {
    title := 'КД'
}),

insert9 := (
insert Right {
    value := 'create_summary_right'
}),

insert10 := (
insert Right {
    value := 'create_process_right'
}),

insert11 := (
insert User {
    FIO := 'Иван Павлов',
    login := 'APIDEMON',
    password := '1',
    rights := insert10,
}),

insert12 := (
insert User {
    FIO := 'Илья Лютоев',
    login := 'votilya',
    password := '1234',
    rights := insert10,
}),

insert13 := (
insert User {
    FIO := 'Арсений Соколов',
    login := 'valerasaray',
    password := '1234',
    rights := insert9,
}),

insert14 := (
insert User {
    FIO := 'Артем Зимин',
    login := 'animemaster',
    password := '1111',
    rights := insert10,
}),

insert15 := (
insert User {
    FIO := 'Даврон Диеров',
    login := 'davik47',
    password := '12412',
    rights := insert10,
}),

insert16 := (
insert Department {
    title := 'Фронтенд отдел',
    staff := insert14,
    boss := insert14,
}),

insert17 := (
insert Department {
    title := 'Бэкенд отдел',
    staff := distinct {
        insert11,
        insert12,
        insert13,
        insert15,
    },
    boss := insert11,
}),

insert18 := (
insert SubNode {
    title := 'Утвердил',
    main := true,
}),

insert19 := (
insert SubNode {
    title := 'Утвердил',
    main := true,
}),

insert20 := (
insert SubNode {
    title := 'Утвердил',
    main := true,
}),

insert23 := (
insert Node {
    addenable := false,
    title := 'Проверка Докеризации',
    assigned := insert17,
    status := insert3,
    subs := insert20,
}),


insert22 := (
insert Node {
    addenable := false,
    title := 'Наличие багов',
    assigned := distinct {
        insert16,
        insert17,
    },
    next := insert23,
    status := insert3,
    subs := insert20,
}),

insert21 := (
insert Node {
    addenable := false,
    title := 'Кодстайл',
    assigned := insert16,
    next := insert22,
    status := insert0,
    subs := insert18,
}),

insert24 := (
insert Process {
    title := 'Процесс согласования ИИ',
    processType := insert7,
    priority := insert4,
    realiser := insert11,
    realiserGroup := insert17,
    nodes := distinct {
        insert21,
        insert22,
        insert23,
    },
    head := insert21,
}),

insert25 := (
insert Template {
    title := 'ИИ',
    process := insert24,
}),

select User;