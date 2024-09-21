# flask-lambda

A simple Terraform deployment of Flask using AWS Lambda.
```
git clone https://github.com/rei-nld/flask-lambda.git && cd flask-lambda
terraform init && terraform apply -auto-approve
```

# How to manually rebuild **dependencies.zip** (to be implemented in CI/CD)

x86_64:
```
rm -rf src/dependencies.zip && \
pip install \
--platform manylinux2014_x86_64 \
--target=python \
--implementation cp \
--python-version 3.12 \
--only-binary=:all: --upgrade \
-r requirements.txt && \
zip -r src/dependencies.zip python && rm -rf python
```

ARM64:
```
rm -rf src/dependencies.zip && \
pip install \
--platform manylinux2014_aarch64 \
--target=python \
--implementation cp \
--python-version 3.12 \
--only-binary=:all: --upgrade \
-r requirements.txt && \
zip -r src/dependencies.zip python && rm -rf python
```
