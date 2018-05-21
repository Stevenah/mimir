import React from 'react';
import { connect } from 'react-redux';
import { compose, withProps, nest, withHandlers, lifecycle, defaultProps } from 'recompose';
import { requestCnnClasses, selectCnnClass, requestImageVisualization } from 'actions';

import Panel from 'layout/Panel'
import TableSelector from 'components/ui/TableSelector';
import { prettyProbability } from 'utils';
import {  } from 'actions';

const enhance = compose(
    connect(
        state => ({
            classes: state.cnn.classes,
            imageId: state.cnn.selectedImageId,
            layerId: state.cnn.selectedLayer,
            classId: state.cnn.selectedClass,
            selectedRow: state.cnn.selectedClass,
            classification: state.cnn.classifications[state.cnn.selectedImageId],
            loading: state.loading.classes
        }),
        dispatch => ({
            requestCnnClasses() {
                dispatch(requestCnnClasses());
            },
            selectVisualizationTarget(imageId, layerId, classId){
                dispatch(selectCnnClass(classId));
                dispatch(requestImageVisualization(imageId, layerId, classId));
            },
        })
    ),
    defaultProps({
        classification: [],
    }),
    withHandlers({
        onClick: props => rowId => {
            props.selectVisualizationTarget(
                props.imageId,
                props.layerId,
                rowId,
            );
        },
    }),
    withProps(props => ({
        isEmpty: !props.imageId,
        header: [ 'Class', 'Probability' ],
        sorter: (a, b) => props.classification[props.classes[b.id]] - props.classification[props.classes[a.id]],
        rows: Object.keys(props.classes).map(rowId => ({
            id: rowId,
            content: [ 
                props.classes[rowId], 
                prettyProbability(props.classification[props.classes[rowId]])
            ]
        })),
        emptyMessage: 'List of targets will be listed here',
    })),
    lifecycle({
        componentWillMount() {
            this.props.requestCnnClasses();     
        },
    })
);

export default enhance(nest(Panel, TableSelector));