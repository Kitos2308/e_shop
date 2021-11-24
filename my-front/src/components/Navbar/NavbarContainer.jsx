import React from 'react';
import Navbar from "./Navbar";
import {connect} from "react-redux";
import {  getCategory,  } from "../../redux/navbar-reducer";



class NavbarContainer extends React.Component {
    componentDidMount() {

      this.props.getCategory();
    }

    render() {
        debugger
        return <Navbar {...this.props} />
    }
}
const mapStateToProps = (state) => ({
    isOpen: state.navbar.isOpen,
    data: state.navbar.data

});

export default connect(mapStateToProps, {getCategory,  })(NavbarContainer);