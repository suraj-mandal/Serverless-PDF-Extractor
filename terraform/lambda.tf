resource "aws_lambda_function" "pdf_extractor_lambda" {
  function_name    = var.lambda_function_name
  role             = aws_iam_role.lambda_role.arn
  handler          = "main.lambda_handler"
  runtime          = "python3.10"
  filename         = "lambda_function.zip"
  timeout          = 10

}
