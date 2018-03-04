import React from 'react';
import { connect } from 'react-redux';
import { compose, branch, renderComponent } from 'recompose';

import ButtonAction from 'components/button/ButtonAction';
import ButtonAttachFile from 'components/button/ButtonAttachFile';
import ButtonDetachFile from 'components/button/ButtonDetachFile';

import { getSelectedFileFromState } from 'utils';

const enhance = compose(
    connect(
        state => ({
            file: getSelectedFileFromState(state),
            attached: getSelectedFileFromState(state).attached,
        })
    ),
    branch(
        props => !props.attached,
        renderComponent(ButtonAttachFile),
        renderComponent(ButtonDetachFile)
    )
);

export default enhance(ButtonAction);