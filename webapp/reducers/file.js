import * as actions from 'constants';
import update from 'immutability-helper';
import { guid } from 'utils';

const initialState = {
    files: {},
    selectedFile: {},
    loading: false,
    selected: null,
};

const file = (state = initialState, action) => {
    switch (action.type) {
        
        case actions.RECEIVE_FILE_REFRESH:
            return update(state, {
                files: {$merge: action.payload.files}
            });

        case actions.REQUEST_IMAGE_ANALYSIS:
            return update(state, {
                files: {[action.payload.imageId]: {loading: {$set: true}}}
            });

        case actions.RECEIVE_IMAGE_ANALYSIS:
            return update(state, {
                files: {[action.payload.imageId]: {loading: {$set: false}}}
            });

        case actions.ATTACH_FILE:
            return update(state, {
                files: {[action.payload.file.id]: {attached: {$set: true}}}
            });

        case actions.DETACH_FILE:
            return update(state, {
                files: {[action.payload.file.id]: {attached: {$set: false}}}
            });

        case actions.SELECT_FILE:
            return update(state, {
                files: {
                    $apply: files => {
                        let updated = {}
                        Object.keys(files).forEach(fileId => {
                            updated[fileId] = update(files[fileId], {selected: {$set: fileId === action.payload.fileId}})
                        })
                        return updated;
                    }
                },
                selectedFile: {$set: state.files[action.payload.fileId]},
                selected: {$set: action.payload.fileId},
            });

        default:
            return state;
    }
};

export default file;