// const Pool = require('pg').Pool
// const pool = new Pool({
//     user: "admin",
//     password: 'admin',
//     host: "270-356-496.local",
//     port: 5432,
//     database: "bot-hackaton"
// })

const Pool = require('pg').Pool
const pool = new Pool({
    user: "postgres",
    password: 'root',
    host: "localhost",
    port: 5432,
    database: "Bot-hackaton"
})


module.exports = pool