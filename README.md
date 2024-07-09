# resmed-py
Python client for interacting with ResMed MyAir API

This is a "soft" fork of the embedded client in a [repo by](https://github.com/prestomation/resmed_myair_sensors/) @Prestomation. 

## Known Issues

This integration was reversed engineered from the myAir website. There are no guarentees that this will continue to work, as this is up to the whims of ResMed. Please DO NOT rely on this for any health-related matters.

This integration currently only connects to the Americas and Europe. If you are in Asia, please open an issue and offer yourself as a test subject.

_This integration does not work if you selected France as your country during myAir registration!_
In France, ResMed enforces two-factor email-based authentication which is not yet supported by the integration.

You may workaround this issue by:
1. Unregistering your device from your French myAir account
1. Register a new account in a European country that is not France
1. Register your device with your new account
1. Wait until your first night(and the myAir website shows your data) before creating a configuration for this integration



