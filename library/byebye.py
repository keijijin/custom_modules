#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule


def byebye():
    module_args = dict(
      name = dict( type='str', required=True),
      msg = dict( type='str', required=False)
    )

    module = AnsibleModule(
      argument_spec=module_args,
      supports_check_mode=True
      )

    result = dict(
       stdout_lines = '',
       changed = False,
       failed = False,
       stdout = ''
       )

    result['stdout_lines'] = "Bye bye " + module.params['name'] + ": " + module.params['msg']

    module.exit_json(**result)


def main():
  byebye()

if __name__ == '__main__':
    main()
