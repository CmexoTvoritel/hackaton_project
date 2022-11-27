import { $authHost, $host } from "./index";

export const registration = async(name, surname, patronymic, mail, password) => {
    const response = await $host.post('/api/teacher', {name, surname, patronymic, mail, password})                                                         
    return response
}

export const login = async(mail, password) => {
    const response = await $host.get('/api/teacher', {mail, password})
    return response
}