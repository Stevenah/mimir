import React, { Component } from 'react';
import { connect } from 'react-redux';
import { compose, withProps } from 'recompose';
import { requestFiles } from 'actions';

import Dropzone from 'components/ui/Dropzone';

const enhance = compose(
    connect(
        null,
        dispatch => ({
            onDrop(files) {
                dispatch(requestFiles(files))
            }
        })
    ),
    withProps(
        props => ({
            style: {
                width: '100%',
                height: '100%',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center'
            },
            className: 'clickable'
        })
    )
)

export default enhance(Dropzone);