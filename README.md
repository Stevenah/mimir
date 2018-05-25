# Mimir Automatic Reporting
This is *Mimir*, an autoamtic reporting system aimed at medical doctors for endoscopic image analysis and reporting. May also be used to diagnose convolutional neural networks for potential imrpovements through the use of grad-CAM and guided grad-CAM visualizations.

## Getting Started
The following instructions should get you up and running with a local instance of Mimir.

### Before we start
It is recommended that Mimir is run on a computer using a GPU. Although Mimir will run on the CPU alone, it may be considerably less performant.

### Prerequisites
Before we run Mimir, we must first make sure the following programs are installed.

* Git - [Download & Install Git](https://git-scm.com/downloads) and git lfs to download the sample Keras models.
* Python 3.6+ - [Download & Install Python 3.6](https://www.python.org/downloads/) and the package manager pip.
* OpenCV 3.0+ - [Download & Install OpenCV 3](https://opencv.org/) and make sure it supports FFmpeg, this is required for video processing.
* SQLite - [Download & Install SQLite](https://www.sqlite.org/download.html).

### Installation
 Before we start, make sure that you clone this repository to your local computer by running `git clone https://github.com/stevenah/mimir` in the directory of your choice. With all prerequisites installed, running `pip -r install requirements.txt` should install all required python dependencies. This is all that is needed for a basic local instance of Mimir. To pull down the sample Keras models included with Mimir, run `git lfs pull` in the root directory.
 
### Usage
To start a local instance of Mimir, it should be enough to run the `app.py` file located in the `server` directory.

## Built With
* [Flask](http://flask.pocoo.org/) - The web framework used
* [React](https://reactjs.org/) - Front-end view library used
* [Keras](https://keras.io/) - Deep learning framework used
* [Tensorflow](https://www.tensorflow.org/) - Deep learning library used

## Authors
* **Steven Hicks** - *Work done as part of master thesis* - [Stevenah](https://github.com/Stevenah)

## License
This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](LICENSE.md) file for details
