# Mimic Me!

Track faces in a video, identify facial expressions (using [Affectiva](http://www.affectiva.com/)’s Emotion-as-a-Service API), and tag each face with an appropriate emoji next to it. Then turn this into a game where the player needs to mimic a random emoji displayed by the computer!


- **mimic.js**: Javascript file with code that connects to the Affectiva API and processes results
- **index.html**: dynamic webpage that displays the video feed and results
- **mimic.css**: stylesheet file that defines the layout and presentation for HTML elements
- **serve.py**: a lightweight Python webserver required to serve the webpage over HTTPS, so that we can access the webcam feed
- **generate-pemfile.sh**: a shell script that need to run once to generate an SSL certificate for the webserver


## Affectiva Resources

- [Affectiva's JS SDK documentation](https://affectiva.readme.io/docs/getting-started-with-the-emotion-sdk-for-javascript)
- [Affectiva Developer portal](http://developer.affectiva.com/index.html)
- [Demo](https://jsfiddle.net/affectiva/opyh5e8d/show/) that this project is based on
- Tutorials: [Camera stream](https://affectiva.readme.io/docs/analyze-the-camera-stream-3), [video](https://affectiva.readme.io/docs/analyze-a-video-frame-stream-4), [photo](https://affectiva.readme.io/docs/analyze-a-photo-3)
