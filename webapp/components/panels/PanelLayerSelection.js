import React from 'react';
import { connect } from 'react-redux';
import { compose, withProps, nest, withHandlers, lifecycle } from 'recompose';
import { requestCnnLayers, selectCnnLayer, requestImageVisualization } from 'actions';

import Panel from 'layout/Panel'
import TableSelector from 'components/ui/TableSelector';

const enhance = compose(
    connect(
        state => ({
            layers: state.cnn.layers,
            imageId: state.cnn.selectedImageId,
            layerId: state.cnn.selectedLayer,
            classId: state.cnn.selectedClass,
            selectedRow: state.cnn.selectedLayer,
            loading: state.loading.layers,
        }),
        dispatch => ({
            requestCnnLayers() {
                dispatch(requestCnnLayers());
            },
            selectCnnLayer(layerIndex) {
                dispatch(selectCnnLayer(layerIndex));
            },
            selectVisualizationLayer(imageId, layerId, classId){
                dispatch(requestImageVisualization(imageId, layerId, classId));
            },
        })
    ),
    withHandlers({
        onClick: props => rowId => {
            props.selectCnnLayer(rowId);
            props.selectVisualizationLayer(
                props.imageId,
                rowId,
                props.classId
            );
        },
    }),
    withProps(props => ({
        isEmpty: !props.imageId,
        header: ['Layer Name'],
        sorter: (a, b) => Number(b.id) - Number(a.id),
        rows: Object.keys(props.layers).map(rowId => ({
            id: rowId,
            content: [ props.layers[rowId] ]
        })),
        emptyMessage: 'The result of the file analysis will appear here',
    })),
    lifecycle({
        componentWillMount() {
            this.props.requestCnnLayers();     
        },
    })
);

export default enhance(nest(Panel, TableSelector));