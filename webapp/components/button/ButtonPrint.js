import React from 'react';
import { connect } from 'react-redux';
import { compose, withProps, withHandlers } from 'recompose';

import { isEmpty } from 'utils';

import ButtonCover from 'components/button/ButtonCover'

const enhance = compose(
    withProps(props => ({
        label: 'Print',
    })),
    withHandlers({
        onClick: props => event => {
            console.log("printing...")
        }
    })
);

export default enhance(ButtonCover);