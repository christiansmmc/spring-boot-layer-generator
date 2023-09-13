import os.path

from create_handler import *

VALID_LAYERS = ['REPOSITORY', 'SERVICE', 'FACADE', 'CONTROLLER', 'RESOURCE', 'CONTEXT']


def is_list_valid(list_to_validate: list[str]) -> bool:
    for item in list_to_validate:
        if item.upper() not in VALID_LAYERS:
            return False
    return True


def main() -> None:
    path = "../" + create_input('Where are the layers on ?\n'
                        '* Example: src/main/java/com/tealpanda\n'
                        ' - ')

    if not os.path.isdir(path):
        print('Not a valid path')
        return

    entity_name = input('\nWhat is the name of the entity ? (Case sensitive)\n'
                        '* Example: User\n'
                        ' - ')

    is_default_layers = create_input('Are you using default layers (y/n) ?\n'
                                     '[Controller - Facade - Service - Repository]\n'
                                     ' - ')

    if is_default_layers == 'n':
        layers_to_create = create_input('Which layers do you want to create ?\n'
                                        '[options: Resource - Controller - Facade - Context - Service - Repository]\n'
                                        '* Send separated by space\n'
                                        '* Example: resource facade service repository\n'
                                        ' - \n')

        if not is_list_valid(layers_to_create.split(' ')):
            print('Layer not valid')
            return

    else:
        layers_to_create = 'controller facade service repository'

    layers_to_create = layers_to_create.split(' ')
    package_prefix = path.split("java/")[1].replace('/', '.')

    for layer in layers_to_create:
        if layer == 'repository':
            create_repository(entity_name, package_prefix, path)
        if layer == 'service':
            create_service(entity_name, package_prefix, path)
        if layer == 'facade':
            create_facade(entity_name, package_prefix, path)
        if layer == 'controller':
            create_controller(entity_name, package_prefix, path)
        if layer == 'resource':
            create_resource(entity_name, package_prefix, path)
        if layer == 'context':
            create_context(entity_name, package_prefix, path)

    print('\nCreation successful!')


if __name__ == '__main__':
    main()
