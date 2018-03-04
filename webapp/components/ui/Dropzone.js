import React, { Component } from 'react';
import Dropzone from 'react-dropzone';

export default props =>
    <Dropzone
        style={props.style}
        onDrop={props.onDrop}
        className={props.className}
    >
        {props.children}
    </Dropzone>