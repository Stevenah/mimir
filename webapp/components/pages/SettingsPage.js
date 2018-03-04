import React, { Component } from 'react';
import { Form } from 'semantic-ui-react'
import { connect } from 'react-redux';

import Panel from 'layout/Panel';
import PanelHeader from 'layout/PanelHeader';
import ContentGrid from 'layout/ContentGrid';
import ContentColumn from 'layout/ContentColumn';
import HeaderGrid from 'layout/HeaderGrid';
import HeaderColumn from 'layout/HeaderColumn';
import ContentRow from 'layout/ContentRow';

import { compose, withProps, branch, nest, renderComponent } from 'recompose';
import { setApiUrl } from 'actions';

const SettingsPage = props =>
    <div>
        <HeaderGrid>
            <HeaderColumn>
                <PanelHeader />
            </HeaderColumn>
        </HeaderGrid>
        <ContentGrid>
            <ContentColumn>
                    <Form>
                        <Form.Field style={{width: "20em", margin: "10px"}}>
                            <label style={{color: "white"}}>Set api url</label>
                            <input onChange={(e) => props.setUrl(e.target.value)} placeholder='url' value={props.apiUrl} />
                        </Form.Field>                        
                    </Form>
            </ContentColumn>
        </ContentGrid>
    </div>


const enhance = compose(
    connect(
        state => ({
            apiUrl: state.settings.api.url
        }),
        dispatch => ({
            setUrl(url) {
                dispatch(setApiUrl(url));
            }
        })
    )
)

export default enhance(SettingsPage);

