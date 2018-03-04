import React from 'react';
import { connect } from 'react-redux';
import { compose, withProps, nest, lifecycle } from 'recompose';
import { selectFile, requestFileRefresh, requestSelectedVisualization, requestCnnClassification } from 'actions';
import { Icon } from 'semantic-ui-react'

import Panel from 'layout/Panel'
import ImageDropzone from 'components/ui/ImageDropzone';
import FileSelector from 'components/ui/FileSelector';

const enhance = compose(
    connect(
        state => ({
            loading: state.loading.file,
            files: state.file.files,
        }),
        dispatch => ({
            refreshFiles() {
                dispatch(requestFileRefresh())
            },
            selectFile(fileId) {
                dispatch(selectFile(fileId))
                dispatch(requestCnnClassification(fileId))
                dispatch(requestSelectedVisualization())
            },
        })
    ),
    lifecycle({
        componentWillMount() {
            this.props.refreshFiles();
        }
    }),
    withProps(props => ({
        emptyMessage: (
            <ImageDropzone>
                <Icon size='huge' name='image' />
            </ImageDropzone>
        ),
    }))
);

export default enhance(nest(Panel, FileSelector));