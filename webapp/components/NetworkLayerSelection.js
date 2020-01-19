import React, { Component } from 'react';
import { connect } from 'react-redux';

import { List } from 'mimir-ui';
import { requestNetworkLayers, selectLayer, requestGradCam, requestGuidedGradCam } from 'actions';

class NetworkLayerSelection extends Component {

    componentDidMount() {
        this.props.requestNetworkLayers();
    }

    getListRows = () => {

        if (!this.props.networkLayers) {
            return [];
        }
        
        return this.props.networkLayers.map((layer, index) => (
            <List.Item
                key = { `layer_selection_${ index }` }
                selected={ layer.index === this.props.selectedLayer }
                onClick={ () => this.props.selectLayer(layer.index) }
            >
                { layer.name }
            </List.Item>
        ));
    }

    render() {
        return (
            <List>
                { this.getListRows() }
            </List>
        );
    }
}

export default connect(
    state => ({
        networkLayers: state.network.layers,
        selectedLayer: state.root.layer,
    }),
    dispatch => ({
        requestNetworkLayers: () => {
            dispatch(requestNetworkLayers(1));
        },
        selectLayer: layerId => {
            dispatch(selectLayer(layerId));
            dispatch(requestGradCam());
            dispatch(requestGuidedGradCam());
        },
    })
)(NetworkLayerSelection)