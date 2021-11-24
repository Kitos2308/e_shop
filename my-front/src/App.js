import React from 'react';
import './App.css';
import LoginPage from "./components/Login/Login";
import RegisterPage from "./components/Register/Register"
import NavbarContainer from './components/Navbar/NavbarContainer';
import  { Route } from "react-router-dom";
import HeaderContainer from "./components/Header/HeaderContainer";
import CategoryContainer from "./components/Category/CategoryContainer";

import {Router} from "react-router";


const App = () => {
    debugger
  return (
    <div className='app-wrapper'>
      <HeaderContainer />
      <NavbarContainer />

         <Route path='/empty'
                render={ () => <div> <h1>EMPTY</h1></div> }/>

          <Route path='/login'
                           render={ () => <LoginPage /> }/>

         <Route path='/register'
                           render={ () => <RegisterPage /> }/>



        <Route   path={[
            "/api/category/:categoryname/:subcategoryname/:subcategoryproductname/:productsname",
            "/api/category/:categoryname/:subcategoryname/:subcategoryproductname",
            "/api/category/:categoryname/:subcategoryname"
                        ]}
                           render={ () => <CategoryContainer /> }/>






    </div>);
}

export default App;



