import React from 'react';
import {Field, reduxForm} from "redux-form";
import {createField, Input} from "../common/FormsControls/FormsControls";
import {required} from "../../utils/validators/validators";
import {connect} from "react-redux";
import {login, getUnRegisterUserData} from "../../redux/auth-reducer";
import {Redirect} from "react-router-dom";
import style from "./../common/FormsControls/FormsControls.module.css"
import s from './Login.module.css';
const LoginForm = ({handleSubmit, error, captchaUrl}) => {
    return (
        <form onSubmit={handleSubmit} className={s.loginBlock}>
           {createField("Email", "email", [required], Input)}
            {createField("Password", "password", [required], Input, {type: "password"})}
            {/*{createField(null, "rememberMe", [], Input, {type: "checkbox"}, "remember me")}*/}

            {/*{ captchaUrl && <img src={captchaUrl} />}*/}
            { captchaUrl &&  createField("Symbols from image", "captcha", [required], Input, {}) }


            {error && <div className={style.formSummaryError}>
                {error}
            </div>
            }
            <div>
                <button>Login</button>
            </div>
        </form>
    )
}

const LoginReduxForm = reduxForm({form: 'login'})(LoginForm)

const Login = (props) => {
    const onSubmit = (formData) => {
        props.login(formData.email, formData.password);
    }

    if (props.isAuth) {
        return <Redirect to={"/empty"}/>
    }

    return <div>
        <h1>Login</h1>
        <LoginReduxForm onSubmit={onSubmit} />
    </div>
}
const mapStateToProps = (state) => ({
    isAuth: state.auth.isAuth,
    // getUnRegisterUserData: state.auth.getUnRegisterUserData,
})

export default connect(mapStateToProps, {login})(Login);
// getUnRegisterUserData