export CILIUM_POD=＄(kubectl get po -n istio-system -l k8s-app=cilium -o jsonpath='{.items[0].metadata.name}')
kubectl exec $CILIUM_POD -n kube-system -- cilium endpoint list