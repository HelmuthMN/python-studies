from users import Admin

root = Admin('root', 'root', 0, 'secret', 'secret')
root.privileges.show_privileges()