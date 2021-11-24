import * as axios from "axios"

export const base_url_category = "/api/category/"

const instance = axios.create({

    withCredentials: true,

    baseURL: 'http://localhost:8000/api/',

     headers : {
        'Content-Type' : 'application/json'

    }
});

export const categoryAPI = {
        get_category() {
            return instance.get('/category')
        },

         get_category_product_data(slug) {
            return instance.get('/category' + slug)
        }
}

export const authAPI = {

    register(email, password, password_confirm) {
        let formfield = new FormData()
        formfield.append('email',email)
        formfield.append('password', password)
        formfield.append('password_confirm', password_confirm)
        return instance.post(`user/register`,  formfield)
    },

    login(email, password,) {
        let formfield = new FormData()
        formfield.append('email',email)
        formfield.append('password', password)
        return instance.post(`user/login`,  formfield )
    },

    logout() {
        return instance.post(`user/logout`)
    },

    me() {
        return instance.get(`user/authme`)
    }
}

