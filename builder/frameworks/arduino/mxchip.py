# Copyright 2014-present PlatformIO <contact@platformio.org>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Arduino

Arduino Wiring-based Framework allows writing cross-platform software to
control devices attached to a wide range of Arduino boards to create all
kinds of creative coding, interactive objects, spaces or physical experiences.

http://www.stm32duino.com
"""

from os import walk
from os.path import isdir, join
from typing import Dict, AnyStr, Any

from SCons.Script import DefaultEnvironment

env = DefaultEnvironment()
platform = env.PioPlatform()
board = env.BoardConfig()

FRAMEWORK_DIR = platform.get_package_dir("framework-arduinostm32mxchip")
FRAMEWORK_VERSION = platform.get_package_version(
    "framework-arduinostm32mxchip")
assert isdir(FRAMEWORK_DIR)

env.SConscript("../_bare.py")

COMPILE_OPTS = dict(
    ASFLAGS=['-c', '-x', 'assembler-with-cpp', '-I{build_system_path}', '-I{build_system_path}/mbed-os', '-I{build_system_path}/mbed-os/cmsis', '-I{build_system_path}/mbed-os/drivers', '-I{build_system_path}/mbed-os/events', '-I{build_system_path}/mbed-os/events/equeue', '-I{build_system_path}/mbed-os/features', '-I{build_system_path}/mbed-os/features/filesystem', '-I{build_system_path}/mbed-os/features/filesystem/bd', '-I{build_system_path}/mbed-os/features/filesystem/fat', '-I{build_system_path}/mbed-os/features/filesystem/fat/ChaN', '-I{build_system_path}/mbed-os/features/frameworks/greentea-client/greentea-client', '-I{build_system_path}/mbed-os/features/frameworks/unity/unity', '-I{build_system_path}/mbed-os/features/mbedtls/inc', '-I{build_system_path}/mbed-os/features/mbedtls', '-I{build_system_path}/mbed-os/features/netsocket', '-I{build_system_path}/mbed-os/hal', '-I{build_system_path}/mbed-os/hal/storage_abstraction', '-I{build_system_path}/mbed-os/platform', '-I{build_system_path}/mbed-os/rtos', '-I{build_system_path}/mbed-os/rtos/rtx/TARGET_CORTEX_M', '-I{build_system_path}/mbed-os/targets/TARGET_MXCHIP', '-I{build_system_path}/mbed-os/targets/TARGET_MXCHIP/TARGET_AZ3166', '-I{build_system_path}/mbed-os/targets/TARGET_MXCHIP/TARGET_AZ3166/device', '-I{build_system_path}/mbed-os/targets/TARGET_STM', '-I{build_system_path}/mbed-os/targets/TARGET_STM/TARGET_STM32F4', '-I{build_system_path}/mbed-os/targets/TARGET_STM/TARGET_STM32F4/device', '-I{build_system_path}/az3166-driver', '-I{build_system_path}/az3166-driver/libraries/drivers/display/VGM128064', '-I{build_system_path}/az3166-driver/libraries/drivers/gpio_btn', '-I{build_system_path}/az3166-driver/libraries/drivers/spi_flash', '-I{build_system_path}/az3166-driver/libraries/utilities', '-I{build_system_path}/az3166-driver/mico', '-I{build_system_path}/az3166-driver/mico/include', '-I{build_system_path}/az3166-driver/mico/include/mico_drivers', '-I{build_system_path}/az3166-driver/mico/net/LwIP/lwip-sys', '-I{build_system_path}/az3166-driver/mico/net/LwIP/lwip-sys/arch', '-I{build_system_path}/az3166-driver/mico/net/LwIP/lwip-ver1.4.0.rc1/src/include', '-I{build_system_path}/az3166-driver/mico/net/LwIP/lwip-ver1.4.0.rc1/src/include/lwip', '-I{build_system_path}/az3166-driver/mico/net/LwIP/lwip-ver1.4.0.rc1/src/include/ipv4', '-I{build_system_path}/az3166-driver/mico/platform', '-I{build_system_path}/az3166-driver/mico/platform/include', '-I{build_system_path}/az3166-driver/mico/platform/mbed', '-I{build_system_path}/az3166-driver/mico/rtos', '-I{build_system_path}/az3166-driver/mico/system', '-I{build_system_path}/az3166-driver/mico/system/command_console', '-I{build_system_path}/az3166-driver/TARGET_AZ3166', '-I{build_system_path}/az3166-driver/TARGET_STM/peripherals', '-I{build_system_path}/az3166-driver/utilities', '-I{build_system_path}/azure-iot-sdk-c/', '-I{build_system_path}/azure-iot-sdk-c/c-utility/inc', '-I{build_system_path}/azure-iot-sdk-c/c-utility/pal/mbed_os5', '-I{build_system_path}/azure-iot-sdk-c/deps/parson', '-I{build_system_path}/azure-iot-sdk-c/deps/uhttp/inc', '-I{build_system_path}/azure-iot-sdk-c/deps/umock-c/inc', '-I{build_system_path}/azure-iot-sdk-c/deps/azure-macro-utils-c/inc', '-I{build_system_path}/azure-iot-sdk-c/iothub_client/inc', '-I{build_system_path}/azure-iot-sdk-c/iothub_client/inc/internal', '-I{build_system_path}/azure-iot-sdk-c/digitaltwin_client/inc', '-I{build_system_path}/azure-iot-sdk-c/digitaltwin_client/inc/internal', '-I{build_system_path}/azure-iot-sdk-c/provisioning_client/inc', '-I{build_system_path}/azure-iot-sdk-c/provisioning_client/adapters', '-I{build_system_path}/azure-iot-sdk-c/provisioning_client/deps/RIoT/Reference/DICE', '-I{build_system_path}/azure-iot-sdk-c/provisioning_client/deps/RIoT/Reference/RIoT', '-I{build_system_path}/azure-iot-sdk-c/provisioning_client/deps/RIoT/Reference/RIoT/Core/', '-I{build_system_path}/azure-iot-sdk-c/provisioning_client/deps/RIoT/Reference/RIoT/Core/RIoTCrypt/include', '-I{build_system_path}/azure-iot-sdk-c/umqtt/inc', '-I{build_core_path}', '-I{build_core_path}/cli', '-I{build_core_path}/httpclient', '-I{build_core_path}/httpclient/http_parser', '-I{build_core_path}/httpserver', '-I{build_core_path}/NTPClient', '-I{build_core_path}/system', '-I{build_core_path}/Telemetry', '-DTRANSACTION_QUEUE_SIZE_SPI=2', '-D__CORTEX_M4', '-DUSB_STM_HAL', '-DARM_MATH_CM4', '-D__FPU_PRESENT=1', '-DUSBHOST_OTHER', '-D__MBED_CMSIS_RTOS_CM', '-D__CMSIS_RTOS', '-mcpu={build_mcu}', '-DARDUINO={runtime_ide_version}', '-DARDUINO_{build_board}', '-DARDUINO_ARCH_{build_arch}'],
    CFLAGS=['-std=gnu99'],
    CCFLAGS=['-c', '-O2', '-g', '-w', '-ffunction-sections', '-fdata-sections', '-nostdlib', '--param', 'max-inline-insns-single=500', '-include', 'mbed_config.h', '-MMD', '-mcpu={build_mcu}'],
    CXXFLAGS=['-std=gnu++11', '-Wno-unused-parameter', '-Wno-missing-field-initializers', '-fmessage-length=0', '-fno-threadsafe-statics', '-fno-rtti', '-Wvla'],
    CPPDEFINES=[('DEVICE_RTC', '1'), ('MXCHIP_LIBRARY', None), ('__CORTEX_M4', None), ('DEVICE_SERIAL_FC', '1'), ('LPS22HB_I2C_PORT', 'MICO_I2C_1'), ('DEVICE_I2C_ASYNCH', '1'), ('DEVICE_PORTINOUT', '1'), ('DEVICE_SLEEP', '1'), ('TARGET_FF_MORPHO', None), ('TOOLCHAIN_GCC', None), ('TARGET_LIKE_CORTEX_M4', None), ('DEVICE_SPISLAVE', '1'), ('DEVICE_PORTIN', '1'), ('TARGET_UVISOR_UNSUPPORTED', None), ('TARGET_DEBUG', None), ('DEVICE_LOWPOWERTIMER', '1'), ('DEVICE_SPI_ASYNCH', '1'), ('DEVICE_PORTOUT', '1'), ('__CMSIS_RTOS', None), ('__MBED_CMSIS_RTOS_CM', None), ('USB_STM_HAL', None), ('DEVICE_PWMOUT', '1'), ('ARDUINO_{build_board}', None), ('TRANSACTION_QUEUE_SIZE_SPI', '2'), ('DEVICE_ERROR_RED', '1'), ('DEVICE_QSPI', '1'), ('TARGET_STM32F4', None), ('__FPU_PRESENT', '1'), ('__MBED__', '1'), ('TOOLCHAIN_GCC_ARM', None), ('TARGET_FF_ARDUINO', None), ('ARDUINO_ARCH_{build_arch}', None), ('TARGET_M4', None), ('TARGET_CORTEX_M', None), ('TARGET_AZ3166', None), ('DEVICE_SDIO', '1'), ('TARGET_STM', None), ('TARGET_LIKE_MBED', None), ('ARDUINO', '{runtime_ide_version}'), ('DEVICE_CAN', '1'), ('DEVICE_I2C', '1'), ('DEVICE_SERIAL_ASYNCH', '1'), ('DEVICE_I2CSLAVE', '1'), ('TOOLCHAIN_object', None), ('DEVICE_SPI', '1'), ('HSE_VALUE', '((uint32_t)26000000)'), ('MBED_BUILD_TIMESTAMP', '1490085708.63'), ('TARGET_RTOS_M4_M7', None), ('DEVICE_ANALOGIN', '1'), ('DEVICE_SERIAL', '1'), ('ARM_MATH_CM4', None), ('DEVICE_TRNG', '1'), ('DEVICE_STDIO_MESSAGES', '1'), ('TARGET_MXCHIP', None), ('DEVICE_INTERRUPTIN', '1'), ('DEVICE_RTC', '1'), ('MXCHIP_LIBRARY', None), ('__CORTEX_M4', None), ('DEVICE_SERIAL_FC', '1'), ('LPS22HB_I2C_PORT', 'MICO_I2C_1'), ('DEVICE_I2C_ASYNCH', '1'), ('DEVICE_PORTINOUT', '1'), ('DEVICE_SLEEP', '1'), ('TARGET_FF_MORPHO', None), ('TOOLCHAIN_GCC', None), ('TARGET_LIKE_CORTEX_M4', None), ('DEVICE_SPISLAVE', '1'), ('DEVICE_PORTIN', '1'), ('TARGET_UVISOR_UNSUPPORTED', None), ('TARGET_DEBUG', None), ('DEVICE_LOWPOWERTIMER', '1'), ('DEVICE_SPI_ASYNCH', '1'), ('DEVICE_PORTOUT', '1'), ('__CMSIS_RTOS', None), ('__MBED_CMSIS_RTOS_CM', None), ('USB_STM_HAL', None), ('DEVICE_PWMOUT', '1'), ('ARDUINO_{build_board}', None), ('TRANSACTION_QUEUE_SIZE_SPI', '2'), ('DEVICE_ERROR_RED', '1'), ('DEVICE_QSPI', '1'), ('TARGET_STM32F4', None), ('__FPU_PRESENT', '1'), ('__MBED__', '1'), ('TOOLCHAIN_GCC_ARM', None), ('TARGET_FF_ARDUINO', None), ('ARDUINO_ARCH_{build_arch}', None), ('TARGET_M4', None), ('TARGET_CORTEX_M', None), ('TARGET_AZ3166', None), ('DEVICE_SDIO', '1'), ('TARGET_STM', None), ('TARGET_LIKE_MBED', None), ('ARDUINO', '{runtime_ide_version}'), ('DEVICE_CAN', '1'), ('DEVICE_I2C', '1'), ('DEVICE_SERIAL_ASYNCH', '1'), ('DEVICE_I2CSLAVE', '1'), ('TOOLCHAIN_object', None), ('DEVICE_SPI', '1'), ('HSE_VALUE', '((uint32_t)26000000)'), ('MBED_BUILD_TIMESTAMP', '1490085708.63'), ('TARGET_RTOS_M4_M7', None), ('DEVICE_ANALOGIN', '1'), ('DEVICE_SERIAL', '1'), ('ARM_MATH_CM4', None), ('DEVICE_TRNG', '1'), ('DEVICE_STDIO_MESSAGES', '1'), ('TARGET_MXCHIP', None), ('DEVICE_INTERRUPTIN', '1')],
    LIBPATH=['{build_path}', '{build_system_path}', '{build_system_path}/az3166-driver', '{build_system_path}/az3166-driver/libwlan/TARGET_EMW1062'],
    LIBS=['stdc++', 'devkit-sdk-core-lib', 'wlan', 'stsafe', 'm'],
    LINKFLAGS=['-mcpu={build_mcu}', '-mthumb', '-O2', '-g', '-Wl,--cref', '-Wl,--check-sections', '-Wl,--gc-sections', '-Wl,--unresolved-symbols=report-all', '-Wl,--warn-common', '-Wl,--warn-section-align', '-T{build_variant_path}/{build_ldscript}', '-Wl,-Map,{build_path}/{build_project_name}.map', '-Wl,--gc-sections', '-Wl,--wrap,_malloc_r', '-Wl,--wrap,_free_r', '-Wl,--wrap,_realloc_r', '-Wl,--wrap,_calloc_r', '-Wl,--start-group', '{build_path}/{archive_file}', '-Wl,--end-group', '-gcc', '--specs=nano.specs', '--specs=nosys.specs', '-u', '_printf_float'],
    LIBSOURCE_DIRS=[join(FRAMEWORK_DIR, "libraries")]
)

BOARD_SUBS = dict(
    build_arch="STM32",
    build_board=board.get("build.board"),
    build_core_path=join(FRAMEWORK_DIR, "cores", board.get("core")),
    build_mcu=board.get("build.cpu"),
    build_path=FRAMEWORK_DIR,
    build_project_name="pio-project",
    build_system_path=join(FRAMEWORK_DIR, "system"),
    build_variant_path=join(FRAMEWORK_DIR, "variants",
                            board.get("build.variant")),
    build_ldscript=board.get(
        "build.ldscript", board.get("build.arduino.ldscript")),
    runtime_ide_version=10813
)

def expand(def_str: AnyStr, def_index: Dict[AnyStr, AnyStr]) -> AnyStr:
    class fmt_dict(dict):
        def __missing__(self, key):
            return f"{key}"

    substitutions = fmt_dict(def_index)
    before_expansion = def_str
    after_expansion = def_str.format_map(substitutions)
    while before_expansion != after_expansion:
        before_expansion = after_expansion
        after_expansion = after_expansion.format_map(substitutions)

    return after_expansion

def expand_dict(d: Dict[AnyStr, Any], subs: Dict[AnyStr, AnyStr]) -> Dict[AnyStr, Any]:
    result = dict()
    for key, val in d.items():
        key = expand(key, subs)

        if isinstance(val, str):
            result[key] = expand(val, subs)
        elif isinstance(val, tuple):
            result[key] = tuple(expand(token, subs) for token in val)
        elif isinstance(val, list):
            result[key] = [expand(token, subs) for token in val]
    return result


COMPILE_OPTS = expand_dict(COMPILE_OPTS, BOARD_SUBS)


env.Append(
    ASFLAGS=COMPILE_OPTS["ASFLAGS"],
    CFLAGS=COMPILE_OPTS["CFLAGS"],
    CCFLAGS=COMPILE_OPTS["CCFLAGS"],
    CXXFLAGS=COMPILE_OPTS["CXXFLAGS"],
    CPPDEFINES=COMPILE_OPTS["CPPDEFINES"],
    LIBPATH=COMPILE_OPTS["LIBPATH"],
    LIBS=COMPILE_OPTS["LIBS"],
    LINKFLAGS=COMPILE_OPTS["LINKFLAGS"],
    LIBSOURCE_DIRS=COMPILE_OPTS["LIBSOURCE_DIRS"]
)

env.Replace(LDSCRIPT_PATH=BOARD_SUBS['build_ldscript'])
