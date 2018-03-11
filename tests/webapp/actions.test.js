import * as actions from '../../webapp/actions';

describe('actionCreator', () => {
    test('that empty object is true', () => {

        const type = 'TEST',
              payload = { message: 'test' }

        expect(actions.actionCreator(type)(payload)).toEqual({
            type,
            payload,
            meta: {},
            error: {},
        });
    });
});

describe('imageVisualization', () => {
    test('request', () => {

        const id = '1';

        expect(actions.requestImageVisualization(id, id, id)).toEqual({
            type: 'REQUEST_IMAGE_VISUALIZATION',
            payload: {
                imageId: id,
                layerId: id,
                classId: id,
            },
            meta: {},
            error: {},
        });
    });

    test('receive', () => {

        const id = '1';
        const response = {
            'gradCam': 'test',
            'guidedGradCam': 'test'
        };

        expect(actions.receiveImageVisualization(response, id, id, id)).toEqual({
            type: 'RECEIVE_IMAGE_VISUALIZATION',
            payload: {
                gradCam: 'test',
                guidedGradCam: 'test',
                imageId: '1-1-1',
                layerId: id,
                classId: id,
            },
            meta: {},
            error: {},
        });
    });

    test('error', () => {
        const error = 'error';
        expect(actions.rejectImageVisualization(error)).toEqual({
            type: 'REJECT_IMAGE_VISUALIZATION',
            payload: { error },
            meta: {},
            error: {},
        });
    });
});

describe('images', () => {
    test('receive', () => {
        expect(actions.requestImages()).toEqual({
            type: 'REQUEST_IMAGES',
        });
    });

    test('request', () => {

        const response = {
            images: [{
                id: '1',
                source: 'source'
            }]
        };

        expect(actions.receiveImages(response)).toEqual({
            type: 'RECEIVE_IMAGES',
            payload: {
                images: {
                    '1': {
                        id: '1',
                        source: 'data:image/jpeg;base64,source',
                        selected: false,
                        loading: false,
                        attached: false,
                        type: 'image',
                    }
                }
            },
            meta: {},
            error: {},
        });
    });

    test('error', () => {
        const error = 'error';
        expect(actions.rejectImages(error)).toEqual({
            type: 'REJECT_IMAGES',
            payload: { error },
            meta: {},
            error: {},
        });
    });
});

describe('classes', () => {
    test('receive', () => {
        expect(actions.requestCnnClasses()).toEqual({
            type: 'REQUEST_CNN_CLASSES',
        });
    });

    test('request', () => {

        const response = {
            classes: [
                'test_1',
                'test_2',
                'test_3',
            ],
        };

        expect(actions.receiveCnnClasses(response)).toEqual({
            type: 'RECEIVE_CNN_CLASSES',
            payload: {
                classes: response.classes,
            },
            meta: {},
            error: {},
        });
    });

    test('error', () => {
        const error = 'error';
        expect(actions.rejectCnnClasses(error)).toEqual({
            type: 'REJECT_CNN_CLASSES',
            payload: {
                error
            },
            meta: {},
            error: {},
        });
    });

    test('select', () => {
        const id = '1';
        expect(actions.selectCnnClass(id)).toEqual({
            type: 'SELECT_CNN_CLASS',
            payload: {
                classId: '1'
            },
            meta: {},
            error: {},
        });
    });
});

describe('layers', () => {
    test('receive', () => {
        expect(actions.requestCnnLayers()).toEqual({
            type: 'REQUEST_CNN_LAYERS',
        });
    });

    test('request', () => {

        const response = {
            layers: [
                'test_1',
                'test_2',
                'test_3',
            ],
        };

        expect(actions.receiveCnnLayers(response)).toEqual({
            type: 'RECEIVE_CNN_LAYERS',
            payload: {
                layers: response.layers,
            },
            meta: {},
            error: {},
        });
    });

    test('error', () => {
        const error = 'error';
        expect(actions.rejectCnnLayers(error)).toEqual({
            type: 'REJECT_CNN_LAYERS',
            payload: {
                error
            },
            meta: {},
            error: {},
        });
    });

    test('select', () => {
        const id = '1';
        expect(actions.selectCnnLayer(id)).toEqual({
            type: 'SELECT_CNN_LAYER',
            payload: {
                layerId: '1'
            },
            meta: {},
            error: {},
        });
    });
});

describe('classification', () => {
    test('receive', () => {
        const id = '1'
        expect(actions.requestCnnClassification(id)).toEqual({
            type: 'REQUEST_CNN_CLASSIFICATION',
            payload: {
                imageId: '1',
            },
            meta: {},
            error: {},
        });
    });

    test('request', () => {

        const id = '1';
        const response = {
            classification: {
                'class_1': '.95',
            }
        };

        expect(actions.receiveCnnClassification(response, id)).toEqual({
            type: 'RECEIVE_CNN_CLASSIFICATION',
            payload: {
                imageId: '1',
                classification: response.classification,
            },
            meta: {},
            error: {},
        });
    });

    test('error', () => {
        const error = 'error';
        expect(actions.rejectCnnClassification(error)).toEqual({
            type: 'REJECT_CNN_CLASSIFICATION',
            payload: { error },
            meta: {},
            error: {},
        });
    });
});

describe('image attachements', () => {
    test('attach', () => {
        const id = '1'
        expect(actions.attachFile(id)).toEqual({
            type: 'ATTACH_FILE',
            payload: { imageId: '1', },
            meta: {},
            error: {},
        });
    });

    test('detach', () => {
        const id = '1';
        expect(actions.detachFile(id)).toEqual({
            type: 'DETACH_FILE',
            payload: { imageId: '1', },
            meta: {},
            error: {},
        });
    });
});

describe('setters', () => {
    test('file', () => {
        const id = '1'
        expect(actions.selectFile(id)).toEqual({
            type: 'SELECT_FILE',
            payload: { fileId: '1', },
            meta: {},
            error: {},
        });
    });

    test('textfield', () => {
        const value = '1';
        const field = 'test';
        expect(actions.setTextField(field, value)).toEqual({
            type: 'SET_TEXT_FIELD',
            payload: { 
                value,
                field: 'test',
            },
            meta: {},
            error: {},
        });
    });

    test('api', () => {
        const url = 'test.com';
        expect(actions.setApiUrl(url)).toEqual({
            type: 'SET_API_URL',
            payload: { apiUrl: url },
            meta: {},
            error: {},
        });
    });
});

describe('upload', () => {
    test('upload', () => {
        expect(actions.requestFileUpload()).toEqual({
            type: 'REQUEST_FILE_UPLOAD',
        });
    });
});
