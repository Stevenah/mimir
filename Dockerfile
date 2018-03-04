ARG cuda_version=8.0
ARG cudnn_version=6
FROM nvidia/cuda:${cuda_version}-cudnn${cudnn_version}-devel

ENV CONDA_DIR /opt/conda
ENV PATH $CONDA_DIR/bin:$PATH

# Prepare enviroment
RUN mkdir -p $CONDA_DIR && \
    echo export PATH=$CONDA_DIR/bin:'$PATH' > /etc/profile.d/conda.sh && \
    apt-get update && \
    apt-get install -y wget git libhdf5-dev g++ graphviz openmpi-bin nginx supervisor libgl1-mesa-glx && \
    wget --quiet https://repo.continuum.io/miniconda/Miniconda3-4.2.12-Linux-x86_64.sh && \
    echo "c59b3dd3cad550ac7596e0d599b91e75d88826db132e4146030ef471bb434e9a *Miniconda3-4.2.12-Linux-x86_64.sh" | sha256sum -c - && \
    /bin/bash /Miniconda3-4.2.12-Linux-x86_64.sh -f -b -p $CONDA_DIR && \
    rm Miniconda3-4.2.12-Linux-x86_64.sh

# Python
ARG python_version=3.6

# Setup python enviroment
RUN conda install -y python=${python_version} && \
    pip install --upgrade pip && \
    pip install tensorflow-gpu && \
    pip install tensorflow && \
    conda install Pillow scikit-learn notebook pandas matplotlib mkl nose pyyaml six h5py scipy numpy && \
    conda install -c menpo opencv && \
    pip install sklearn_pandas && \
    pip install git+git://github.com/keras-team/keras.git@2.0.8 && \
    conda clean -yt 

# Setup flask application
RUN mkdir -p /deploy/app
COPY . /deploy/app
RUN pip install -r /deploy/app/requirements.txt

# Setup gunicorn
RUN pip install gunicorn

# Setup nginx
RUN rm /etc/nginx/sites-enabled/default
COPY config/flask.conf /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/flask.conf /etc/nginx/sites-enabled/flask.conf
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# Setup supervisord
RUN mkdir -p /var/log/supervisord
COPY config/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Start process
CMD ["/usr/bin/supervisord"]

