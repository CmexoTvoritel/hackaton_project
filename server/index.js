const express = require('express')
const teacherRouter = require('./routes/teacher.routes')


const PORT = 5000

const app = express()
app.use(express.json())
app.use('/api', teacherRouter)



app.listen(PORT, () => console.log(`Server started on port ${PORT}`))