import React from 'react';
import { connect } from 'react-redux';
import { compose, withProps, nest } from 'recompose';

import Panel from 'layout/Panel'
import PanelShowcaseImage from 'components/ui/ShowcaseImage'; 

const enhance = compose(
    connect(
        state => ({
            source: state.cnn.selectedImageSource,
        })
    ),
    withProps(props => ({
        emptyMessage: 'The result of the file analysis will appear here',
        isEmpty: !props.source,
    })),
);

export default enhance(nest(Panel, PanelShowcaseImage));