data "archive_file" "lambda" {
  type        = "zip"
  source_dir  = "${path.module}/package"
  output_path = "${path.module}/lambda_function.zip"
}

resource "aws_lambda_function" "pdf_extractor_lambda" {
  function_name    = var.lambda_function_name
  role             = aws_iam_role.lambda_role.arn
  handler          = "main.lambda_handler"
  runtime          = "python3.10"
  filename         = "lambda_function.zip"
  layers           = [aws_lambda_layer_version.poppler_layer.arn]
  timeout          = 300
  memory_size      = 1024
  source_code_hash = data.archive_file.lambda.output_base64sha256
  # depends_on    = [null_resource.install_dependencies]  # 👈 Ensure ZIP is created first
}