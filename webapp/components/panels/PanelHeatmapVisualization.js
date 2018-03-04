import React from 'react';
import { connect } from 'react-redux';
import { compose, withProps, nest, lifecycle } from 'recompose';
import { requestGradCam } from 'actions';

import Panel from 'layout/Panel';
import ShowcaseImage from 'components/ui/ShowcaseImage'; 

const enhance = compose(
    connect(
        state => ({
            source: state.cnn.selectedGradCam,
            loading: state.loading.analysis,
        })
    ),
    withProps(props => ({
        emptyMessage: 'A heatmap representation of the image will appear here.',
        isEmpty: !props.source
    })),
);

export default enhance(
    nest(Panel, ShowcaseImage)
);