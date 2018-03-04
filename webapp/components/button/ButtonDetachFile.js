import React from 'react';
import { connect } from 'react-redux';
import { compose, withProps, withHandlers } from 'recompose';
import { detachFile } from 'actions';

import { isEmpty } from 'utils';

import ButtonAction from 'components/button/ButtonAction'

const enhance = compose(
    connect(
        state => ({
            file: state.file.selectedFile,
        }),
        dispatch => ({
            detachImage(file) {
                dispatch(detachFile(file))
            },
        }),
    ),
    withProps(props => ({
        label: 'Detach Image',
    })),
    withHandlers({
        onClick: props => event => {
            if (!isEmpty(props.file)) {
                props.detachImage(props.file);
            }
        }
    })
);

export default enhance(ButtonAction);