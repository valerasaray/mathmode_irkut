select User {
    login,
    FIO,
    rights: {value}
} filter .login=<str>$login