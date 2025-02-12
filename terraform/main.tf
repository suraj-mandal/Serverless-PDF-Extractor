resource "aws_lambda_layer_version" "poppler_layer" {
  layer_name = "poppler_layer"
  filename   = "${path.module}/data/poppler.zip"
  compatible_architectures = ["x86_64", "arm64"]
  compatible_runtimes = ["python3.10"]
}