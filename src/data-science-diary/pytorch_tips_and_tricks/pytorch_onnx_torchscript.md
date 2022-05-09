# Red Herrings for PyTorch-ONNX-TorchScript Conversions

Once you create a model in PyTorch and train it, it's time to put it to use: typically known as *inferencing*. Typically, a regular PyTorch model would be mostly slow here. This is why the PyTorch model is generally converted into TorchScript or ONNX and run on OnnxRunTime (ORT) or if possible, on TensorRunTime (TRT) from Nvidia.

But there are several caveats to what can be converted from a PyTorch model into an ONNX or TorchScript model. ONNX models tend to be faster than TorchScript ones, in general [#citation](...).

## Things to Avoid

1. [Avoid NumPy and built-in Python types][_avoid_rule_1] 

   > PyTorch models can be written using NumPy or Python types and functions, but during tracing, any variables of NumPy or Python types (rather than torch.Tensor) are converted to constants, which will produce the wrong result if those values should change depending on the inputs.

   [_avoid_rule_1]: https://pytorch.org/docs/stable/onnx.html#avoid-numpy-and-built-in-python-types

2. [Avoid Tensor.data][_avoid_rule_2]
   
   > Use `torch.Tensor.detach()` instead of `torch.Tensor.data`.

   [_avoid_rule_2]: https://pytorch.org/docs/stable/onnx.html#avoid-tensor-data

3. [Avoid in-place operations when using `tensor.shape` in tracing mode][_avoid_rule_3]

   Do not use any of the following constructs.

   | **Avoid** :red_circle: | **Adopt** :green_circle: |
   |:---|:---|
   | x += 2 | x = x + 2 |
   | x *= 2 | x = x * 2 |
   | x /= 2 | x = x / 2 |

   [_avoid_rule_3]: https://pytorch.org/docs/stable/onnx.html#avoid-in-place-operations-when-using-tensor-shape-in-tracing-mode

## References

For more details, please see the following links.

- [Avoiding Pitfalls](https://pytorch.org/docs/stable/onnx.html#avoiding-pitfalls)
- [Limitations](https://pytorch.org/docs/stable/onnx.html#limitations)
