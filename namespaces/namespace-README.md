## Welcome to K8s namespace README
Viewing namespaces

1. List the current namespaces in a cluster using:

```kubectl get namespaces```

2. Creating a new namespace 
Create a new YAML file called my-namespace.yaml with the contents:

    ```apiVersion: v1
    kind: Namespace
    metadata:
      name: <insert-namespace-name-here>```
Then run:

   ``` kubectl create -f ./my-namespace.yaml```

Alternatively, you can create namespace using below command:

  ```  kubectl create namespace <insert-namespace-name-here>```
  
3. Deleting a namespace

Delete a namespace with

```kubectl delete namespaces <insert-some-namespace-name>```

For more information, refer to my article on [Medium](https://imoisharma.medium.com/namespaces-in-kubernetes-k8s-series-by-m-sharma-on-demand-part-2-65e455b846a0?source=your_stories_page-------------------------------------)
