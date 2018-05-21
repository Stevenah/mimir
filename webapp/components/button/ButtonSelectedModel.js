import React from 'react';
import { connect } from 'react-redux';
import { compose, withProps, withHandlers, lifecycle, defaultProps } from 'recompose';

import { isEmpty } from 'utils';

import ButtonCover from 'components/button/ButtonCover'
import { requestActiveModel } from '../../actions';

const enhance = compose(
    connect(
        state => ({
            activeModel: state.cnn.activeModelName
        }),
        dispatch => ({
            requestActiveModel() {
                dispatch(requestActiveModel());
            }
        })
    ),
    defaultProps({
        activeModel: 'None'
    }), 
    lifecycle({
        componentWillMount() {
            this.props.requestActiveModel();
        }
    }),
    withProps(props => ({
        label: props.activeModel,
    })),
    withHandlers({
        onClick: props => event => {
            console.log("Selected Model clicked!")
        }
    })
);

export default enhance(ButtonCover);