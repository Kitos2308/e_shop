import s from "./Navbar.module.css";
import {NavLink} from "react-router-dom";
import {base_url_category} from "../../api/api";
import Navbar from "./Navbar";
import React  from "react";


class SubNav extends React.Component {

    constructor(props) {

        super(props);

    }



        base_url = "/api/category"

    state = {
        editMode: true,
        editModeProduct:false,
        product_last_id:0,
        product_open:[],
        product_id:0,
        subitem_:null,
        item_:null

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



    render() {

             var data_ = this.props.subitem_.subcategoryproduct.map((product, productindex) => {
                    return (
                        <div key={productindex} >
                            <button onMouseEnter={this.activateEditMode.bind(this, this.props.subitem_.id)}
                            >
                                <NavLink to={base_url_category + this.props.item_.slug + "/" + this.props.subitem_.slug + "/" + product.slug}
                                         onMouseEnter={this.activateEditProductMode.bind(this, product.id)}
                                >
                                    {product.name} </NavLink>

                            </button>
                            {this.state.editModeProduct && product.id === this.state.product_last_id &&
                            <div onMouseLeave={this.deactivateEditProductMode.bind(this, null)}>

                                {
                                    product.subcategoryproduct_last.map((subproduct) => {

                                        return <button onMouseLeave={this.deactivateEditProductMode.bind(this, null)}>
                                            <NavLink to={base_url_category +
                                            this.props.item_.slug + "/" + this.props.subitem_.slug + "/" + product.slug + "/" + subproduct.slug}>

                                                {subproduct.name} </NavLink>
                                        </button>
                                    })
                                }
                            </div>
                            }
                        </div>
                    )
                }
            )

        return ( < div > {data_} </div>  )
        }

}

export default SubNav;

// <div className={s.subitem_css}> {data_} </div>