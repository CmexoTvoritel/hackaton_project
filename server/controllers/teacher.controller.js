const db = require('../db')
const bcrypt = require('bcrypt')

class TeacherControler {
    async registration(req, res) {
        
        const {name, surname, patronymic, mail, password} = req.body
        const newTeacher = await db.query(`INSERT INTO teachers (name, surname, patronymic, mail, password) VALUES ($1, $2, $3, $4, $5) RETURNING *`, [name, surname, patronymic, mail, password])
        res.json(newTeacher.rows[0])  
    }
    async login(req, res) {
        const {mail, password} = req.body
        const teacher_pass = await db.query('SELECT password FROM teachers WHERE mail=$1', [mail])
        res.json(teacher_pass.rows[0])
        // if(!teacher_pass.password == password) {
        //     res.json({wrong: 1})
        // }
        // else {
        //     res.json(teacher_pass.rows[0])
        // }
        //res.send(teacher_pass.rows[0])
        ///res.json(teacher_pass.rows[0])
        /*
        const teacher = await db.query('SELECT * FROM teachers')
        res.json(teacher.rows)
        */
    }
}

module.exports = new TeacherControler()