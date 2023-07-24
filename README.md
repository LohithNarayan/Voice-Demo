# Voice-Demo
Creating a Company Custom Answering Rule
Be mindful of the following when constructing a request to create a user custom answering rule:

Provide a meaningful name for the rule using the name parameter.
Set the type parameter as "Custom."
Set the enabled parameter to True if the rule needs to be in effect immediately. Otherwise, set it to False.
Specify one or more conditions (see below).
Specify the action to take using the callHandlingAction field (see table below).
Specify the extension and greetings parameters. More details
Finally, make a POST request to the following endpoint:

/restapi/v1.0/account/{accountId}/extension/{extensionId}/answering-rule
