import React from 'react';
import { connect } from 'react-redux';
import { compose, withProps, nest, lifecycle } from 'recompose';

import Panel from 'layout/Panel';
import ShowcaseImage from 'components/ui/ShowcaseImage';

const enhance = compose(
    connect(
        state => ({
            guidedGradCam: state.cnn.guidedGradCamImages[`${state.cnn.selectedImageId}-${state.cnn.selectedLayer}-${state.cnn.selectedClass}`],
            loading: state.loading.guidedGradCam[`${state.cnn.selectedImageId}-${state.cnn.selectedLayer}-${state.cnn.selectedClass}`],
        })
    ),
    withProps(props => ({
        emptyMessage: 'A gradcam representation of the image will appear here',
        source: props.guidedGradCam ? 'data:image/jpeg;base64,' + props.guidedGradCam : '',
        isEmpty: !props.guidedGradCam
    })),
);

export default enhance(
    nest(Panel, ShowcaseImage)
);