const Router = require('express')
const router = new Router()
const userRouter = require('./userRouter')

router.use('/teachers', userRouter)

module.exports = router