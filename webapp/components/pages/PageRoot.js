import React, { Component } from 'react'
import 'style/pages/PageRoot.scss';

const PageRoot = props =>
    <article>
        { props.children }
    </article>

export default PageRoot;