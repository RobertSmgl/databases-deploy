terraform {
  required_providers {
    yandex = {
      source  = "yandex-cloud/yandex"
      # version = "~> 0.107.0"
    }
  }
  required_version = ">= 1.3"
}

variable "IAM_TOKEN" {
  type = string
}

variable "YC_CLOUD_ID" {
  type = string
}

variable "YC_FOLDER_ID" {
  type = string
}

variable "PASSWORD" {
  type = string
}


provider "yandex" {
  token                    = "${var.IAM_TOKEN}"
  cloud_id                 = "${var.YC_CLOUD_ID}"
  folder_id                = "${var.YC_FOLDER_ID}"
  zone                     = "ru-central1-a"
}