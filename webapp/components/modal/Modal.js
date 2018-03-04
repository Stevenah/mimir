import React, { Component } from 'react';
import { connect } from 'react-redux';
import { compose, withHandlers, defaultProps } from 'recompose';

import { closeModal } from 'actions';

import { Modal as SemanticModal, Button } from 'semantic-ui-react'

const enhance = compose(
    connect(
        null,
        dispatch => ({
            closeModal() {
                dispatch(closeModal());
            },
        }),
    ),
    defaultProps({
        open: true,
        dimmer: false,
        actions: [],
        style: {
        }
    })
);

const Modal = props =>
    <SemanticModal
        style={props.style}
        dimmer={props.dimmer}
        onClose={ props.closeModal }
        open={ props.open }
        closeOnDocumentClick
    >
        <SemanticModal.Header>
            {props.header}
        </SemanticModal.Header>
        <SemanticModal.Content
            scrolling
        >
            {props.children}
        </SemanticModal.Content>
        <SemanticModal.Actions>
            {props.actions}
        </SemanticModal.Actions>
    </SemanticModal>

export default enhance(Modal);