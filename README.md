# flask-lambda

A simple Terraform deployment of Flask using AWS Lambda.
```
git clone https://github.com/rei-nld/flask-lambda.git && cd flask-lambda
terraform init && terraform apply -y
```

# How to manually rebuild dependencies.zip (to be implemented in CI/CD)

x86_64:
```
rm -rf src/dependencies.zip && \
pip install \
--platform manylinux2014_x86_64 \
--target=src/dependencies \
--implementation cp \
--python-version 3.<version:number> \
--only-binary=:all: --upgrade \
<package:name> && \
zip -r src/dependencies.zip src/dependencies && rm -rf src/dependencies
```

ARM64:
```
rm -rf src/dependencies.zip && \
pip install \
--platform manylinux2014_aarch64 \
--target=src/dependencies \
--implementation cp \
--python-version 3.<version:number> \
--only-binary=:all: --upgrade \
<package:name> && \
zip -r src/dependencies.zip src/dependencies && rm -rf src/dependencies
```
