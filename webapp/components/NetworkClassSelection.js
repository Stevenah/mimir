import React, { Component } from 'react';
import { connect } from 'react-redux';

import { List } from 'mimir-ui';
import { requestNetworkClasses, selectClass, requestGradCam, requestGuidedGradCam } from 'actions';

class NetworkClassSelection extends Component {
    
    componentDidMount() {
        this.props.requestNetworkClasses();
    }

    getListRows = () => {

        if (!this.props.networkClasses) {
            return []
        }
        
        return this.props.networkClasses.map((category, index) => (
            <List.Item
                key = { `class_selection_${ index }` }
                selected={ category.index === this.props.selectedClass }
                onClick={ () => this.props.selectClass(category.index) }
            >
                { category.category__name }
            </List.Item>
        ));
    }

    render() {
        return (
            <List>
                { this.getListRows() }
            </List>
        );
    }
}

export default connect(
    state => ({
        networkClasses: state.network.classes,
        selectedClass: state.root.class,
    }),
    dispatch => ({
        requestNetworkClasses: () => {
            dispatch(requestNetworkClasses(1));
        },
        selectClass: classId => {
            dispatch(selectClass(classId));
            dispatch(requestGradCam());
            dispatch(requestGuidedGradCam());
        }
    })
)(NetworkClassSelection)

