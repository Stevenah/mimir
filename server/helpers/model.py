
def upload_model(form_attributes):

        submission_id = form_attributes['submission_id']
        button_id = form_attributes['buttonId']
        file_name = form_attributes['qqfilename']

        model = NeuralNet.create(submission_id)

        with open(os.path.join(MODEL_STORAGE_PATH, file_name), 'wb+') as f:
            f.write(file.read())

        if model is None:

            model_file = open(file_path, 'rb').read() if button_id == 'model_file_input' else None
            class_file = open(file_path, 'rb').read() if button_id == 'class_file_input' else None

            model = Architecture(model_name, dataset_name, description,
                model_file, class_file, submission_id)

            db.session.add(model)
            db.session.commit()
            
        else:
            if button_id == 'model_file_input':
                model.model_file = open(file_path, 'rb').read()
            else:
                model.class_file = open(file_path, 'rb').read()
            db.session.commit()