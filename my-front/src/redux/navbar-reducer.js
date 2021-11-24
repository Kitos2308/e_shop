import {categoryAPI} from "../api/api";
import {stopSubmit} from "redux-form";


const SET_OPEN = 'SET_OPEN'
const SET_CATEGORY_DATA = 'SET_CATEGORY_DATA'
// const GET_CAPTCHA_URL_SUCCESS = 'samurai-network/auth/GET_CAPTCHA_URL_SUCCESS';

let initialState = {

    isOpen: false,
    data: [],

};

const navReducer = (state = initialState, action) => {
    switch (action.type) {
        case SET_OPEN:
            return {
                ...state,
                ...action.isOpen
            }
        case SET_CATEGORY_DATA:
            return  {...state, data: action.data}

        default:
            return state;
    }
}


export const setOpen = ( isOpen) => ({
    type: SET_OPEN,   isOpen
});

export const setCategoryData  = ( data) => ({
    type: SET_CATEGORY_DATA, data
});




export const getCategory = () => async (dispatch) => {
    debugger
    let response = await categoryAPI.get_category()
    if (response.data.resultCode === "0") {
        let  data_ = response.data['data'];
        dispatch(setCategoryData( data_));
    }
}




export default navReducer;