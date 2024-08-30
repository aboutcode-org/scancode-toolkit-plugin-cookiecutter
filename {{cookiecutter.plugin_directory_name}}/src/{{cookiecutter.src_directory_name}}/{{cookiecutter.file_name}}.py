#
# Copyright (c) nexB Inc. and others. All rights reserved.
# http://nexb.com and https://github.com/aboutcode-org/scancode-toolkit/
# The ScanCode software is licensed under the Apache License version 2.0.
# Data generated with ScanCode require an acknowledgment.
# ScanCode is a trademark of nexB Inc.
#
# You may not use this software except in compliance with the License.
# You may obtain a copy of the License at: http://apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software distributed
# under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
# CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.
#
# When you publish or redistribute any data created with ScanCode or any ScanCode
# derivative work, you must accompany this data with the following acknowledgment:
#
#  Generated with ScanCode and provided on an "AS IS" BASIS, WITHOUT WARRANTIES
#  OR CONDITIONS OF ANY KIND, either express or implied. No content created from
#  ScanCode should be considered or used as legal advice. Consult an Attorney
#  for any legal advice.
#  ScanCode is a free software code scanning tool from nexB Inc. and others.
#  Visit https://github.com/aboutcode-org/scancode-toolkit/ for support and download.

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from plugincode.{{cookiecutter.plugincode_filename}} import {{cookiecutter.scan_plugin}}
from plugincode.{{cookiecutter.plugincode_filename}} import {{cookiecutter.pluggy_impl}}
from scancode import CommandLineOption
from scancode import {{cookiecutter.SCAN_GROUP}}


@{{cookiecutter.pluggy_impl}}
class {{cookiecutter.class_name}}({{cookiecutter.scan_plugin}}):
    """
    Illustrate a simple "Hello World" post-scan plugin.
    """

    options = [
        CommandLineOption(('{{cookiecutter.commandline_option}}',),
                          is_flag=True, default=False,
                          help='Generate a simple "Hello ScanCode" greeting in the terminal.',
                          help_group={{cookiecutter.SCAN_GROUP}})
    ]

    def is_enabled(self, hello, **kwargs):
        return hello

    def process_codebase(self, codebase, hello, **kwargs):
        """
        Say hello.
        """
        if not self.is_enabled(hello):
            return

        print('\nHello {{cookiecutter.greeting_recipient}}!!\n')
