import React, { Component } from 'react'
import classnames from 'classnames';

import 'style/button/ButtonUpload.scss';

class ButtonUpload extends Component {

    static defaultProps = {
        label: 'Upload file',
        classNames: [],
    }

    render() {
        let classNames = classnames(
            this.props.classNames
        );

        let label = this.props.children ? 
            this.props.children : this.props.label;

        return (
            <div className={classNames} style={{marginTop: "5px"}}>
                <input onChange={this.props.onChange}
                    type="file"
                    name="file-1[]"
                    id="file-1"
                    className="inputfile"
                    data-multiple-caption="{count} files selected"
                    multiple
                />
                <label htmlFor="file-1">
                    <span className="link-button">
                        {label}
                    </span>
                </label>
            </div>
        );
    }
}

export default ButtonUpload;