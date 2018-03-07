import React from 'react';
import { connect } from 'react-redux';
import { compose, branch, renderComponent } from 'recompose';

import ButtonAction from 'components/button/ButtonAction';
import ButtonAttachFile from 'components/button/ButtonAttachFile';
import ButtonDetachFile from 'components/button/ButtonDetachFile';

const enhance = compose(
    connect(
        state => ({
            imageId: state.app.selectedImageId,
            image: state.app.images[state.app.selectedImageId],
        })
    ),
    branch(
        props => props.image && !props.image.attached,
        renderComponent(ButtonAttachFile),
        renderComponent(ButtonDetachFile)
    )
);

export default enhance(ButtonAction);