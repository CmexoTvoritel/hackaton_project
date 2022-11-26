const User = require('../models/models')
const bcrypt = require('bcrypt')
const jwt = require('jsonwebtoken')

class UserController {
    async registration(req, res) {
        const{id, name, surname, patronymic, mail, password} = req.body
        const candidate = await User.find0ne({where: {mail}})
        const hashPassword = await bcrypt.hash(password, 5)
        const teacher = await User.create({id, name, surname, patronymic, mail, password: hashPassword})
        const token = jwt.sign({id: teacher.id, name, surname, patronymic, mail}, process.env.SECRET_KEY,
            {expiresIn: '24h'}    
        )
        return res.json({token})
    }

    async login(req, res) {
        const {email, password} = req.body
        const teacher = await User.find0ne({where: {mail}})
        let comparePassword = bcrypt.compareSync(password, teacher.password)
        const token = generateJwt(teacher.id, teacher.password, teacher.mail)
        return res.json({token})
    }
}
module.exports = new UserController()