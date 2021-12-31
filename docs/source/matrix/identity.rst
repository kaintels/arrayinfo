**************
단위 행렬
**************

주대각성분은 모두 1이고 나머지 성분은 모두 0인 행렬을 만듭니다.

.. note::
    :class: sphx-glr-download-link-note

    Numpy는 **identity**, tensorflow 및 pytorch는 **eye** 인 점을 기억합시다.

**Numpy**

.. code-block:: python
   :linenos:

   import numpy as np
   np.identity()

**Tensorflow**

.. code-block:: python
   :linenos:

   import tensorflow as tf
   tf.eye()

**Pytorch**

.. code-block:: python
   :linenos:

   import torch
   torch.eye()
