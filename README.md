<h1>Trompa Contributor Environment Python Client</h1>

<!-- <h2>Pritish Chandna, Merlijn Blaauw, Jordi Bonada, Emilia Gómez</h2> -->

<h2>Music Technology Group, Universitat Pompeu Fabra, Barcelona</h2>

A python library to read from and write to the Trompa CE
<h3>Installation</h3>
To install, run <pre><code>setup.py</code></pre> to install the packages required.


<h2>Application Side Functionality</h2>
<h3>Creating an application</h3>
1) Set up the configurations for the application in the .ini file, an example is present in app_config.ini.
2) Run application_create.py


<h3>Creating an entry point and linking to the application</h3>
1) Set up the configurations for the entrypoint, control action and properties and property values in the .ini file, an example is present in ep_config.ini.
2) Run entrypoint_create.py

<h3>Subscribe to an entry point</h3>
3) Run entrypoint_subscribe.py

<h2>Client Side Functionality</h2>

<h3>Get all applications, entry points, control actions</h3>
1) Run client_get_control.py. This will create configuration files to be set up for each of the applications in the CE. The values in the configuration files need to be set up before sending an action request. 

<h3>Request an action</h3>
1) Set up the values in the config file for the entry point to be requested. 
2) Run client_send_request.py.
3) The script will send a request every second to the CE to get the status of the requested action, till completed or an error is encountered. 