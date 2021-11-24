import React from 'react';
import Category from "./Category";
import {  getCategoryData,  } from "../../redux/category-data-reducer";
import {connect} from "react-redux";
import {compose} from "redux";
import {withRouter} from "react-router-dom";



class CategoryContainer extends React.Component {

    componentDidMount() {
      this.props.getCategoryData();
    }

    componentDidUpdate(prevProps, prevState, snapshot) {
        debugger
    if ( this.props.match.params.subcategoryname !== prevProps.match.params.subcategoryname && this.props.match.params.subcategoryproductname === undefined   )
    {
        let slug ="/" + this.props.match.params.categoryname + "/" + this.props.match.params.subcategoryname
        this.props.getCategoryData(slug);
    } else if (  this.props.match.params.subcategoryproductname !== undefined &&  this.props.match.params.productsname === undefined  ) {
             let slug ="/" + this.props.match.params.categoryname + "/" + this.props.match.params.subcategoryname + "/" + this.props.match.params.subcategoryproductname
        this.props.getCategoryData(slug);
     } else if ( this.props.match.params.subcategoryname === prevProps.match.params.subcategoryname && this.props.match.params.subcategoryproductname !== prevProps.match.params.subcategoryproductname
        && this.props.match.params.productsname === undefined    ) {
        let slug ="/" + this.props.match.params.categoryname + "/" + this.props.match.params.subcategoryname
        this.props.getCategoryData(slug);
    } else if (  this.props.match.params.productsname !== undefined   ) {
             let slug ="/" + this.props.match.params.categoryname + "/" + this.props.match.params.subcategoryname
                 + "/" + this.props.match.params.subcategoryproductname + "/" + this.props.match.params.productsname
        this.props.getCategoryData(slug);
     }
}

    render() {
        debugger
        return <Category {...this.props} />
    }
}
const mapStateToProps = (state) => ({
    data: state.categorydata.data

});

// export default connect(mapStateToProps, {getCategoryData,  })(CategoryContainer);

export default compose(
    connect(mapStateToProps, {getCategoryData}),
    withRouter
)(CategoryContainer);