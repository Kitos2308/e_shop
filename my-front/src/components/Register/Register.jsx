import React from 'react';
import {Field, reduxForm} from "redux-form";
import {createField, Input} from "../common/FormsControls/FormsControls";
import {required} from "../../utils/validators/validators";
import {connect} from "react-redux";
import {register, setRegisterUserData} from "../../redux/auth-reducer";
import {Redirect} from "react-router-dom";
import style from "./../common/FormsControls/FormsControls.module.css"
import s from './Register.module.css';


const RegisterForm = ({handleSubmit, error}) => {
    return (
        <form onSubmit={handleSubmit} className={s.loginBlock}>
           {createField("Email", "email", [required], Input)}
            {createField("Password", "password", [required], Input, {type: "password"})}
            {createField("Confirm Password", "confirm_password", [required], Input, {type: "password"})}
            {/*{createField(null, "rememberMe", [], Input, {type: "checkbox"}, "remember me")}*/}

            {/*{ captchaUrl && <img src={captchaUrl} />}*/}
            {/*{ captchaUrl &&  createField("Symbols from image", "captcha", [required], Input, {}) }*/}


            {error && <div className={style.formSummaryError}>
                {error}
            </div>
            }
            <div>
                <button>Register</button>
            </div>
        </form>
    )
}

const RegisterReduxForm = reduxForm({form: 'register'})(RegisterForm)

const Register = (props) => {
    const onSubmit = (formData) => {
        props.register(formData.email, formData.password, formData.confirm_password);
    }
    debugger
    if (props.isRegistry) {
        alert('isRegistry true')

        return <Redirect to={"/login"}/>
    }

    return <div>
        <h1>Register</h1>
        <RegisterReduxForm onSubmit={onSubmit} />
    </div>
}
const mapStateToProps = (state) => ({
    isRegistry: state.auth.isRegistry
})

export default connect(mapStateToProps, {register})(Register);