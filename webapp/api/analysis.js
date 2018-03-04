import * as path from 'path';
import { handleErrors, postJsonOptions, getOptions, getJsonOptions } from 'api/utils';
import { dataURLtoFile } from 'utils';

export const analyzeImage = (imageId, apiUrl) =>
    fetch(`${apiUrl}/api/analyze/image/${imageId}`, postJsonOptions())
        .then(handleErrors)
        .then(response => response.json())
        .then(data => data)
        .catch(error => {
            throw error
        });

export const refreshFiles = (apiUrl) =>
    fetch(`${apiUrl}/api/file/get/all`, getOptions())
        .then(handleErrors)
        .then(response => response.json())
        .then(files => {
            let fileObj = {}
            files.files.forEach(file => {
                fileObj[file.uuid] = {
                    ...file,
                    selected: false,
                    loading: false,
                    attached: false,
                    thumbnail: "data:image/jpeg;base64," + file.file,
                    source: "data:image/jpeg;base64," + file.file,
                    id: file.uuid,
                    file: dataURLtoFile("data:image/jpeg;base64," + file.file, file.name)
                }
            });
            return fileObj;
        })
        .catch(error => {
            throw error
        });

export const getCnnLayers = url => {
    return fetch(`${url}/api/model/layers`, getOptions())
        .then(handleErrors)
        .then(response => response.json())
        .then(layers => layers.layers)
        .catch(error => { throw error; })
}

export const getCnnClasses = url => {
    return fetch(`${url}/api/model/classes`, getOptions())
        .then(handleErrors)
        .then(response => response.json())
        .then(classes => classes.classes)
        .catch(error => { throw error; })
}

export const requestCnnClassification = (imageId, url) => {
    return fetch(`${url}/api/model/classify/${imageId}`, getJsonOptions())
        .then(handleErrors)
        .then(response => response.json())
        .then(response => response.classification)
        .catch(error => { throw error; })
}