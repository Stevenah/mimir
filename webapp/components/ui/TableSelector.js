import React, { Component } from 'react';
import { Icon, Label, Menu, Table } from 'semantic-ui-react'
import classnames from 'classnames';

import 'style/ui/TableSelector.scss'

const defaultClassNames = [
    'selection-table',
    'analysis-table',
];

class TableSelector extends Component {

    static defaultProps = {
        classNames: [],
        header: [],
        content: [],
    }

    buildHeaderRows = () => {
        return (
            <Table.Row className='table-selection-row'> 
                {this.props.header.map(header => (
                    <Table.HeaderCell className='table-selection-header-cell'>
                        {header}
                    </Table.HeaderCell>
                ))}
            </Table.Row>
        );
    }

    buildBodyRows = () => {
        return this.props.content.map((content, i) => {
            
            let classNames = classnames({
                'table-selection-row': true,
                'clickable': true,
                'selected': i === this.props.selectedRow,
            });

            return (
                <Table.Row onClick={() => this.props.onClick(i)} className={classNames}>
                    {content.map(element => (
                        <Table.Cell>
                            {element}
                        </Table.Cell>
                    ))}
                </Table.Row>
            )
        });
    }

    render() {

        let classNames = classnames(
            defaultClassNames,
            this.props.classNames,
        );
        
        return (
            <div className={"test"}>
                <Table basic className={classNames}>
                    <Table.Header>
                        {this.buildHeaderRows()}
                    </Table.Header>
                    <Table.Body className='selection-table-body'>
                        {this.buildBodyRows()}
                    </Table.Body>
                </Table>
            </div>
        );
    }
}

export default TableSelector