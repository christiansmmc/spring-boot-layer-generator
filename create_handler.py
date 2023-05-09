import os


def create_input(message):
    return input(f'\n{message} ').lower()


def create_repository(entity_name: str, package_prefix: str, path: str) -> None:
    java_code = f'package {package_prefix}.repository;\n' \
                f'\n' \
                f'import {package_prefix}.domain.{entity_name};\n' \
                f'import org.springframework.data.jpa.repository.JpaRepository;\n' \
                f'import org.springframework.stereotype.Repository;\n' \
                f'\n' \
                f'@Repository\n' \
                f'public interface {entity_name}Repository extends JpaRepository<{entity_name}, Long> {{\n' \
                f'}}\n'

    file_path = f'{path}/repository/{entity_name}Repository.java'
    create_file(file_path, java_code)
    print('Repository Created!')


def create_service(entity_name: str, package_prefix: str, path: str) -> None:
    service_java_code = f'package {package_prefix}.service;\n' \
                        f'\n' \
                        f'public interface {entity_name}Service {{\n' \
                        f'}}\n'

    service_impl_java_code = f'package {package_prefix}.service.impl;\n' \
                             f'\n' \
                             f'import {package_prefix}.service.{entity_name}Service;\n' \
                             f'import lombok.AllArgsConstructor;\n' \
                             f'import org.springframework.stereotype.Service;\n' \
                             f'\n' \
                             f'@Service\n' \
                             f'@AllArgsConstructor\n' \
                             f'public class {entity_name}ServiceImpl implements {entity_name}Service {{\n' \
                             f'}}\n'

    service_file_path = f'{path}/service/{entity_name}Service.java'
    create_file(service_file_path, service_java_code)
    print('Service Created!')

    service_impl_file_path = f'{path}/service/impl/{entity_name}ServiceImpl.java'
    create_file(service_impl_file_path, service_impl_java_code)
    print('ServiceImpl Created!')


def create_context(entity_name: str, package_prefix: str, path: str) -> None:
    context_java_code = f'package {package_prefix}.context;\n' \
                        f'\n' \
                        f'public interface {entity_name}Context {{\n' \
                        f'}}\n'

    context_impl_java_code = f'package {package_prefix}.context.impl;\n' \
                             f'\n' \
                             f'import {package_prefix}.context.{entity_name}Context;\n' \
                             f'import lombok.AllArgsConstructor;\n' \
                             f'import org.springframework.stereotype.Service;\n' \
                             f'\n' \
                             f'@Service\n' \
                             f'@AllArgsConstructor\n' \
                             f'public class {entity_name}ContextImpl implements {entity_name}Context {{\n' \
                             f'}}\n'

    context_file_path = f'{path}/context/{entity_name}Context.java'
    create_file(context_file_path, context_java_code)
    print('Context Created!')

    context_impl_file_path = f'{path}/context/impl/{entity_name}ContextImpl.java'
    create_file(context_impl_file_path, context_impl_java_code)
    print('ContextImpl Created!')


def create_facade(entity_name: str, package_prefix: str, path: str) -> None:
    dto_java_code = f'package {package_prefix}.facade.dto.{entity_name.lower()};\n' \
                    f'\n' \
                    f'import lombok.AllArgsConstructor;\n' \
                    f'import lombok.Builder;\n' \
                    f'import lombok.Data;\n' \
                    f'import lombok.NoArgsConstructor;\n' \
                    f'import java.io.Serializable;\n' \
                    f'\n' \
                    f'@Data\n' \
                    f'@Builder\n' \
                    f'@NoArgsConstructor\n' \
                    f'@AllArgsConstructor\n' \
                    f'public class {entity_name}DTO implements Serializable {{\n' \
                    f'}}\n'

    mapper_java_code = f'package {package_prefix}.facade.mapper;\n' \
                       f'\n' \
                       f'import {package_prefix}.domain.{entity_name};\n' \
                       f'import {package_prefix}.facade.dto.{entity_name.lower()}.{entity_name}DTO;\n' \
                       f'import org.mapstruct.Mapper;\n' \
                       f'import org.mapstruct.ReportingPolicy;\n' \
                       f'\n' \
                       f'@Mapper(componentModel = "spring", uses = {{}}, unmappedTargetPolicy = ReportingPolicy.IGNORE)\n' \
                       f'public interface {entity_name}Mapper extends EntityMapper<{entity_name}DTO, {entity_name}> {{\n' \
                       f'}}\n'

    facade_java_code = f'package {package_prefix}.facade;\n' \
                       f'\n' \
                       f'import org.springframework.stereotype.Service;\n' \
                       f'import lombok.AllArgsConstructor;\n' \
                       f'import {package_prefix}.facade.mapper.{entity_name}Mapper;\n' \
                       f'import {package_prefix}.service.{entity_name}Service;\n' \
                       f'\n' \
                       f'@Service\n' \
                       f'@AllArgsConstructor\n' \
                       f'public class {entity_name}Facade {{\n' \
                       f'\n' \
                       f'    private final {entity_name}Mapper mapper;\n' \
                       f'    private final {entity_name}Service service;\n' \
                       f'}}\n'

    dto_file_path = f'{path}/facade/dto/{entity_name.lower()}/{entity_name}DTO.java'
    create_file(dto_file_path, dto_java_code)
    print('DTO created!')

    mapper_file_path = f'{path}/facade/mapper/{entity_name}Mapper.java'
    create_file(mapper_file_path, mapper_java_code)
    print('Mapper created!')

    facade_file_path = f'{path}/facade/{entity_name}Facade.java'
    create_file(facade_file_path, facade_java_code)
    print('Facade Created!')


def create_controller(entity_name: str, package_prefix: str, path: str) -> None:
    java_code = f'package {package_prefix}.controller;\n' \
                f'\n' \
                f'import {package_prefix}.facade.{entity_name}Facade;' \
                f'import lombok.AllArgsConstructor;' \
                f'import lombok.extern.slf4j.Slf4j;' \
                f'import org.springframework.web.bind.annotation.RequestMapping;' \
                f'import org.springframework.web.bind.annotation.RestController;' \
                f'\n' \
                f'@RestController\n' \
                f'@RequestMapping("/api")\n' \
                f'@AllArgsConstructor\n' \
                f'@Slf4j\n' \
                f'public class {entity_name}Controller {{\n' \
                f'\n' \
                f'    private final {entity_name}Facade facade;\n' \
                f'}}\n'

    file_path = f'{path}/controller/{entity_name}Controller.java'
    create_file(file_path, java_code)
    print('Controller Created!')


def create_resource(entity_name: str, package_prefix: str, path: str) -> None:
    java_code = f'package {package_prefix}.web.rest;\n' \
                f'\n' \
                f'import {package_prefix}.facade.{entity_name}Facade;' \
                f'import lombok.AllArgsConstructor;' \
                f'import lombok.extern.slf4j.Slf4j;' \
                f'import org.springframework.web.bind.annotation.RequestMapping;' \
                f'import org.springframework.web.bind.annotation.RestController;' \
                f'\n' \
                f'@RestController\n' \
                f'@RequestMapping("/api")\n' \
                f'@AllArgsConstructor\n' \
                f'@Slf4j\n' \
                f'public class {entity_name}Resource {{\n' \
                f'\n' \
                f'    private final {entity_name}Facade facade;\n' \
                f'}}\n'

    file_path = f'{path}/web/rest/{entity_name}Resource.java'
    create_file(file_path, java_code)
    print('Resource Created!')


def create_file(file_path: str, java_code: str) -> None:
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w") as file:
        file.write(java_code)
