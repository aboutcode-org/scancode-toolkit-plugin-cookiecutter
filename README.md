# scancode-toolkit-plugin-cookiecutter

A [cookiecutter](https://github.com/cookiecutter/cookiecutter) post-scan plugin
for [scancode-toolkit](https://github.com/aboutcode-org/scancode-toolkit/) to
illustrate the creation of a simple post-scan plugin.

## Install Cookiecutter

Install cookiecutter into the Scancode-Toolkit virtualenv (created when scancode
was configured for the first time).

Navigate to the downloaded scancode-toolkit directory.

```
cd scancode-toolkit-3.1.1
./scancode --help
source bin/activate
```

Now, install cookiecutter (Version 1.6.0) via pip.

```
pip install cookiecutter==1.6.0
```

## Load Plugin with Scancode

Navigate to `scancode-toolkit/plugins/`, and download the cookiecutter plugin.

```
cd plugins/
cookiecutter https://github.com/aboutcode-org/scancode-toolkit-plugin-cookiecutter.git
```

Press ENTER for the following options to select the default option.

```
plugin_directory_name [scancode-cookiecutter-hello]:
src_directory_name [hello_scancode]:
file_name [hello_scancode]:
class_name [SayHello]:
entrypoint [scancode_post_scan]:
greeting_recipient [ScanCode User]:
commandline_option [--hello]:
plugincode_filename [post_scan]:
scan_plugin [PostScanPlugin]:
pluggy_impl [post_scan_impl]:
SCAN_GROUP [POST_SCAN_GROUP]:
```

To load and use the plugin in the normal course, navigate to the plugin’s root
folder and install via pip.

```
cd plugins/scancode-cookiecutter-hello/
pip install .
```

If you’re developing and want to test your work, save your edits and run
`pip install -e .` from the same folder.

## Documentation

`scancode-toolkit` : https://scancode-toolkit.readthedocs.io/ `cookiecutter` :
https://cookiecutter.readthedocs.io/
