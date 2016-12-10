#!/usr/bin/python

from ansible.module_utils.basic import *


def chain_present(data):  
    chain = data["chain"]

    return_code = os.system("iptables -n --list "+chain)
    has_changed = False
    if return_code != 0:
        os.system("iptables -N "+chain)
        has_changed = True

    return (has_changed, {})

def chain_absent(data=None):  
    has_changed = False
    meta = {"absent": "not yet implemented"}

def main():
    fields = {
        "chain":  {"required": True, "type": "str"},
         "state": {
            "default": "present", 
            "choices": ['present', 'absent'],  
            "type": 'str' 
        },
    }
    module = AnsibleModule(argument_spec=fields)
    choice_map = {
        "present": chain_present,
        "absent": chain_absent, 
    }
    has_changed, result = choice_map.get(module.params['state'])(module.params)
    module.exit_json(changed=has_changed, meta=result)


if __name__ == '__main__':
    main()

