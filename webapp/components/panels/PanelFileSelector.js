import React from 'react';
import { connect } from 'react-redux';
import { compose, withProps, nest, lifecycle } from 'recompose';
import { selectFile, requestImages, requestImageVisualization, requestCnnClassification } from 'actions';

import { isEmpty } from 'utils';

import Panel from 'layout/Panel'
import ImageDropzone from 'components/ui/ImageDropzone';
import FileSelector from 'components/ui/FileSelector';



const enhance = compose(
    connect(
        state => ({
            files: state.app.images,
            loading: state.loading.files,
            selectedFile: state.cnn.selectedImageId,
            selectedLayer: state.cnn.selectedLayer,
            selectedClass: state.cnn.selectedClass,
        }),
        dispatch => ({
            requestImages() {
                dispatch(requestImages())
            },
            selectFile(imageId, layerId, classId) {
                dispatch(selectFile(imageId))
                dispatch(requestCnnClassification(imageId))
                dispatch(requestImageVisualization(imageId, layerId, classId))
            },
        }),
        (state, dispatch, ownProps) => ({
            ...ownProps,
            ...state,
            ...dispatch,
            selectFile(imageId) {
                dispatch.selectFile(imageId, state.selectedLayer, state.selectedClass)
            }
        })
    ),
    lifecycle({
        componentWillMount() {
            this.props.requestImages();
        }
    }),
    withProps(props => ({
        isEmpty: isEmpty(props.files),
        emptyMessage: ( <ImageDropzone /> ),
    }))
);

export default enhance(nest(Panel, FileSelector));