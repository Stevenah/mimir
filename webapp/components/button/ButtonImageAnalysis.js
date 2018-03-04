import React from 'react';
import { connect } from 'react-redux';
import { compose, withProps, withHandlers } from 'recompose';
import { requestImageAnalysis } from 'actions';

import { isEmpty } from 'utils';

import ButtonAction from 'components/button/ButtonAction'

const enhance = compose(
    connect(
        state => ({
            selectedImageId: state.cnn.selectedImageId,
        }),
        dispatch => ({
            analyzeImage(imageId) {
                dispatch(requestImageAnalysis(imageId))
            },
        }),
    ),
    withHandlers({
        onClick: props => event => {
            props.analyzeImage(props.selectedImageId);    
        }
    })
);

export default enhance(ButtonAction);