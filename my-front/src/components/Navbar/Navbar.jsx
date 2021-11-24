import React, {useState} from 'react';
import s from './Navbar.module.css';
import {NavLink} from "react-router-dom";
import {base_url_category} from '../../api/api'
import SubNav  from "./SubNav";







class Navbar extends React.Component{


    base_url = "/api/category"

    state = {
        editMode: true,
        editModeProduct:false,
        product_last_id:0,
        product_open:[],
        product_id:0,
        close_all_product:false,
        subitem_state:false,
        subitem_: null,
        item_: null
    }



    close_all(){
        this.setState({
            close_all_product:true
        });
    }


        activateEditMode(id) {

        this.setState( {
            editMode: true,
            product_id: id
        }

        );
    }

    deactivateEditMode(id) {
        this.setState( {
            editMode: false,
            product_id:id
        } );
    }

           activateEditProductMode(id) {

        this.setState( {
            editModeProduct: true,
            product_last_id: id
        }

        );
    }

     deactivateEditProductMode(id) {

        this.setState( {
            editModeProduct: false,
            product_last_id: id
        }

        );
    }


    activate_state_subitem(bool_state){
        this.setState(
            {
                subitem_state:bool_state
            }
        );
    }


    setItems = (subitem_, item_) => {

        this.setState(
            {
            subitem_: subitem_,
            item_: item_}
        );

    }




    render() {

        var data_ = this.props.data.map((item, index) => {
        return (
            <div key={index}>
                <ul>{item.name}</ul>
                {
                    item.subcategory.map((subitem, subindex ) => {
                        return (
                            < >
                             {
                        <button

                            // className={s.subcategory_css}
                            onMouseEnter={ () => {
                                this.setItems(subitem, item)
                                this.activateEditMode.bind(this, subitem.id);
                                this.activate_state_subitem(true)

                            } }
                            onMouseLeave={ this.deactivateEditMode.bind(this, null)}
                        > <NavLink to={base_url_category + item.slug + "/" + subitem.slug + "/"}> {subitem.name} </NavLink>

                </button>

                }
                 {this.state.editMode && subitem.id === this.state.product_id &&
                    <SubNav  onMouseLeave={ this.deactivateEditMode.bind(this, subitem.id)}    >

                    </SubNav>

                }
                    </>
                        )
                    })
                }
            </div>
        )
    })



        return (
            <div className={s.nav}>
                    <div className={s.item} >
                    <NavLink to="/empty" activeClassName={s.activeLink}>Empty </NavLink>
                    </div>



                    {
                        data_.map((item, index) => {
                            return <div key={index} className={s.subcategory_css}> {item}
                          <div className={s.subcategory_item}>      {this.state.editMode && this.state.subitem_state &&
                            <SubNav subitem_={this.state.subitem_} item_={this.state.item_}> </SubNav>}
                          </div>
                            </div>
                        })
                    }







            </div>
        )
    }

}

export default Navbar;