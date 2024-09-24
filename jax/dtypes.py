# Copyright 2019 The JAX Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Note: import <name> as <name> is required for names to be exported.
# See PEP 484 & https://github.com/jax-ml/jax/issues/7570

from jax._src.dtypes import (
    bfloat16 as bfloat16,
    canonicalize_dtype as canonicalize_dtype,
    finfo,  # TODO(phawkins): switch callers to jnp.finfo?
    float0 as float0,
    iinfo,  # TODO(phawkins): switch callers to jnp.iinfo?
    issubdtype,  # TODO(phawkins): switch callers to jnp.issubdtype?
    extended as extended,
    prng_key as prng_key,
    result_type as result_type,
    scalar_type_of as scalar_type_of,
)
