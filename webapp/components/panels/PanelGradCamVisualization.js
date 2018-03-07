import React from 'react';
import { connect } from 'react-redux';
import { compose, withProps, nest, lifecycle } from 'recompose';
import { requestGradCam } from 'actions';

import Panel from 'layout/Panel';
import ShowcaseImage from 'components/ui/ShowcaseImage'; 

const enhance = compose(
    connect(
        state => ({
            gradCam: state.cnn.gradCamImages[`${state.cnn.selectedImageId}-${state.cnn.selectedLayer}-${state.cnn.selectedClass}`],
            loading: state.loading.gradCam[`${state.cnn.selectedImageId}-${state.cnn.selectedLayer}-${state.cnn.selectedClass}`],
        })
    ),
    withProps(props => ({
        emptyMessage: 'A heatmap representation of the image will appear here.',
        source: props.gradCam ? 'data:image/jpeg;base64,' + props.gradCam : '',
        isEmpty: !props.gradCam,
    })),
);

export default enhance(
    nest(Panel, ShowcaseImage)
);