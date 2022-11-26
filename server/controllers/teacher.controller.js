const db = require('../db')

class TeacherControler {
    async registration(req, res) {
        
        const {name, surname, patronymic, mail, password} = req.body
        const newTeacher = await db.query(`INSERT INTO teachers (name, surname, patronymic, mail, password) VALUES ($1, $2, $3, $4, $5) RETURNING *`, [name, surname, patronymic, mail, password])
        res.json(newTeacher.rows[0])
        
    }
    async login(req, res) {
        const teacher = await db.query('SELECT * FROM teachers')
        res.json(teacher.rows)
    }
}

module.exports = new TeacherControler()