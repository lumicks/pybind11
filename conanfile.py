from conans import ConanFile, tools, CMake


class PyBind11Conan(ConanFile):
    name = "pybind11"
    version = "2.6.1"
    settings = "os", "compiler", "arch", "build_type"
    description = "Seamless operability between C++11 and Python"
    homepage = "https://github.com/pybind/pybind11"
    license = "BSD Style: https://github.com/pybind/pybind11/blob/master/LICENSE"
    url = "https://github.com/conan-community/conan-pybind11"
    exports_sources = ["CMakeLists.txt", "LICENSE", "include/*", "pybind11/*", "tests/*", "tools/*"]

    def build(self):
        cmake = CMake(self)
        cmake.definitions["PYBIND11_TEST"] = False
        cmake.configure()
        cmake.build()
        cmake.install()

    def package(self):
        self.copy("LICENSE", dst="licenses", keep_path=False)
  
    def package_id(self):
        self.info.header_only()
