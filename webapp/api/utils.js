export const handleErrors = response => {
    if (!response.ok) {
        throw Error(response.statusText);
    }

    return response;
};

export const getOptions = () => ({
    method: 'GET',
});

export const jsonHeaders = () => ({
    "Content-Type": "application/json",
});

export const postJsonOptions = () => {
    return ({
        headers: jsonHeaders(),
        origin: "*",
        method: 'POST',
})};

export const getJsonOptions = () => ({
    headers: jsonHeaders(),
    ...getOptions,
    dataType: 'json',
});