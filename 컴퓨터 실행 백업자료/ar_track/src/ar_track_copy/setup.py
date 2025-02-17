from setuptools import find_packages
from setuptools import setup

package_name = 'ar_track'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['ar_track/resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lee ju hyun',
    maintainer_email='02stu4@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'pub_tb3_pose2d  = ar_track.script.pub_tb3_pose2d:main',
            'stop_tb3        = ar_track.script.stop_tb3:main',
            'track_marker    = ar_track.script.track_marker:main',
        ],
    },
)
