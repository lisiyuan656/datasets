# coding=utf-8
# Copyright 2020 The TensorFlow Datasets Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests for tensorflow_datasets.core.utils.generic_path."""

import os
import pathlib
from unittest import mock

from tensorflow_datasets.core.utils import generic_path


def test_windows_encoding():
  # Is there a better way to test `WindowsPath` on linux than relying on
  # implementation internal ?
  with mock.patch('os.name', 'nt'), \
       mock.patch('pathlib.WindowsPath._flavour.is_supported', True), \
       mock.patch('io.open') as mocked_open:
    assert os.name == 'nt'

    path = generic_path.as_path('c:/Program Files/text.txt')
    assert isinstance(path, generic_path.Utf8WindowsPath)

    path = generic_path.as_path(pathlib.PosixPath('some_dir/abc'))
    assert isinstance(path, generic_path.Utf8WindowsPath)

    path.write_text('content')
    args, _ = mocked_open.call_args  # py3.8: use `call_args.args` instead
    assert args[3] == 'utf-8'  # io.open(file, mode, buffering, encoding, ...)
