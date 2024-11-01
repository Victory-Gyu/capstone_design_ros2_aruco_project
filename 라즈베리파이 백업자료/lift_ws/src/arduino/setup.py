from setuptools import setup

package_name = 'arduino'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ubuntu',
    maintainer_email='ubuntu@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
              'lift_test   = arduino.script.lift_test:main',
              'remote_tb3  = arduino.script.remote_tb3:main',
              'remote_tb3_lift   = arduino.script.remote_tb3_lift:main',
              'remote_turtle   =arduino.script.remote_turtle:main',
              'sub_lift_msg    = arduino.script.sub_lift_msg:main'
        ],
    },
)
