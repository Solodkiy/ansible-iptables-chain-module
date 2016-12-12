# ansible-iptables-chain-module
Simple ansible module for create and delete (not yet) iptables chains

Create chain example
```yaml
- name: create chain
  iptables_chain:
    chain: CHAIN-NAME
  become: yes
```

Result:
```
Chain INPUT (policy ACCEPT)
target     prot opt source               destination         

Chain FORWARD (policy ACCEPT)
target     prot opt source               destination         

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination         

Chain CHAIN-NAME
target     prot opt source               destination 
```
