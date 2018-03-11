import React from 'react';
import { connect } from 'react-redux';
import { compose, withProps, branch, nest, renderComponent, defaultProps } from 'recompose';
import { getSelectedFileFromState } from 'utils';

import { isEmpty } from 'utils';

import Panel from 'layout/Panel';
import ImageDescription from 'components/ui/ImageDescription';

const prettifyClassificationResult = classifications => {

    if (!classifications) {
        return null;
    }

    const prediction = Object.keys(classifications)
        .reduce((max, next) => 
            classifications[next] > classifications[max] ? 
                next : max);
                
    return `The image you selected has a ${(classifications[prediction] * 100).toFixed(3).replace(/\.0+$/,'')}% probability of containing ${prediction}`;
}

const enhance = compose(
    connect(
        state => ({
            selectedClassification: state.cnn.classifications[state.cnn.selectedImageId],
            loading: state.loading.classification
        })
    ),
    withProps(props => ({
        description: prettifyClassificationResult(props.selectedClassification),
        emptyMessage: 'A brief explination of the analyzed file will appear here',
        isEmpty: !props.selectedClassification,
    })),
);

export default enhance(nest(Panel, ImageDescription));