# Setting AWS Elastic Kubernetes Service (EKS) with FAST API

# https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/
# https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/#not-all-objects-are-in-a-namespace
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
the config file path.

```
kubectl get nodes --kubeconfig=<PATH_TO_CONFIG_FILE>
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

## Part 2

### 4. Installing ALB Ingress Controller

References:
* https://kubernetes-sigs.github.io/aws-load-balancer-controller/v2.2/



### 5. ClusterRole, ClusterRoleBinding & Service Account

```
kubectl apply -f eks/2/rbac-role.yml --kubeconfig=<PATH_TO_CONFIG_FILE>
```
or directly from repository master branch

```
kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/aws-alb-ingress-controller/master/docs/examples/rbac-role.yaml
```

### 6. List Service Account for ALB

```
kubectl describe sa alb-ingress-controller -n kube-system --kubeconfig=<PATH_TO_CONFIG_FILE>
```




### 6. Download IAM Policy

```
curl -o iam-policy.json https://raw.githubusercontent.com/kubernetes-sigs/aws-load-balancer-controller/v2.2.1/docs/install/iam_policy.json
```



### 7. Create an IAM policy called AWSLoadBalancerControllerIAMPolicy

Make sure you are inside the directory **eks/2**
```
aws iam create-policy \
    --policy-name AWSLoadBalancerControllerIAMPolicy \
    --policy-document file://iam-policy.json
```

or you can copy it from :

```
https://raw.githubusercontent.com/kubernetes-sigs/aws-alb-ingress-controller/master/docs/examples/iam-policy.json
```


### 8. Create an IAM role & attach it to the service account

```
eksctl create iamserviceaccount \
    --region <AWS_REGION> \
    --name alb-ingress-controller \
    --namespace kube-system \
    --cluster <CLUSTER_NAME> \
    --attach-policy-arn <POLICY_ARN> \
    --override-existing-serviceaccounts \
    --approve

```

For our tutorial, we will be using :

```
eksctl create iamserviceaccount \
    --region ap-south-1 \
    --name alb-ingress-controller \
    --namespace kube-system \
    --cluster fastapi-demo \
    --attach-policy-arn arn:aws:iam::254501641575:policy/AWSLoadBalancerControllerIAMPolicy \
    --override-existing-serviceaccounts \
    --approve

```

### 9. Verify IAM Service Account

```
eksctl get iamserviceaccount --cluster <CLUSTER_NAME>
```

### 10. Deploying Ingress Controller (ALB)

```
kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/aws-alb-ingress-controller/master/docs/examples/alb-ingress-controller.yaml --kubeconfig=<PATH_TO_CONFIG_FILE>

```

You can also verify:

```
kubectl get deploy -n kube-system --kubeconfig=<PATH_TO_CONFIG_FILE>
```


You need to update the deployment by adding the cluster name.

```
kubectl edit deployment alb-ingress-controller -n kube-system --kubeconfig=<PATH_TO_CONFIG_FILE>
```
with NANO Editor

```
KUBE_EDITOR="nano" kubectl edit deployment alb-ingress-controller -n kube-system --kubeconfig=fastapi-demo
```

Update the below line

```
    spec:
      containers:
      - args:
        - --ingress-class=alb
        - --cluster-name=fastapi-demo 

```

Verify Logs

```
kubectl logs -f alb-ingress-controller-65d6f7f9b5-w4jbd -n kube-system --kubeconfig=fastapi-demo
```



### 11. Subnet Discovery

https://aws.amazon.com/premiumsupport/knowledge-center/eks-vpc-subnet-discovery/



### 12. RDS

kubectl apply -f eks/deploy/rds/db-service.yml --kubeconfig=<PATH_TO_CONFIG_FILE>


