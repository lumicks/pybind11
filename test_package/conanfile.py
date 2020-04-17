from conans import ConanFile, CMake
import os
import sys


class Pybind11TestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        self.cmake_build_folder = cmake.build_folder

    def test(self):
        sys.path.append(os.path.join(self.cmake_build_folder, "bin"))
        sys.path.append(os.path.join(self.cmake_build_folder, "lib"))

        import example
        self.output.info("2 + 3 == %s" % example.add(2, 3))
        assert example.add(2, 40) == 42
