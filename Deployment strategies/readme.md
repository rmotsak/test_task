To switch from blue to green, update the Deployment for the green version and scale it up to the desired number of replicas.

```
kubectl apply -f green-app-deployment.yaml
kubectl scale deployment green-app --replicas=3
```
Update the Service to select the green version of the application.
```
kubectl patch service app-service -p '{"spec": {"selector": {"app": "green-app"}}}'
```
Scale down the blue Deployment and delete it.
```
kubectl scale deployment blue-app --replicas=0
kubectl delete deployment blue-app
```
