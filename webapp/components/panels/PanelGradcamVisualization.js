import React from 'react';
import { connect } from 'react-redux';
import { compose, withProps, nest, lifecycle } from 'recompose';
import { requestGuidedGradCam } from 'actions';

import Panel from 'layout/Panel';
import ShowcaseImage from 'components/ui/ShowcaseImage';

const enhance = compose(
    connect(
        state => ({
            source: state.cnn.selectedGuidedGradCam,
            loading: state.loading.analysis,
        })
    ),
    withProps(props => ({
        emptyMessage: 'A gradcam representation of the image will appear here',
        isEmpty: !props.source
    }))
);

export default enhance(
    nest(Panel, ShowcaseImage)
);