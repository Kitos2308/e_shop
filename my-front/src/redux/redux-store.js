import {applyMiddleware, combineReducers, createStore} from "redux";
import { reducer as formReducer } from 'redux-form'
import thunkMiddleware from "redux-thunk";
import authReducer from "./auth-reducer";
import navReducer from "./navbar-reducer"
import categoryReducer from "./category-data-reducer";


let reducers = combineReducers({
    auth: authReducer,
    navbar: navReducer,
    categorydata: categoryReducer,
    form: formReducer,
});

let store = createStore(reducers, applyMiddleware(thunkMiddleware));

window.store = store;


export default store;