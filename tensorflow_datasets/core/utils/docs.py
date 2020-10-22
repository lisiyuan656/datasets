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

"""Documentation utils."""

from tensorflow.tools.docs import doc_controls  # pylint: disable=g-direct-tensorflow-import


def _no_op_decorator(obj):
  return obj


set_deprecated = doc_controls.set_deprecated
do_not_doc = doc_controls.do_not_generate_docs
# Same as `do_not_doc`, but also applied to childs
do_not_doc_inheritable = doc_controls.do_not_doc_inheritable
# Document the parent, but not the childs
do_not_doc_in_subclasses = doc_controls.do_not_doc_in_subclasses

if hasattr(doc_controls, 'doc_private'):
  doc_private = doc_controls.doc_private
else:
  doc_private = _no_op_decorator
