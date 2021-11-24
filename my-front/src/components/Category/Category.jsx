import React from 'react';
import {getCategoryData} from "../../redux/category-data-reducer";
import {useParams} from "react-router-dom";

const Category = (props) => {
    debugger
    // let { categoryname, subcategoryname } = useParams();
    // alert(categoryname)
    // alert(subcategoryname)
    return (

        props.data.map(item => <li>{item.name}</li>)

    )
}

export default Category;