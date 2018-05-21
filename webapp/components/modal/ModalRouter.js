import React, { Component, Children } from 'react';
import { connect } from 'react-redux';
import { compose, withProps, defaultProps, branch, renderNothing, componentFromProp } from 'recompose';

const matchChild = (children, match) => {
    return Children.toArray(children)
        .find(modal => modal.props.name === match);
} 

const enhance = compose(
    connect(
        state => ({
            active: state.modal.active,
        })
    ),
    withProps(
        props => ({
            component: Children.toArray(props.children)
                .find(modal => modal.props.name === props.active) ?
                Children.toArray(props.children)
                .find(modal => modal.props.name === props.active).props.component : 
                null
        })
    ),
    branch(
        props => props.component === null,
        renderNothing
    )
);

export default enhance(componentFromProp('component'));