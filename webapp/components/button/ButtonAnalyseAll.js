import React from 'react';
import { connect } from 'react-redux';
import { compose, withProps, withHandlers } from 'recompose';
import { requestImageAnalysis } from 'actions';

import { isEmpty } from 'utils';

import ButtonAction from 'components/button/ButtonAction'

const enhance = compose(
    connect(
        state => ({
            images: state.cnn.originalImages
        }),
        dispatch => ({
            analyzeImage(imageId) {
                dispatch(requestImageAnalysis(imageId))
            },
        }),
    ),
    withHandlers({
        onClick: props => event => {
            Object.keys(props.images).forEach(imageId => {
                props.analyzeImage(imageId);
            })
        }
    })
);

export default enhance(ButtonAction);