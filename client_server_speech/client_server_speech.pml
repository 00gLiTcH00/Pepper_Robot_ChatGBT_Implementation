<?xml version="1.0" encoding="UTF-8" ?>
<Package name="client_server_speech" format_version="4">
    <Manifest src="manifest.xml" />
    <BehaviorDescriptions>
        <BehaviorDescription name="behavior" src="behavior_1" xar="behavior.xar" />
    </BehaviorDescriptions>
    <Dialogs>
        <Dialog name="ExampleDialog" src="behavior_1/ExampleDialog/ExampleDialog.dlg" />
        <Dialog name="topic" src="topic/topic.dlg" />
    </Dialogs>
    <Resources>
        <File name="server_speech" src="speech_server/server_speech.py" />
        <File name="client_test" src="speech_server/client_test.py" />
        <File name="choice_sentences" src="behavior_1/Aldebaran/choice_sentences.xml" />
    </Resources>
    <Topics>
        <Topic name="ExampleDialog_enu" src="behavior_1/ExampleDialog/ExampleDialog_enu.top" topicName="ExampleDialog" language="en_US" />
        <Topic name="topic_enu" src="topic/topic_enu.top" topicName="topic" language="en_US" />
    </Topics>
    <IgnoredPaths />
    <Translations auto-fill="en_US">
        <Translation name="translation_en_US" src="translations/translation_en_US.ts" language="en_US" />
    </Translations>
</Package>
