import {categoryAPI} from "../api/api";

const SET_CATEGORY_DATA = 'SET_CATEGORY_DATA_'

let initialState = {
    data: [],
    // categoryname: "",
    // subcategoryname: " "
};

const categoryReducer = (state = initialState, action) => {
    switch (action.type) {

        case SET_CATEGORY_DATA:
            return  {...state, data: action.data, }

        default:
            return state;
    }
}

export const setCategoryData  = (data) => ({
    type: SET_CATEGORY_DATA, data
});


export const getCategoryData = (slug) => async (dispatch) => {
    debugger
    let response = await categoryAPI.get_category_product_data(slug)
    if (response.data.resultCode === "0") {
        let  data_ = response.data['data'];
        dispatch(setCategoryData( data_));
    }
}

// export const getUserProfile = (userId) => (dispatch) => {
//     usersAPI.getProfile(userId).then(response => {
//         dispatch(setUserProfile(response.data));
//     });
// }



export default categoryReducer;