import React from 'react';
import { connect } from 'react-redux';
import { compose, withProps, nest, withHandlers, lifecycle } from 'recompose';
import { requestCnnLayers, selectCnnLayer, requestSelectedVisualization } from 'actions';

import Panel from 'layout/Panel'
import TableSelector from 'components/ui/TableSelector';

const enhance = compose(
    connect(
        state => ({
            layers: state.cnn.layers,
            imageId: state.cnn.selectedImageId,
            selectedRow: state.cnn.layers.indexOf(state.cnn.selectedLayer),
        }),
        dispatch => ({
            requestCnnLayers() {
                dispatch(requestCnnLayers());
            },
            selectVisualizationLayer(layerId){
                dispatch(selectCnnLayer(layerId));
                dispatch(requestSelectedVisualization());
            },
        })
    ),
    withHandlers({
        onClick: props => rowIndex => {
            props.selectVisualizationLayer(Object.keys(props.layers)[rowIndex])
        },
    }),
    withProps(props => ({
        isEmpty: !props.imageId,
        header: ['Layer Name'],
        content: props.layers.map(layerName =>  [layerName]),
        emptyMessage: 'The result of the file analysis will appear here',
    })),
    lifecycle({
        componentWillMount() {
            this.props.requestCnnLayers();     
        },
    })
);

export default enhance(nest(Panel, TableSelector));