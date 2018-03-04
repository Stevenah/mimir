import React from 'react';
import { connect } from 'react-redux';
import { compose, withProps, nest, withHandlers, lifecycle, defaultProps } from 'recompose';
import { requestCnnClasses, selectCnnClass, requestSelectedVisualization } from 'actions';

import Panel from 'layout/Panel'
import TableSelector from 'components/ui/TableSelector';

const enhance = compose(
    connect(
        state => ({
            classes: state.cnn.classes,
            imageId: state.cnn.selectedImageId,
            selectedRow: Number(state.cnn.selectedClass),
            classification: state.cnn.classifications[state.cnn.selectedImageId],
        }),
        dispatch => ({
            requestCnnClasses() {
                dispatch(requestCnnClasses());
            },
            selectVisualizationTarget(classId){
                dispatch(selectCnnClass(classId));
                dispatch(requestSelectedVisualization());
            },
        })
    ),
    defaultProps({
        classification: [],
    }),
    withHandlers({
        onClick: props => rowIndex => {
            props.selectVisualizationTarget(
                Object.keys(props.classes)[rowIndex]
            );
        },
    }),
    withProps(props => ({
        isEmpty: !props.imageId,
        header: [ 'Class', 'Probability' ],
        content: props.classes.map(label => [label, `${(Number(props.classification[label]) * 100).toFixed(3).replace(/\.0+$/,'')}%`]),
        emptyMessage: 'List of targets will be listed here',
    })),
    lifecycle({
        componentWillMount() {
            this.props.requestCnnClasses();     
        },
    })
);

export default enhance(nest(Panel, TableSelector));