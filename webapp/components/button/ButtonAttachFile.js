import React from 'react';
import { connect } from 'react-redux';
import { compose, withProps, withHandlers } from 'recompose';
import { attachFile } from 'actions';

import { isEmpty } from 'utils';

import ButtonAction from 'components/button/ButtonAction'

const enhance = compose(
    connect(
        state => ({
            file: state.file.selectedFile,
        }),
        dispatch => ({
            attachImage(file) {
                dispatch(attachFile(file))
            },
        }),
    ),
    withProps(props => ({
        label: 'Attach Image',
    })),
    withHandlers({
        onClick: props => event => {
            if (!isEmpty(props.file)) {
                props.attachImage(props.file);
            }
        }
    })
);

export default enhance(ButtonAction);