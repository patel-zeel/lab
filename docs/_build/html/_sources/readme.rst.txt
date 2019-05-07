`LAB <http://github.com/wesselb/lab>`__
=======================================

|Build| |Coverage Status| |Latest Docs|

A generic interface for linear algebra backends: code it once, run it on
any backend

-  `Installation <#installation>`__
-  `Basic Usage <#basic-usage>`__
-  `List of Types <#list-of-types>`__

   -  `General <#general>`__
   -  `NumPy <#numpy>`__
   -  `TensorFlow <#tensorflow>`__
   -  `PyTorch <#pytorch>`__

-  `List of Methods <#list-of-methods>`__

   -  `Constants <#constants>`__
   -  `Generic <#generic>`__
   -  `Linear Algebra <#linear-algebra>`__
   -  `Random <#random>`__
   -  `Shaping <#shaping>`__

Installation
------------

The package is tested for Python 2.7 and Python 3.6, which are the
versions recommended to use. To install the package, use the following
sequence of commands:

::

    git clone https://github.com/wesselb/lab
    cd lab
    make install

Basic Usage
-----------

The basic use case for the package is to write code that automatically
determines the backend to use depending on the types of its arguments.

Example:

.. code:: python

    import lab as B

    def objective(matrix):
        outer_product = B.matmul(matrix, matrix, tr_b=True)
        return B.mean(outer_product)

Run it with NumPy and AutoGrad:

.. code:: python

    >>> import autograd.numpy as np

    >>> from autograd import grad

    >>> grad(objective)(B.randn((2, 2), np.float64))
    array([[-0.35247881, -0.4144402 ],
           [-0.35247881, -0.4144402 ]])

Run it with TensorFlow:

.. code:: python

    >>> import tensorflow as tf

    >>> objective(B.randn((2, 2), tf.float64))
    <tf.Tensor 'Mean:0' shape=() dtype=float64>

Run it with PyTorch:

.. code:: python

    >>> import torch

    >>> objective(B.randn((2, 2), torch.float64))
    tensor(1.9557, dtype=torch.float64)

List of Types
-------------

This section lists all available types, which can be used to check types
of objects or extend functions.

Example:

.. code:: python

    >>> import lab as B

    >>> import numpy as np

    >>> isinstance([1., np.array([1., 2.])], B.NPList)
    True

    >>> isinstance([1., np.array([1., 2.])], B.TFList)
    False

    >>> import tensorflow as tf

    >>> isinstance((tf.constant(1.), tf.ones(5)), B.TFTuple)
    True

General
~~~~~~~

::

    Int          # Integers
    Float        # Floating-point numbers
    Bool         # Booleans
    Number       # Numbers
    Numeric      # Numerical objects, including booleans
    ListOrTuple  # Lists or tuples
    Shape        # Shapes
    DType        # Data typse
    Framework    # Anything accepted by supported frameworks

NumPy
~~~~~

::

    NPNumeric
    NPList
    NPTuple
    NPList
    NPListOrTuple
    NPShape
    NPDType
     
    NP             # Anything NumPy

TensorFlow
~~~~~~~~~~

::

    TFNumeric
    TFList
    TFTuple
    TFList
    TFListOrTuple
    TFShape
    TFDType
     
    TF             # Anything TensorFlow

PyTorch
~~~~~~~

::

    TorchNumeric
    TorchList
    TorchTuple
    TorchList
    TorchListOrTuple
    TorchShape
    TorchDType
     
    Torch             # Anything PyTorch

List of Methods
---------------

This section lists all available constants and methods.

-  Arguments *must* be given as arguments and keyword arguments *must*
   be given as keyword arguments. For example, ``zeros((2, 2))`` is
   valid, but ``zeros(shape=(2, 2))`` is not; and
   ``sum(tensor, axis=1)`` is valid, but ``sum(tensor, 1)`` is not.

