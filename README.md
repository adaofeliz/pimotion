Pimotion
========

![PIMotion Logo](docs/logo-256.png?raw=true)

Pimotion is a motion detector application that runs on the Raspberry PI. It captures snapshots of movement and uploads the montage image to Dropbox.

### Prerequisites

* A Dropbox App token, that can be generated at [Dropbox Apps](https://www.dropbox.com/developers/apps)
* (Optional) A Slack token for notifications, that can be generated at [Slack Integrations](https://ymedia-team.slack.com/apps/manage/custom-integrations)

### Installation

Detailed installation instructions can be found at [docs/installation.md](docs/installation.md)

### Running

Once you've completed steps outlined in the the [installation](docs/installation.md) instructions, the application can be started by running:

	$ python pimotion/main.py

### Example Capture
![pimotion-demo-capture](https://raw.githubusercontent.com/citrusbyte/pimotion/master/docs/pimotion-demo-capture.jpg)

### License

This project is delivered under the MIT license. See [LICENSE](LICENSE) for the terms.

### Attributions

Written by [Sarah Henkens](https://github.com/sarahhenkens), sponsored by [Citrusbyte](https://citrusbyte.com/)
