**Open Speech Recording** is a small web application to collect short snippets
of speech, and upload them to cloud storage. It's designed to help gather open
speech data sets to train machine learning systems.

It's based around a small Flask app that will run on Google App Engine. This
serves up a client-side Javascript app that prompts for a series of words,
records the audio, and then POSTs the results back to the server.

## Install gcloud
https://cloud.google.com/sdk/docs/quickstart-mac-os-x
./google-cloud-sdk/install.sh
source '[path-to-my-home]/google-cloud-sdk/path.bash.inc'
source '[path-to-my-home]/google-cloud-sdk/completion.bash.inc'

gcloud not found?
source path.bash.inc
source completion.bash.inc


https://codelabs.developers.google.com/codelabs/cloud-vision-app-engine/index.html?index=..%2F..%2Findex#6
export PROJECT_ID=speech-up-voice-collector
gcloud iam service-accounts create voice-data-app --display-name "voice data app key"

gcloud projects add-iam-policy-binding speech-up-voice-collector --member serviceAccount:voice-data-app@${PROJECT_ID}.iam.gserviceaccount.com --role roles/owner

gcloud iam service-accounts keys create ~/key.json --iam-account voice-data-app@speech-up-voice-collector.iam.gserviceaccount.com

export GOOGLE_APPLICATION_CREDENTIALS="/home/${USER}/key.json"

step 1:
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt

KEY ERROR CLOUD_STORAGE_BUCKET
export CLOUD_STORAGE_BUCKET=${PROJECT_ID}
sudo gsutil mb gs://${PROJECT_ID}

pip install google-cloud -t [my_project]/lib/google/cloud

pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2


https://stackoverflow.com/questions/41905503/module-google-auth-httplib2-not-found-after-pip-installing-google-cloud-how-can
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
