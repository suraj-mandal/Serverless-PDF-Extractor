variable "aws_region" {
  description = "AWS region to deploy the resources"
  default     = "ap-south-1"
}

variable "lambda_function_name" {
  description = "A unique name for the lambda function."
  default     = "PDF_Extractor"
}

