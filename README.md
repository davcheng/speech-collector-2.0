**Open Speech Recording** is a small web application to collect short snippets
of speech, and upload them to cloud storage.

It's based around a small Flask app that will run on Google App Engine. This
serves up a client-side Javascript app that prompts for a series of words,
records the audio, and then POSTs the results back to the server.

## DEPLOYMENT INSTRUCTIONS

# 1. Project Creation
https://codelabs.developers.google.com/codelabs/cloud-vision-app-engine/index.html?index=..%2F..%2Findex#1
If you don't already have a Google Account (Gmail or Google Apps), you must create one. Sign-in to Google Cloud Platform console (console.cloud.google.com) and create a new project:

# 2. Billing
Next, you'll need to enable billing in the Cloud Console in order to use Google Cloud resources.

Running through this codelab shouldn't cost you more than a few dollars, but it could be more if you decide to use more resources or if you leave them running.

# 3. Google Cloud Shell
https://codelabs.developers.google.com/codelabs/cloud-vision-app-engine/index.html?index=..%2F..%2Findex#2
While Google Cloud can be operated remotely from your laptop, in this codelab we will be using Google Cloud Shell, a command line environment running in the Cloud. This Debian-based virtual machine is loaded with all the development tools you'll need (gcloud, python, virtualenv, pip and more), it offers a persistent 5GB home directory, and runs on the Google Cloud, greatly enhancing network performance and authentication. This means that all you will need for this codelab is a browser (yes, it works on a Chromebook).

To activate Google Cloud Shell, from the developer console simply click the button on the top right-hand side (it should only take a few moments to provision and connect to the environment):

# 4. Get code (done in Google Cloud Shell)
git clone

# 5. Enable the APIs (done in Google Cloud Shell)
gcloud service-management enable storage-component.googleapis.com
gcloud service-management enable storage-api.googleapis.com


# 6. Authenticate API requests (done in Google Cloud Shell)

gcloud auth application-default login
gcloud config set project speech-up-record-app


https://codelabs.developers.google.com/codelabs/cloud-vision-app-engine/index.html?index=..%2F..%2Findex#6
export PROJECT_ID=WHATEVER_YOU_CALL_PROJECT

# 7. Install dependencies (done in Google Cloud Shell)
use python2.7, not 3
virtualenv -p python env
source env/bin/activate
pip install -r requirements.txt

Then run this command to make a lib of requirements in main directory
pip install -t lib -r requirements.txt


## Running

To get started, you'll need to edit app.yaml to point to your own storage bucket
and update the session key. If you have the Google Cloud SDK set up, you should
be able to run a local copy with this command:

```
dev_appserver.py app.yaml
```

I've often had trouble getting local copies of the app to work with cloud
storage, so you may see errors on the final upload stage with this setup. To
deploy it to an appspot instance, run this:

```
gcloud app deploy
```

## Credits

Thanks to the Mozilla team for the [Web Dictaphone sample application](https://developer.mozilla.org/en-US/docs/Web/API/MediaStream_Recording_API/Using_the_MediaStream_Recording_API#A_sample_application_Web_Dictaphone)
that I used as a starting point, [Sole](https://soledadpenades.com/) for the
oscilloscope, and the Flask team for a lovely Python microframework!

Written by Pete Warden, pete@petewarden.com.
