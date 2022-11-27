const express = require('express')
const teacherRouter = require('./routes/teacher.routes')
const cors = require('cors');
//const sequelize = require('./db')
//const path = require('path')

const PORT = 5000

const app = express()
app.use(cors({origin: "http://localhost:3000"}))
app.use(express.json())
//app.use(express.static(path.resolve(__dirname, 'static')))
app.use('/api', teacherRouter)


app.listen(PORT, () => console.log(`Server started on port ${PORT}`))
