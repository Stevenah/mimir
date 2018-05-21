import React from 'react';
import { connect } from 'react-redux';
import { compose, withProps, withHandlers } from 'recompose';

import { isEmpty } from 'utils';

import ButtonCover from 'components/button/ButtonCover'

const enhance = compose(
    withProps(props => ({
        label: 'Change Model',
    })),
    withHandlers({
        onClick: props => event => {
            console.log("Change model clicked!")
        }
    })
);

export default enhance(ButtonCover);