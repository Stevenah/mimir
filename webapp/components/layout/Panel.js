import React, { Component } from 'react';
import classnames from 'classnames';
import { compose, withProps, branch, nest, renderComponent, defaultProps } from 'recompose';
import { Grid, Loader } from 'semantic-ui-react';

import { isEmpty } from 'utils';

import 'style/layout/Panel.scss';

const PanelLoading = props =>
    <Grid.Row className='panel'>
        <div style={{position: 'relative', margin: '0 auto'}}>
            <Loader active />
        </div>
    </Grid.Row>

const PanelEmpty = props =>
    <Grid.Row className='panel'>
        {props.emptyMessage}
    </Grid.Row>

class Panel extends Component {
    render() {
        let classNames = classnames([
            'panel'
        ]);

        return (
            <Grid.Row className={classNames}>
                {this.props.children}
            </Grid.Row>
        );
    }
}

const enhance = compose(
    defaultProps({ 
        emptyMessage: '',
        loading: false,
    }),
    branch(
        props => props.loading,
        renderComponent(PanelLoading)
    ),
    branch(
        props => isEmpty(props.children) || props.isEmpty,
        renderComponent(PanelEmpty)
    )
);

export default enhance(Panel);