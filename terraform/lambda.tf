resource "null_resource" "install_dependencies" {
  provisioner "local-exec" {
    command = <<EOT
      rm -rf ../package && mkdir ../package
      pip install -r ../requirements.txt -t ../package
      cp -r ../lambda/* ../package/
      cd ../package && zip -r ../lambda_function.zip .
    EOT
  }

  triggers = {
    always_run = timestamp()
  }
}

resource "aws_lambda_function" "pdf_extractor_lambda" {
  function_name = var.lambda_function_name
  role          = aws_iam_role.lambda_role.arn
  handler       = "main.lambda_handler"
  runtime       = "python3.10"
  filename      = "../lambda_function.zip"
  layers        = [aws_lambda_layer_version.poppler_layer.arn]
  timeout       = 300
  depends_on    = [null_resource.install_dependencies]  # 👈 Ensure ZIP is created first
}