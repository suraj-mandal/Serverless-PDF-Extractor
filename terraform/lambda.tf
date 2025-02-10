resource "null_resource" "install_dependencies" {
  provisioner "local-exec" {
    command = <<EOT
      rm -rf package && mkdir package
      pip install -r lambda/requirements.txt -t package
      cp -r lambda/* package/
      cd package && zip -r ../lambda_function.zip .
    EOT
  }

  triggers = {
    always_run = timestamp()
  }
}

resource "aws_lambda_function" "my_lambda" {
  function_name    = var.lambda_function_name
  role             = aws_iam_role.lambda_role.arn
  handler          = "lambda_function.lambda_handler"
  runtime          = "python3.10"
  filename         = "lambda_function.zip"
  source_code_hash = filebase64sha256("../lambda_function.zip")
  timeout          = 10

  depends_on = [null_resource.install_dependencies]  # 👈 Ensure ZIP is created first
}
