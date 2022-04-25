import logging

import tensorflow as tf

from . import dispatch, B
from ..types import TFDType, TFNumeric, Int, TFRandomState

__all__ = []

log = logging.getLogger(__name__)


@dispatch
def create_random_state(_: TFDType, seed: Int = 0):
    return tf.random.Generator.from_seed(seed)


@dispatch
def global_random_state(_: TFDType):
    return tf.random.get_global_generator()


@dispatch
def set_global_random_state(state: TFRandomState):
    tf.random.set_global_generator(state)


@dispatch
def rand(state: TFRandomState, dtype: TFDType, *shape: Int):
    return state, state.uniform(shape, dtype=dtype)


@dispatch
def rand(dtype: TFDType, *shape: Int):
    return rand(global_random_state(dtype), dtype, *shape)[1]


@dispatch
def randn(state: TFRandomState, dtype: TFDType, *shape: Int):
    return state, state.normal(shape, dtype=dtype)


@dispatch
def randn(dtype: TFDType, *shape: Int):
    return randn(global_random_state(dtype), dtype, *shape)[1]


@dispatch
def choice(state: TFRandomState, a: TFNumeric, n: Int):
    inds = state.uniform([n], minval=0, maxval=a.shape[0], dtype=tf.int64)
    choices = tf.gather(a, inds)
    return state, choices[0] if n == 1 else choices


@dispatch
def choice(a: TFNumeric, n: Int):
    return choice(global_random_state(a), a, n)[1]


@dispatch
def randint(
    state: TFRandomState,
    dtype: TFDType,
    *shape: Int,
    lower: Int = 0,
    upper: Int,
):
    dtype = B.dtype_int(dtype)
    return state, state.uniform(shape, lower, upper, dtype=dtype)


@dispatch
def randint(dtype: TFDType, *shape: Int, lower: Int = 0, upper: Int):
    state = global_random_state(dtype)
    return randint(state, dtype, *shape, lower=lower, upper=upper)[1]


@dispatch
def randperm(state: TFRandomState, dtype: TFDType, n: Int):
    dtype = B.dtype_int(dtype)
    # TF does not have a function to generate a random permutation. One way to do it
    # manually is to generate a range of length `n` and then shuffle it, but TF also
    # does not have a stateless shuffle. Hence, to get a stateless random permutation,
    # we generate random numbers and sort them...
    # TODO: Do this in a better way.
    perm = tf.argsort(state.uniform((n,), dtype=tf.float32))
    return state, B.cast(dtype, perm)


@dispatch
def randperm(dtype: TFDType, n: Int):
    return randperm(global_random_state(dtype), dtype, n)[1]
