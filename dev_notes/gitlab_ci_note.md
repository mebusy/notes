
# gitlib CI notes

1. install & register a gitlab-runner ( shell executor )
    - https://docs.gitlab.com/ee/ci/docker/using_docker_build.html#use-the-shell-executor
2. on the host machine ( where gitlab-runner lives ),  keep git/docker update-to-date
3. create `.gitlab-ci.yml`  under your repo root 
    - https://docs.gitlab.com/ee/ci/yaml/
4. gitlab-runner execute script as user `gitlab-runner`
    - test your CI script as linux user -- gitlab-runner , on host machine to save life
    - `su gitlab-runner`



## Example .gitlab-ci.yml , build docker image & push 2 AWS ECR

```yaml
# need install & register a gitlab-runner ( shell executor ) !,  PS. keep the git ( on runner host ) version updated 
#   https://docs.gitlab.com/ee/ci/docker/using_docker_build.html#use-the-shell-executor
#   test your CI script by linux user -- gitlab-runner

variables:
  # CI_REGISTRY:   # in gitlab setting/CICD/Vaiables,  add these 3 CI_REGISTRY* variable
  # CI_REGISTRY_USER: 
  # CI_REGISTRY_PASSWORD: 
  IMAGE_NAME: "<your-image-name>_dev"   # TODO: replace dev to prod  on production branch
  IMAGE_TAG: "latest"
  DOCKERFILE_DIR: "image"
  K8S_SERVICE: "<your-k8s-deploy-name>"  # actually its your deployment name
  K8S_NAMESPACE: "<your-k8s-namespace>-dev"    # will be overrided depends on $IMAGE_NAME
  CI_REGISTRY_IMAGE: "$CI_REGISTRY/$IMAGE_NAME"  # will be overrided depends on $IMAGE_NAME


# CI_COMMIT_BRANCH  the branch name, not available on tag commit
# CI_COMMIT_TAG tag name  , not avaiable on branch commit
# CI_COMMIT_REF_NAME  branch OR tag name

# https://docs.gitlab.com/ee/ci/yaml/workflow.html
workflow: 
    rules:
      - if: $CI_COMMIT_BRANCH  # no branch !!!
        when: never 
      - if: $IMAGE_NAME =~ /prod$/  # check prod branch
        variables:
          K8S_NAMESPACE: "xxxxx-prod" # Override 
          CI_REGISTRY_IMAGE: "$CI_REGISTRY/$IMAGE_NAME"   # Override
      - if: $CI_COMMIT_TAG     # other image name case


stages:
  - build  # build image
  - upload  # upload image && update k8s pod

build-docker-image:
  stage: build
  script:
    - echo building... "$CI_REGISTRY_IMAGE:$IMAGE_TAG"
    - cd "$DOCKERFILE_DIR"
    - docker build -t "$CI_REGISTRY_IMAGE:$IMAGE_TAG"  .


upload-image:
  stage: upload
  script:
    - echo pushing... "$CI_REGISTRY_IMAGE:$IMAGE_TAG"
    - docker login --password $CI_REGISTRY_PASSWORD --username $CI_REGISTRY_USER $CI_REGISTRY
    - docker push "$CI_REGISTRY_IMAGE:$IMAGE_TAG"
    - echo "update deployment in namespace:" , $K8S_NAMESPACE
    # - whoami  # user is `gitlab-runner
    - NO_PROXY=amazonaws.com.cn KUBECONFIG="/home/gitlab-runner/gitlab-ci/k8s/k8s.conf" kubectl -n $K8S_NAMESPACE rollout restart deployment $K8S_SERVICE
```
