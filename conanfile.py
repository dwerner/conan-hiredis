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

    def source(self):
        zip_name = "v%s.zip" % self.version
        url = "https://github.com/redis/hiredis/archive/" % zip_name
        download(url, zip_name)
        unzip(zip_name)
        os.unlink(zip_name)

    def build(self):
        if self.settings.os == "Windows":
            self.run("IF not exist _build mkdir _build")
        else:
            self.run("mkdir _build")
        cd_build = "cd _build"
        self.run("%s && make" % (cd_build))

    def package(self):
        # Copying headers
        self.copy(pattern="*.h", dst="include", src=".", keep_path=false)

        # Copying static and dynamic libs
        self.copy(pattern="*.a", dst="lib", src=".", keep_path=False)
        self.copy(pattern="*.lib", dst="lib", src=".", keep_path=False)
        self.copy(pattern="*.dll", dst="bin", src=".", keep_path=False)
        self.copy(pattern="*.so*", dst="lib", src=".", keep_path=False)
        self.copy(pattern="*.dylib*", dst="lib", src=".", keep_path=False)      

    def package_info(self):
        self.cpp_info.libs = ['hiredis']
