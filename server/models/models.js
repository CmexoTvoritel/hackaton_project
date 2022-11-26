const sequelize = require('../db')
const {DataTypes} = require('sequelize')

const User = sequelize.define('teachers', {
    id: {type: DataTypes.INTEGER, primaryKey: true, autoIncrement: true},
    name: {type: DataTypes.STRING},
    surname: {type: DataTypes.STRING},
    patronymic: {type: DataTypes.STRING},
    mail: {type: DataTypes.STRING, unique: true},
    password: {type: DataTypes.STRING},
})

module.exports = {
    User
}