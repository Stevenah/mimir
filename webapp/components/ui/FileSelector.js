import React, { Component } from 'react';
import { connect } from 'react-redux';
import classnames from 'classnames';

import Image from 'components/ui/Image';

import 'style/ui/FileSelector.scss';

const defaultClasses = [
    'image-container',
];

const sortFiles = (a, b) => {
    return (a.id < b.id) ? -1 : (a.id > b.id) ? 1 : 0;
}

class FileSelector extends Component {

    static defaultProps = {
        classNames: [],
        files: [],
    }
    
    getFileArray = () => {
        return Object.keys(this.props.files).
            map(fileId => this.props.files[fileId]).sort(sortFiles);
    }
    
    render() {

        let classNames = classnames(
            defaultClasses,
            this.props.classNames,
        );

        return (
            <div className={classNames}>
                {this.getFileArray().map(file => (
                    <Image
                        width={100}
                        height={100}
                        key={file.id} 
                        selected={file.id === this.props.selectedFile}
                        loading={file.loading}
                        attached={file.attached}
                        label={file.type}
                        clickable={true}
                        src={file.source} 
                        onClick={() => this.props.selectFile(file.id)}
                    />
                ))}
            </div>
        );
    }
}

export default FileSelector;