-  The names of arguments are indicative of their function:

   -  ``a``, ``b``, and ``c`` indicate general tensors.
   -  ``dtype`` indicates a data type. E.g, ``np.float32`` or
      ``tf.float64``, and ``rand(np.float32)`` creates a NumPy random
      number, whereas ``rand(tf.float64)`` creates a TensorFlow random
      number.
   -  ``shape`` indicates a shape. E.g., ``(2, 2)`` or ``[2, 2]``.
   -  ``axis`` indicates an axis over which the function may perform its
      action.
   -  ``ref`` indicates a *reference tensor* from which a property (like
      its data type) will be inferred. E.g., ``zeros(tensor)`` creates a
      tensor full or zeros of the same shape and data type as
      ``tensor``.

See the documentation for more detailled descriptions of each function.

Constants
~~~~~~~~~

::

    nan
    pi
    log_2_pi

    isnan(a)

Generic
~~~~~~~

::

    zeros(shape, dtype)
    zeros(shape)
    zeros(shape, ref)
    zeros(ref, dtype)
    zeros(ref)

    ones(shape, dtype)
    ones(shape)
    ones(shape, ref)
    ones(ref, dtype)
    ones(ref)

    eye(shape, dtype)
    eye(shape)
    eye(shape, ref)
    eye(ref, dtype)
    eye(ref)

    linspace(a, b, num)

    cast(a, dtype)
    cast(a, ref)

    identity(a)
    abs(a)
    sign(a)
    sqrt(a)
    exp(a)
    log(a)
    sin(a)
    cos(a)
    tan(a)
    sigmoid(a)
    relu(a)

    add(a, b)
    subtract(a, b)
    multiply(a, b)
    divide(a, b)
    power(a, b)
    minimum(a, b)
    maximum(a, b)
    leaky_relu(a, alpha)

    min(a, axis=None)
    max(a, axis=None)
    sum(a, axis=None)
    mean(a, axis=None)
    std(a, axis=None)
    logsumexp(a, axis=None)

    all(a, axis=None)
    any(a, axis=None)

    lt(a, b)
    le(a, b)
    gt(a, b)
    ge(a, b)

Linear Algebra
~~~~~~~~~~~~~~

::

    transpose(a, perm=None) (alias: T)
    matmul(a, b, tr_a=False, tr_b=False) (alias: mm, dot)
    trace(a, axis1=0, axis2=1)
    kron(a, b)
    svd(a, compute_uv=True)
    cholesky(a)
    cholesky_solve(a, b)
    trisolve(a, b, lower_a=True)
    outer(a, b)
    reg(a, diag=None, clip=True)

    pw_dists2(a, b)
    pw_dists2(a)
    pw_dists(a, b)
    pw_dists(a)

    ew_dists2(a, b)
    ew_dists2(a)
    ew_dists(a, b)
    ew_dists(a)

    pw_sums2(a, b)
    pw_sums2(a)
    pw_sums(a, b)
    pw_sums(a)

    ew_sums2(a, b)
    ew_sums2(a)
    ew_sums(a, b)
    ew_sums(a)

Random
~~~~~~

::

    set_random_seed(seed) 

    rand(shape, dtype)
    rand(shape)
    rand(dtype)
    rand()

    randn(shape, dtype)
    randn(shape)
    randn(dtype)
    randn()

Shaping
~~~~~~~

::

    shape(a)
    shape_int(a)
    rank(a)
    length(a)
    isscalar(a)
    expand_dims(a, axis=0)
    squeeze(a)
    uprank(a)

    diag(a)
    flatten(a)
    vec_to_tril(a)
    tril_to_vec(a)
    stack(a, axis=0)
    unstack(a, axis=0)
    reshape(a, shape=(-1,))
    concat(a, axis=0)
    concat2d(a)
    take(a, indices, axis=0)

.. |Build| image:: https://travis-ci.org/wesselb/lab.svg?branch=master
   :target: https://travis-ci.org/wesselb/lab
.. |Coverage Status| image:: https://coveralls.io/repos/github/wesselb/lab/badge.svg?branch=master&service=github
   :target: https://coveralls.io/github/wesselb/lab?branch=master
.. |Latest Docs| image:: https://img.shields.io/badge/docs-latest-blue.svg
   :target: https://wesselb.github.io/lab
