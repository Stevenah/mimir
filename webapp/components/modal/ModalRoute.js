import React, { PropTypes, Component } from 'react'
import { connect } from 'react-redux';
import { compose, withProps, defaultProps, branch, renderNothing, componentFromProp } from 'recompose';

const enhance = compose(
    defaultProps({
        component: null,
    }),
    branch(
        props => props.component !== null,
        renderNothing
    )
);

export default enhance(componentFromProp('component'));