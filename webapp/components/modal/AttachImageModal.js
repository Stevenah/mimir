import React, { Component } from 'react';
import { compose, withHandlers, nest, defaultProps, withProps } from 'recompose';

import Modal from 'components/modal/Modal';
import { Button, Image } from 'semantic-ui-react';

const enhance = compose(
    withProps(
        props => ({
            header: 'Attach Images',
            actions: [
                <Button color='red'>
                  Cancel
                </Button>,
                <Button positive>
                    Attach
                </Button>
            ]
        }),
    )
)

const Test = () => 
    <div style={{display: "flex", width: '100%', alignItems: "center", alignContent: 'center', justifyContent: "center"}}>
        <Image.Group 
            size='small'
            style={{display: "flex", width: '100%', alignItems: "center", alignContent: 'center', flexWrap: 'wrap', justifyContent: "center"}}>
            <Image src={'pic1.jpg'} />
            <Image src={'pic2.jpg'} />
            <Image src={'pic3.jpg'} />
            <Image src={'pic4.jpg'} />
            <Image src={'pic1.jpg'} />
            <Image src={'pic2.jpg'} />
            <Image src={'pic3.jpg'} />
            <Image src={'pic4.jpg'} />
            <Image src={'pic1.jpg'} />
            <Image src={'pic2.jpg'} />
            <Image src={'pic3.jpg'} />
            <Image src={'pic4.jpg'} />
            <Image src={'pic1.jpg'} />
            <Image src={'pic2.jpg'} />
            <Image src={'pic3.jpg'} />
            <Image src={'pic4.jpg'} />
            <Image src={'pic1.jpg'} />
            <Image src={'pic2.jpg'} />
            <Image src={'pic3.jpg'} />
            <Image src={'pic4.jpg'} />
            <Image src={'pic1.jpg'} />
            <Image src={'pic2.jpg'} />
            <Image src={'pic3.jpg'} />
            <Image src={'pic4.jpg'} />
            <Image src={'pic1.jpg'} />
            <Image src={'pic2.jpg'} />
            <Image src={'pic3.jpg'} />
            <Image src={'pic4.jpg'} />
            <Image src={'pic1.jpg'} />
            <Image src={'pic2.jpg'} />
            <Image src={'pic3.jpg'} />
            <Image src={'pic4.jpg'} />
            <Image src={'pic1.jpg'} />
            <Image src={'pic2.jpg'} />
            <Image src={'pic3.jpg'} />
            <Image src={'pic4.jpg'} />
            <Image src={'pic1.jpg'} />
            <Image src={'pic2.jpg'} />
            <Image src={'pic3.jpg'} />
            <Image src={'pic4.jpg'} />
            <Image src={'pic1.jpg'} />
            <Image src={'pic2.jpg'} />
            <Image src={'pic3.jpg'} />
            <Image src={'pic4.jpg'} />
            <Image src={'pic1.jpg'} />
            <Image src={'pic2.jpg'} />
            <Image src={'pic3.jpg'} />
            <Image src={'pic4.jpg'} />
            <Image src={'pic1.jpg'} />
            <Image src={'pic2.jpg'} />
            <Image src={'pic3.jpg'} />
            <Image src={'pic4.jpg'} />
            <Image src={'pic1.jpg'} />
            <Image src={'pic2.jpg'} />
            <Image src={'pic3.jpg'} />
            <Image src={'pic4.jpg'} />
            <Image src={'pic1.jpg'} />
            <Image src={'pic2.jpg'} />
            <Image src={'pic3.jpg'} />
            <Image src={'pic4.jpg'} />
            <Image src={'pic1.jpg'} />
            <Image src={'pic2.jpg'} />
            <Image src={'pic3.jpg'} />
            <Image src={'pic4.jpg'} />
            <Image src={'pic1.jpg'} />
            <Image src={'pic2.jpg'} />
            <Image src={'pic3.jpg'} />
            <Image src={'pic4.jpg'} />
            <Image src={'pic1.jpg'} />
            <Image src={'pic2.jpg'} />
            <Image src={'pic3.jpg'} />
            <Image src={'pic4.jpg'} />
            <Image src={'pic1.jpg'} />
            <Image src={'pic2.jpg'} />
            <Image src={'pic3.jpg'} />
            <Image src={'pic4.jpg'} />
            <Image src={'pic1.jpg'} />
            <Image src={'pic2.jpg'} />
            <Image src={'pic3.jpg'} />
            <Image src={'pic4.jpg'} />
            <Image src={'pic1.jpg'} />
            <Image src={'pic2.jpg'} />
            <Image src={'pic3.jpg'} />
            <Image src={'pic4.jpg'} />
            <Image src={'pic1.jpg'} />
            <Image src={'pic2.jpg'} />
            <Image src={'pic3.jpg'} />
            <Image src={'pic4.jpg'} />
            <Image src={'pic1.jpg'} />
            <Image src={'pic2.jpg'} />
            <Image src={'pic3.jpg'} />
            <Image src={'pic4.jpg'} />
            <Image src={'pic1.jpg'} />
            <Image src={'pic2.jpg'} />
            <Image src={'pic3.jpg'} />
            <Image src={'pic4.jpg'} />
            <Image src={'pic1.jpg'} />
            <Image src={'pic2.jpg'} />
            <Image src={'pic3.jpg'} />
            <Image src={'pic4.jpg'} />
            <Image src={'pic1.jpg'} />
            <Image src={'pic2.jpg'} />
            <Image src={'pic3.jpg'} />
            <Image src={'pic4.jpg'} />
            <Image src={'pic1.jpg'} />
            <Image src={'pic2.jpg'} />
            <Image src={'pic3.jpg'} />
            <Image src={'pic4.jpg'} />
            <Image src={'pic1.jpg'} />
            <Image src={'pic2.jpg'} />
            <Image src={'pic3.jpg'} />
            <Image src={'pic4.jpg'} />
            <Image src={'pic1.jpg'} />
            <Image src={'pic2.jpg'} />
            <Image src={'pic3.jpg'} />
            <Image src={'pic4.jpg'} />
            <Image src={'pic1.jpg'} />
            <Image src={'pic2.jpg'} />
            <Image src={'pic3.jpg'} />
            <Image src={'pic4.jpg'} />
            <Image src={'pic1.jpg'} />
            <Image src={'pic2.jpg'} />
            <Image src={'pic3.jpg'} />
            <Image src={'pic4.jpg'} />
            <Image src={'pic1.jpg'} />
            <Image src={'pic2.jpg'} />
            <Image src={'pic3.jpg'} />
            <Image src={'pic4.jpg'} />
            <Image src={'pic1.jpg'} />
            <Image src={'pic2.jpg'} />
            <Image src={'pic3.jpg'} />
            <Image src={'pic4.jpg'} />
        </Image.Group>  
    </div>


export default enhance(nest(Modal, Test));