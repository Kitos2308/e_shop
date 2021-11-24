import {authAPI} from "../api/api";
import {stopSubmit} from "redux-form";

const SET_USER_DATA = 'SET_USER_DATA';
const SET_USER_DATA_REGISTRY = 'SET_USER_DATA_REGISTRY'
// const GET_CAPTCHA_URL_SUCCESS = 'samurai-network/auth/GET_CAPTCHA_URL_SUCCESS';

let initialState = {
    // rId: null,
    email: null,
    login: null,
    register: null,
    isAuth: false,
    isRegistry: false,
    // captchaUrl: null // if null, then captcha is not required
};

const authReducer = (state = initialState, action) => {
    switch (action.type) {
        case SET_USER_DATA:
            return {
                ...state,
                ...action.payload
            }
        case SET_USER_DATA_REGISTRY:
            return {
                ...state,
                ...action.payload_registry
            }
        default:
            return state;
    }
}


export const setAuthUserData = ( email, login, isAuth) => ({
    type: SET_USER_DATA, payload:
        { email, login, isAuth}
});

export const setRegisterUserData = ( isRegistry) => ({
    type: SET_USER_DATA_REGISTRY, payload_registry:
        { isRegistry }
});




export const getAuthUserData = () => async (dispatch) => {
    debugger
    let response = await authAPI.me();
    debugger
    if (response.data.resultCode === "0") {
        let { login, email} = response.data.data;
        dispatch(setAuthUserData( email, login, true));

    }
}

export const getUnRegisterUserData= () =>  (dispatch) => {
    dispatch(setRegisterUserData(false))
}

export const login = (email, password) => async (dispatch) => {
    debugger
    // dispatch(getUnRegisterUserData())
    let response = await authAPI.login(email, password);
    debugger
    if (response.data.resultCode === "0") {
        // success, get auth data
        dispatch(getAuthUserData())
    } else {
        if (response.data.resultCode === "10") {
            alert('error')
            // dispatch(getCaptchaUrl());
        }

        // let message = response.data.messages.length > 0 ? response.data.messages[0] : "Some error";
        dispatch(stopSubmit("login", {_error: 'error'}));
    }
}


export const register = (email, password, password_confirm) => async (dispatch) => {
    debugger
    let response = await authAPI.register(email, password,password_confirm);
    debugger
    if (response.data.resultCode === "0") {
        // success, get auth data
        alert('you are registry success')
        dispatch(setRegisterUserData(true))
    } else {
        if (response.data.resultCode === "10") {
            alert('error')
            // dispatch(getCaptchaUrl());
        }

        // let message = response.data.messages.length > 0 ? response.data.messages[0] : "Some error";
        dispatch(stopSubmit("register", {_error: 'error'}));
    }
}


export const logout = () => async (dispatch) => {
    let response = await authAPI.logout();

    if (response.data.resultCode === '0') {
        dispatch(setAuthUserData(null, null, false));
    }
}



export default authReducer;