const Router = require('express')
const router = new Router()
const teacherController = require('../controllers/teacher.controller')

router.post('/teacher', teacherController.registration)
router.get('/teacher', teacherController.login)

module.exports = router