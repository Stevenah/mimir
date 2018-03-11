import Enzyme, { shallow, render, mount } from 'enzyme';
import { fetch } from 'whatwg-fetch';
import nock from 'nock';
import Adapter from 'enzyme-adapter-react-16';

const { JSDOM } = require('jsdom');

const jsdom = new JSDOM(`
    <!doctype html>
    <html>
        <body>
            <div id="app">
            </div>
        </body>
    </html>
`);

const { window } = jsdom;

Enzyme.configure({ adapter: new Adapter() });

global.window = window;
global.document = window.document;

global.shallow = shallow;
global.render = render;
global.mount = mount;
global.nock = nock;
global.fetch = fetch;

global.initialState = {
    app: {
        images: [],
        selectedImageId: null,
    },

    loading: {
        gradCam: {},
        guidedGradCam: {},
        layers: false,
        classes: false,
        files: false,
    },

    settings: {
        api: {
            url: '',
        }
    },

    cnn: {
        layers: [],
        classes: [],
        selectedClass: 6,
        selectedLayer: 'block5_conv4',
        classifications: {},
        originalImages: {},
        gradCamImages: {},
        guidedGradCamImages: {},    
    },

    report: {
        attachedImages: [],
        patientName: 'Windom Earle',
        dateOfBirth: '07.12.1993',
        generalPracticioner: 'Billy Gregg',
        hospitalNumber: '562346',
        dateOfProcedure: '27.09.2012',
        endoscopist: 'Dan Brownman',
        nurses: 'Jane Doe, Carol Smith',
        medications: 'Xylocaine Sprey',
        instrument: 'G15 - H260',
        extentOfExam: 'Second part of duodenum',
        visualization: 'Good',
        coMorbidity: 'None',
        indicationsForExamination: 'Survailence-Varices',
        procedurePerformed: 'Gastoscopy (OGD)',
        findings: 'Polyps',
        endoscopicDiagnosis: 'Varices. Esophageal. Furthger 4 bands applied',
        recommendations: 'High fiber diet.',
        followUp: 'High fiber diet',
        opsc4Code: 'G45 Gastroscopy (OGD)',
    }
}
