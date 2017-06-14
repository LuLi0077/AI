# Alexa History Skill

Build a fully functional skill for [Amazon’s Alexa](https://developer.amazon.com/alexa) that provides year-dated facts from AI History use the [Alexa Skills Kit (ASK)](https://developer.amazon.com/alexa-skills-kit) - a current state of the art API for building voice systems.  

![Alexa skill process overview](images/skillOverview.png)


- **speechAssets/IntentSchema.json**  - intents definition for the interactive model
- **speechAssets/SampleUtterances_en_US.txt** - utterances for the interactive model
- **src/index.js** - skill logic and handlers to be run in AWS Lamda
- **src/facts.js** - a list of facts that the skill will use in responses
- **tests/*.js** - various unit tests to be run locally with mocha
