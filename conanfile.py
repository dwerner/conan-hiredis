from conans import ConanFile
import os
from conans.tools import download
from conans.tools import unzip
from conans import CMake

class HiredisConan(ConanFile):
    name = "hiredis"
    version = "0.13.3"
    ZIP_FOLDER_NAME = "hiredis-%s" % version
    generators = "cmake"
    settings = "os", "arch", "compiler", "build_type"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    url="http://github.com/dwerner/conan-hiredis"
    license="https://github.com/google/googletest/blob/master/googletest/LICENSE"
    exports="FindHiredis.cmake"
    zip_name = "v%s.zip" % version
    unzipped_name = "hiredis-%s" % version

    def source(self):
        url = "https://github.com/redis/hiredis/archive/%s" % self.zip_name
        download(url, self.zip_name)
        unzip(self.zip_name)
        os.unlink(self.zip_name)

    def build(self):
        cd_build = "cd %s" % self.unzipped_name
        self.run("%s && make" % cd_build)

    def package(self):
        # Copy findHiredis script into project
        self.copy("FindHiredis.cmake", ".", ".")

        # Copying headers
        self.copy(pattern="*.h", dst="include", src=".", keep_path=False)

        # Copying static and dynamic libs
        self.copy(pattern="*.a", dst="lib", src=".", keep_path=False)
        self.copy(pattern="*.lib", dst="lib", src=".", keep_path=False)
        self.copy(pattern="*.dll", dst="bin", src=".", keep_path=False)
        self.copy(pattern="*.so*", dst="lib", src=".", keep_path=False)
        self.copy(pattern="*.dylib*", dst="lib", src=".", keep_path=False)      

    def package_info(self):
        self.cpp_info.libs = ['hiredis']
