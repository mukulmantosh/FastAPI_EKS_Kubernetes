# Setting AWS Elastic Kubernetes Service (EKS) with FAST API

## Part 1

### 1. Publish Image in Amazon ECR

- Publish your Docker Image in a private repository. 

### 2. Create a New Cluster

```
eksctl create cluster -f eks/1/cluster.yml --auto-kubeconfig
```
It will take around 15-20 minutes to create a new cluster.


### 3. Checking Nodes

For checking the available nodes in the cluster, type the following command below along-with
the path of config file.

```
kubectl get nodes --kubeconfig=<PATH_TO_CONFIG_FILE>
```
For our tutorial, we will use:
```
kubectl get nodes --kubeconfig=/home/mukulmantosh/.kube/eksctl/clusters/fastapi-demo
```

### 3. Associate OIDC
To use IAM roles for service accounts, an IAM OIDC provider must exist for your cluster.

References:
* https://docs.aws.amazon.com/eks/latest/userguide/enable-iam-roles-for-service-accounts.html
* https://eksctl.io/usage/iamserviceaccounts/

```
eksctl utils associate-iam-oidc-provider --region <AWS_REGION> --cluster <CLUSTER_NAME> --approve
```
For our tutorial we will be using,

```
eksctl utils associate-iam-oidc-provider --region ap-south-1 --cluster fastapi-demo --approve
```
