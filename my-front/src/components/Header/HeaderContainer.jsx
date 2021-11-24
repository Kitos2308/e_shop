import React from 'react';
import Header from "./Header";
import {connect} from "react-redux";
import {getAuthUserData ,logout, getUnRegisterUserData} from "../../redux/auth-reducer";

class HeaderContainer extends React.Component {
    componentDidMount() {
        debugger
      this.props.getAuthUserData();
      this.props.getUnRegisterUserData();
    }



    render() {
        debugger
        return <Header {...this.props} />
    }
}
const mapStateToProps = (state) => ({
    isAuth: state.auth.isAuth,
    login: state.auth.login,
    isRegistry: state.auth.isRegistry,


});

export default connect(mapStateToProps, {getAuthUserData, getUnRegisterUserData,  logout})(HeaderContainer);